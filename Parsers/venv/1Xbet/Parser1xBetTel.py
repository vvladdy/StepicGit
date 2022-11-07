import time
from pprint import pprint
import re
import requests
import json
import MyInfo

from telegram import (
    Update,
    KeyboardButton,
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup
)

from telegram.ext import (
    CallbackContext,
    MessageHandler,
    Filters,
    Updater
)


class xBetParser:
    TIMEOUT = 10
    sport_ev_rus = []
    sport_ev_eng = []
    INFO = []

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                      'KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    def __init__(self, url):
        self.url = url

    def parsing_sport_events(self, url):
        get_req = requests.get(url)
        json_text = get_req.json()
        pprint(json_text)
        with open('sport_event.json', 'w', encoding='utf-8') as file:
            json.dump(json_text, file, indent=4, ensure_ascii=False)
        # info_from_json = json_text['Value']
        # pprint(info_from_json)

    def parsing_single_event(self):
        xBetParser.INFO = []
        url_test = self.url
        try:
            champ = re.search(r'\d{3,}', url_test)
            # print(champ)
            champs = int(champ[0])
            del_champ = f'&champs={champs}'
        except Exception as err:
            del_champ = ''
        sports = url_test.split('/')
        sport = sports[-2]
        print(sport)
        sport_split = '-'.join((str(sport).split(' ')))
        print(sport_split)
        sport_ID = 0
        with open('sport_event.json', 'rb') as f:
            sport_id = json.load(f)

            for i in sport_id['Value']:
                if '-'.join((i['E'].lower()).split(' ')) == sport:
                    sport_ID = i['I']
                    # print(i['I'], i['E'])
        print(sport_ID)
        json_single_sport = requests.get(
            f'https://1xbet.mobi/LiveFeed/Get1x2_VZip?sports={sport_ID}'
            f'{del_champ}&count=50&lng=ua&mode=4&country=2&getEmpty=true&mobi'
            f'=true', headers=self.headers)
        # pprint(json_single_sport.json())
        koeff = json_single_sport.json()['Value']
        pprint(koeff)
        for i in koeff:
            xBetParser.INFO.append(f"{i['O1E']} - {i['O2E']} -- "
                         f" {[m['C'] for m in i['E']]}")
            print(f"{i['O1R']} - {i['O2R']} --  {[m['C'] for m in i['E']]}")

            # for j in i['E']:
            #     pprint(j['C'])


    def start(self):
        with requests.Session() as session:
            self.response = session.get(self.url, timeout=self.TIMEOUT)
        if self.response.status_code == 200:
            print(self.response.status_code)
            self.parsing_single_event()
        else:
            print('BAD RESPONCE')

# if __name__ == '__main__':
#
#     url = 'https://1xbet.mobi/ua/live/handball/1161141-turkey-superliga'
#
#     if url.split('/')[-2] == 'live':
#         url_p = url + '/text'
#     else:
#         url_p = url
#     print(url_p)
#     date = xBetParser(url_p)
#     date.start()

    # Не работают конные гонки, так как в них нет игрок1-игрок2

class TelegrBot():

    button_no = 'NO'
    button_yes = 'YES'

    def answer_no(self, update, context):
        update.message.reply_text(
            text='Нет, так нет. До свидания!!!'
        )

    def answer_yes(self, update, context):
        update.message.reply_text(
            text='Введите ссылку на интересующее событие:',
            reply_markup=ReplyKeyboardRemove(),
        )
        time.sleep(5)

    def del_info(self, update, context):
        pass

    def start_parsing(self, update, context):
        url = update.message.text
        if url.split('/')[-2] == 'live':
            url_p = url + '/text'
        else:
            url_p = url
        print(url_p)
        date = xBetParser(url_p)
        date.start()

        for i in xBetParser.INFO:
            update.message.reply_text(
                text=i
            )

    def message_handler(self, update: Update, context: CallbackContext):
        text = update.message.text
        if text == 'YES'.upper():
            return self.answer_yes(update=update, context=context)
        if text == 'NO'.upper():
            return self.answer_no(update=update, context=context)
        if text.split('/')[0] == 'https:':
            return self.start_parsing(update=update, context=context)
        reply_markap = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=self.button_yes),
                    KeyboardButton(text=self.button_no),
                ],
            ],
            resize_keyboard=True
        )

        update.message.reply_text(
            text='Привет. Я бот 1xBet. Хочешь увидеть реальные коэффициенты?',
            reply_markup=reply_markap,
        )

    def start_bot(self):
        self.updater = Updater(
            token=MyInfo.yablonvlbot_token,
            use_context=True
        )

        self.updater.dispatcher.add_handler(
            MessageHandler(
                filters=Filters.text, callback=self.message_handler
            ))
        self.updater.start_polling()
        self.updater.idle()
#
if __name__ == '__main__':
    s = TelegrBot()
    s.start_bot()