# Парсинг сайта https://inventure.com.ua с динамической подгрузкой страниц

import json
import time
import requests
from bs4 import BeautifulSoup
from queue import Queue


TIMEOUT = 20
headers = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def connection(url, page: int):
    print('Парсинг страницы {} начался'.format(page))
    with requests.Session() as session:
        responce = session.get(url, timeout=TIMEOUT, headers=headers)
        assert responce.status_code == 200, 'Bad response'
        print(responce.status_code)

        with open (f'page{page}.html', 'w', encoding="utf-8") as file:
            file.write(responce.text)

        # with open('project3.html', encoding='utf-8') as file:
        #     src = file.read()
        # soup = BeautifulSoup(src, 'html.parser')

        soup = BeautifulSoup(responce.content, 'html.parser')

        links = soup.select('.cards__item')
        linklist = []
        queue = Queue()
        for art in range(len(links)):
            queue.put('https://inventure.com.ua/'+ links[art].get('href'))
            linklist.append('https://inventure.com.ua/'+ links[art].get('href'))
        # print(linklist)
        print(queue.qsize())

        titles = soup.select('.cards__title')
        invest_cost = soup.select('.price-tag')
        public_date = soup.select('.opacity-75')

        titlelist = [titles[title].text.rstrip() for title in range(len(
            titles))]
        # print(len(titlelist))

        # invest_cost_list = []
        # for i in range(len(invest_cost)):
        #     invest_cost_list.append(invest_cost[i].text.rstrip())
        #     # print (invest_cost[i].text.rstrip())
        # print(len(invest_cost_list))

        # public_date_list = []
        # for i in range(0, len(public_date), 2):
        #     public_date_list.append(public_date[i].text.rstrip())
        #     # print(public_date[i].text.rstrip())
        # print(len(public_date_list))

        info = []
        for i in range(0, len(titlelist)):
            info.append(
                {
            'название проекта': titles[i].text.rstrip(),
            'стоимость инвестиций': invest_cost[i].text.rstrip(),
            'ссылка на прoект': 'https://inventure.com.ua/' +
                                links[i].get('href'),
            'дата публикации': public_date[i*2].text.rstrip()
            })
        # print(info)

        with open(f'info{page}.json', 'w', encoding='utf-8') as file:
            json.dump(info, file, indent=4, ensure_ascii=False)

    print('Парсинг страницы {} окончен'.format(page))
    time.sleep(3)

def main():
    url = 'https://inventure.com.ua/invest.php?action=get&limit=23'
    connection(url, 1)
    for page in range(2, 15):
        connection(f'https://inventure.com.ua/invest.php?lang=ru&locale=ru_RU'
                   f'.utf8&_params[action]=routing&_params['
                   f'url]=projects&cname=index&meta_priority['
                   f'0]=post&meta_priority[1]=rubric&meta_priority['
                   f'2]=category&meta_priority[3]=blog&page='
                   f'{page}&action=get&limit=23', page)

if __name__ == '__main__':
    main()