import time
import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram import KeyboardButton      # формируем кнопку
from telegram import ReplyKeyboardMarkup # формируем кнопку
from telegram import ReplyKeyboardRemove # удаление кнопки после нажатия
from queue import Queue
import json

LINKS = []
queue_old_auto = Queue()
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
           'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
TIMEOUT = 10


import MyInfo

button_yes = 'Да'
button_no = 'Нет'
button_model = 'Модель'


models_auto = ['bmw', 'subaru', 'chevrolet', 'audi', 'ford', 'honda', 'kia',
               'hyundai', 'lexus', 'mazda', 'mercedes-benz', 'mitsubishi',
               'nissan', 'opel', 'peugeot', 'renault', 'skoda', 'toyota',
               'volkswagen', 'volvo', 'geely', 'citroen']

models_volkswagen = ['touareg', 'golf-v', 'passat-b8', 'tiguan', 'jetta', 'polo']


# создадим декоратор, для отлавливания синтакс.ошибок
def log_error(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as err:
            print(f'Ошибка: {err}')
            raise err
    return inner()


# добавляем обработчик
def button_yes_handler(update: Update, context: CallbackContext):
    reply_but = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_model),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text=f'Нажми на кнопку {button_model} авто',
        reply_markup=reply_but,
    )

def disappier_button(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Напиши модель из приведенных ниже: ',
    )
    n = pars_models_autoria()
    for i in n:
        update.message.reply_text(
            text=f'{i}',
    reply_markup=ReplyKeyboardRemove(),

        )

def button_no_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Нет, так нет!!! До свидания!!!'
    )

def choose_auto(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Напишите, модель, которую вы выбрали',
        reply_markup=ReplyKeyboardRemove(),
    )

def parsing_single_model(update, context):
    update.message.reply_text(
        text=f'Вы выбрали {update.message.text}. Запускаю процесс...'
    )
    url = 'https://auto.ria.com/uk/car/' + update.message.text
    print(url)
    parsing_for_links(url)
    update.message.reply_text(
        text=f'Ждите... еще немного...'
    )
    out = get_number_old_car(queue_old_auto)
    for i in out[0:3]:
        for v in i.values():
            update.message.reply_text(
                text=f'{v}',
            )

    for i in out[3:5]:
        for v in i.values():
            update.message.reply_text(
                text=f'{v}',
            )
    try:
        for i in out[5:8]:
            for v in i.values():
                update.message.reply_text(
                    text=f'{v}',
                )
    except Exception as err:
        raise (err, 'No more')

    try:
        for i in out[8:]:
            for v in i.values():
                update.message.reply_text(
                    text=f'{v}',
                )
    except Exception as err:
        raise (err, 'No more')

    update.message.reply_text(
        text='Сбор данных окончен. Еще...?'
    )

    button_yes_handler(update, context)

def parsing_for_links(url):
    with requests.Session() as session:
        responce = session.get(url, headers=HEADERS)
        assert responce.status_code == 200, 'BAD RESPONCE'

        print(responce.status_code)

        soup = BeautifulSoup(responce.content, 'html.parser')

        links = soup.select('.head-ticket div a')

        for link in range(len(links)):
            for el in links[link].get('href').split('/'):
                if el == 'newauto':
                    break
            else:
                queue_old_auto.put(links[link].get('href'))

        # print(link)
        # return LINKS

def get_number_old_car(queue: Queue):
    INFO = []
    while queue.qsize() > 0:
        print(f'Нужно oбработать {queue.qsize()} страниц')
        url = queue.get()
        print(url, queue.qsize())
        with requests.Session() as session:
            responce = session.get(url, headers=HEADERS, timeout=TIMEOUT)

            content = responce.text
            soup = BeautifulSoup(content, 'lxml')
            idexc = url.split('_')[-1][:8]
            marca_model = url.split('_')[-2]

            try:

                title = soup.select('.head')[0].text.rstrip()
                manufacture_year = title.lstrip()[-4:]
                price = soup.select('#showLeftBarView section div strong')[
                    0].text.strip(' ')
                sale_name = ' '.join(
                    soup.select('#showLeftBarView section div')[
                        3].text.strip(' ').split(' ')[0:2]).replace('На', '')
                mile = \
                soup.select('#showLeftBarView section div')[2].text.strip(' '
                                '').split(' ')[0] + ' тис.км'

                hesh = soup.findAll('script')[38].get('data-hash')

                print(title)
                print(price)
                print(mile)
                print(sale_name)

                # print(idexc)
                # print(hesh)
                urlphone = f'https://auto.ria.com/users/phones/{idexc}?hash=' \
                        f'{hesh}&expires=2592000'

                jsonhesh = requests.get(urlphone)
                print(jsonhesh.json()['formattedPhoneNumber'])
                phone_number = jsonhesh.json()['formattedPhoneNumber']
            except Exception as error:
                print('Such does not work')
        INFO.append({
            'car model': title,
            # 'marka modeli': marca_model,
            # 'manufacture year': manufacture_year,
            'price': price,
            'miles': mile,
            'saller': sale_name,
            'phone': phone_number,
            'link': url
        })
    print(queue.qsize())
    return INFO

def pars_models_autoria():
    url = 'https://auto.ria.com/uk/'
    with requests.Session() as session:
        response = session.get(url, timeout=10)
        assert response.status_code == 200, 'BAD RESPONCE'
        print(response.status_code)

        soup = BeautifulSoup(response.content, 'html.parser')

        models = soup.select('#brandTooltipBrandAutocomplete-brand li')

        m = []
        for i in range(1, 20):
            m.append(models[i].text.strip().lower())
        m.append('Geely'.lower())
        m.append('subaru'.lower())
        m.append('citroen'.lower())

        return m

def choose_marka_volkswagen(update, context):
    reply_but = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=str(models_volkswagen[0])),
                KeyboardButton(text=str(models_volkswagen[1])),
                KeyboardButton(text=models_volkswagen[2]),
                KeyboardButton(text=models_volkswagen[3]),
                KeyboardButton(text=models_volkswagen[4]),
                KeyboardButton(text=models_volkswagen[5]),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text='Выбери марку модели Volkswagen',
        reply_markup=reply_but,
    )
    time.sleep(4)


def parsing_model_volkswagen(update, context):
    update.message.reply_text(
        text=f'Вы выбрали {update.message.text}. Запускаю процесс...'
    )
    print(update.message.text)
    url = 'https://auto.ria.com/car/volkswagen/' + update.message.text
    print(url)
    parsing_for_links(url)
    update.message.reply_text(
        text=f'Ждите... еще немного...'
    )
    out = get_number_old_car(queue_old_auto)
    for i in out[0:3]:
        for v in i.values():
            update.message.reply_text(
                text=f'{v}',
            )

    for i in out[3:5]:
        for v in i.values():
            update.message.reply_text(
                text=f'{v}',
            )
    try:
        for i in out[5:8]:
            for v in i.values():
                update.message.reply_text(
                    text=f'{v}',
                )
    except Exception as err:
        raise (err, 'No more')

    try:
        for i in out[8:]:
            for v in i.values():
                update.message.reply_text(
                    text=f'{v}',
                )
    except Exception as err:
        raise (err, 'No more')

    update.message.reply_text(
        text='Сбор данных окончен. Еще...?'
    )

    button_yes_handler(update, context)


def start_command(update, context):
    reply_murkap = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_yes),
                KeyboardButton(text=button_no),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text='Привет. Начнем заново...',
        reply_markup=reply_murkap,
    )


def wrong_model(update, context):
    update.message.reply_text(
        text=f'Вы написали {update.message.text}. Такой модели нет...'
    )
    start_command(update=update, context=context)


# добавляем обработчик
def message_handler(update: Update, context: CallbackContext):
    # обработка сообщения из кнопки
    text = update.message.text  # это и есть тот текст, который нам прислан
    if text == button_yes:
        return button_yes_handler(update=update, context=context)
    if text == button_no:
        return button_no_handler(update=update, context=context)
    if text == button_model:
        disappier_button(update=update, context=context)
        return choose_auto(update=update, context=context)
    if text.lower() == 'volkswagen':
        choose_marka_volkswagen(update=update, context=context)
        time.sleep(2)
    if text.lower() in models_volkswagen:
        parsing_model_volkswagen(update=update, context=context)
    if text.lower() in models_auto and text.lower() != 'volkswagen':
        parsing_single_model(update=update, context=context)
    else:
        return wrong_model(update=update, context=context)


    # описывем и добавляем кнопку. Перед этм кнопку назвали
    reply_murkup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_yes),
                KeyboardButton(text=button_no),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text='Привет. Я Бот. Хочешь новинки с autoria?',
        reply_markup=reply_murkup,
    )

def main():
    print('Start')
    # updater - конструкция, кот идет в телеграмм за обновлениями
    updater = Updater(
        token=MyInfo.yablonvlbot_token,
        use_context=True
    )
    # сейчас напишем код, блокирует ли провайдер Телеграм-бот
    print(updater.bot.get_me()) # метод get_me возвращает инф-ю о боте
    # Запуск самого бота нужно комментировать. Если инфа есть, то бот работает
    ###################################################
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all,
                                                  callback=message_handler))

    updater.start_polling()
    updater.idle()

    print('Finish') # для проверки блокировки
if __name__ == '__main__':
    main()