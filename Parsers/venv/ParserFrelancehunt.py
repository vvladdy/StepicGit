import json
import pickle
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import MyInfo as secret

INFO = []
user = UserAgent().random
link_arr = []

LOGIN = secret.LOGIN_frilance
PASSWORD = secret.PASSWORD_freelance

HEADERS = {
    'user-agent': user
}


def cookie_collect(url):
    datas = {'login': LOGIN, 'password': PASSWORD}

    session = requests.Session()

    autorisation = session.post(url, headers=HEADERS, data=datas)

    print(autorisation.status_code)

    # запись cookies в файл
    pickle.dump(session.cookies, open(
        'C:/Users/User/PycharmProjects/Parsers/venv/Cookies/frelance.cookies',
        'wb'))

def parsing():
    # чтение cookies из файла
    session2 = requests.Session()
    for cookies in pickle.load(open(
     'C:/Users/User/PycharmProjects/Parsers/venv/Cookies/frelance.cookies',
            'rb')):

        session2.cookies.set(**cookies)

    with session2:
        response = session2.get(
            'https://freelancehunt.com/projects?skills%5B%5D=22',
                        headers=HEADERS, timeout=10)
        print(response.status_code)

        soup = BeautifulSoup(response.content, 'html.parser')
        pages = int(soup.select('.pagination a')[-2].text)
        for page in range(1, pages+1):
            print('Парсинг страницы: ',page)
            response_p = session2.get(
                f'https://freelancehunt.com/projects?skills%5B%5D=22&page={page}',
                headers=HEADERS, timeout=10)
            soup = BeautifulSoup(response_p.content, 'html.parser')

            block = soup.select('.left')

            description = soup.select('.left')

            links = soup.select('.left a')

            # descript = ' '.join(description[0].text.rstrip().split('\n'))
            # title = ' '.join(descript.split(' ')[:10]).strip()


            for link in range(len(links)):
                for el in links[link].get('href').split('/'):
                    if el == 'project':
                        link_arr.append(links[link].get('href'))
                        # print(links[link].get('href'))

            for el in range(len(block)):
                INFO.append(
                    {
                        'title': (' '.join(
                            (' '.join(description[el].text.rstrip().split('\n'))
                             ).split(' ')[:10]).strip()),
                        'task': (' '.join(
                            (' '.join(description[el].text.rstrip().split('\n'))
                             ).split(' ')[10:-5]).replace('Приветствую', ''
                                                         ).strip(' +')),
                        'link': link_arr[el]#links[el].get('href')
                    }
                )
        return INFO

def writejson():
    with open ('freelanse.json', 'w', encoding='utf-8') as file:
        json.dump(INFO, file, indent=4, ensure_ascii=False)

def main():
    url = 'https://freelancehunt.com/profile/login'
    # cookie_collect(url)
    parsing()
    writejson()

if __name__ == '__main__':
    main()
