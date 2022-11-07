from pprint import pprint
import re
import requests
import json

class xBetParser:

    TIMEOUT = 10
    sport_ev_rus = []
    sport_ev_eng = []

    def __init__(self):
        pass

    def parsing_sport_events(self, url):
        get_req = requests.get(url)
        json_text = get_req.json()
        pprint(json_text)
        # with open('sport_event.json', 'w', encoding='utf-8') as file:
        #     json.dump(json_text, file, indent=4, ensure_ascii=False)
        info_from_json = json_text['Value']
        pprint(json_text)
        for sport_ev in info_from_json:
            self.sport_ev_rus.append(sport_ev['R'])
            self.sport_ev_eng.append(sport_ev['E'])
            # with open('sport_event_eng.txt', 'a+', encoding='utf-8') as file:
            #     if sport_ev['E'] not in file:
            #         file.write(sport_ev['E']+'\n')
            # with open('sport_event_rus.txt', 'a+', encoding='utf-8') as file:
            #     if sport_ev['R'] not in file:
            #         file.write(sport_ev['R']+'\n')
            # print(sport_ev['E'], sport_ev['R'])

    def parsing_single_event(self, url):
        get_req = requests.get(url)
        json_text = get_req.json()
        pprint(json_text)
        with open('sport_single_event.json', 'w', encoding='utf-8') as file:
            json.dump(json_text, file, indent=4, ensure_ascii=False)
        info_from_json = json_text['Value']
        pprint(json_text)


    def main(self, url):
        with requests.Session() as session:
            self.response = session.get(url, timeout=self.TIMEOUT)
        assert self.response.status_code == 200, 'BAD RESPONCE'
        print(self.response.status_code)
        self.parsing_sport_events(self.response.text)
        return self.response.content


if __name__ == '__main__':
    date = xBetParser()
    url = 'https://1xbet.mobi//live'
    url_events = 'https://1xbet.mobi/LiveFeed/GetSportsShortZip?sports=40&lng=ua&country=2&group=54&mobi=true'
    # sports_event = date.parsing_sport_events(url_events)

    # url_single_event = 'https://1xbet.mobi/LiveFeed/Get1x2_VZip?sports=4' \
    #    '&champs=2472355&count=50' #"цифра в sports= - это "I": 4 (номер
                                # спорта из sport_event.json)
    # champs=2472355 - чемпионат( число из url события), count= - любая цифра
    # кратная 5
    #&lng=ua&mode=4&country=2&getEmpty=true&mobi=true' -  не важно


    #single_event = date.parsing_single_event(url_single_event)

    #пример: Баскетбол - кубок
    # индонезии 'https://1xbet.mobi/ua/live/basketball/1356627-indonesia-cup'
    # get-запрос будет https://1xbet.mobi/LiveFeed/Get1x2_VZip?sports=3&champs=1356627&count=50&lng=ua&mode=4&country=2&getEmpty=true&mobi=true
    # где &lng=ua&mode=4&country=2&getEmpty=true&mobi=true - не обязательно
    # 'https://1xbet.mobi/LiveFeed/Get1x2_VZip?sports=3&champs=1356627&count=50'

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
           'KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    url_test = 'https://1xbet.mobi/ua/live/basketball/1369445-japan-b-league-division-3'

    champ = re.search(r'\d{2,}', url_test)
    champs = int(champ[0])
    print(champs)

    sport_ID = 0
    with open('sport_event.json', 'rb') as f:
        sport_id = json.load(f)
        sport = 'basketball'
        # pprint(sport_id['Value'])
        for i in sport_id['Value']:
            if i['E'].lower() == sport:
                sport_ID = i['I']
                print(i['I'], i['E'])


    json_single_sport = requests.get(
        f'https://1xbet.mobi/LiveFeed/Get1x2_VZip?sports={sport_ID}&'
        f'champs={champs}&count=50&lng=ua&mode=4&country=2&getEmpty=true&mobi'
        f'=true', headers=headers)
    pprint(json_single_sport.json())

# 'https://1xbet.mobi/LiveFeed/Get1x2_VZip?sports=3&champs=1369445&count=50&lng=ua&mode=4&country=2&getEmpty=true&mobi=true'
class TelegrBot:
    pass