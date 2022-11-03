from pprint import pprint

import requests
import MyInfo
import pickle
from bs4 import BeautifulSoup


HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }

def authorization(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    login = MyInfo.LOGIN_olx
    pasword = MyInfo.PASSWORD_olx

    datas = {
        'login[email_phone]': login,
        'login[password]': pasword
    }
    session = requests.Session()
    authorisation = session.post(url, headers=headers, data=datas)
    print(authorisation.status_code)
    pickle.dump(session.cookies, open('C:/Users/User/PycharmProjects/Parsers'
                                       '/venv/Cookies/olx.cookies', 'wb'))


    cokies_dict = [
        {
            'domain': key.domain,
            'name': key.name,
            'path': key.path,
            'value': key.value
    }
        for key in session.cookies
    ]

    session2 = requests.Session()
    for cookies in cokies_dict:
        session2.cookies.set(**cookies)

    params = {
        # 'Host': 'www.olx.ua:443',
        # 'Accept': '*/*',
        # 'Authorization': 'Bearer 31486c100bfef1411a34fba9b0b926b0f880af81',

    }

    # responce = session2.get('https://www.olx.ua/myaccount/answers/?my_ads=0',
    #                         headers=HEADERS)
    # #
    # print(responce.status_code)
    #
    # print(responce.text) # виден мой регистрационный ключ в html- коде

    responceapi = session2.get(
        'https://www.olx.ua/api/v1/targeting/data/?page=ad&params%5Bad_id%5D'
        '=730060033&dfp_user_id=fb2a7982-cce3-40fd-970e-79bee661e94d-ver2&advertising_test_token&user_id=16073811',
        # 'https://www.olx.ua/api/v1/offers/760615654/phone-view/',
        headers=HEADERS)

    data = responceapi.json()

    print(responceapi.status_code)
    # pprint(data['data']['targeting'])

    responseinfo3 = session.get('https://www.olx.ua/api/v1/offers/721692100',
                                 headers=headers)
    # data3 = responseinfo3.json()
    pprint(responseinfo3.json()['data'])



def parsing(url):
    session2 = requests.Session()
    for cookies in pickle.load(open('C:/Users/User/PycharmProjects/Parsers'
                                       '/venv/Cookies/olx.cookies', 'rb')):
        session2.cookies.set(cookies,
                             "the cookie works",
                             domain="example.com")

    with session2:
        responce = session2.get(url, timeout=10)

        print(responce.text)


def main():
    url = 'https://www.olx.ua/account/'
    authorization(url)
    # parsing('https://www.olx.ua/myaccount/answers/?my_ads=0')


if __name__ == '__main__':
    main()