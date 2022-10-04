import csv
import json

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re

from autorian_db import Price, Car, LinkAuto


# headers = { "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
# }
autoria_arr = []

def choice_car(url, last_page):
    with requests.Session() as session:

        response = session.get(url, timeout=20)

        assert response.status_code == 200, 'Bad response'
        print(response.status_code)

    #response = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    page_count = int(soup.find('nav', class_="unstyle pager").find_all('span',
                 class_="page-item mhide")[-1].text.replace(' ', '').strip())
    # [-1] значит последняя запись, то есть последняя страница

    print('Всего страниц для парсинга: {}'.format(page_count))
    page_count = last_page
    print('Установлено страниц: {}'.format(page_count))
    #autoria_arr = []
    for page in range(1, page_count + 1):
        print(f'Обработка {page} страницы...')
        urlp = f'https://auto.ria.com/uk/legkovie/?page={page}'
        response = requests.get(url=urlp)

        soup = BeautifulSoup(response.content, 'html.parser')

        cars = soup.select('.content ')
        for car in cars:
            name = car.select('div')
           # print(name[0].find('span', class_="blue bold").text.rstrip())
            year = car.select('a')
            #print(year[0].text.rstrip().split()[-1])
            price = car.select('span')
            #print(int(price[2].text.replace(' ', '')))
            link = car.select('a')
            #print(link[0].get('href'))
            drive = car.select('ul', class_="unstyle characteristic")
            drive = car.select('ul')
            # print(drive[0].find('li', class_="item-char js-race").text.strip())
            fuel = drive
            # print(fuel[0].find_all('li')[2].text.split(',')[0])
            valengin = drive
            try:
                volume = valengin[0].find_all('li')[2].text.split(',')[1]
            except:
                volume = None
            # print(valengin[0].find_all('li')[2].text.split(',')[1])

            autoria = {
                #'link': link[0].get('href') if link else None,
                'name': name[0].find('span', class_="blue bold").text.rstrip(),
                'year': f'{year[0].text.rstrip().split()[-1]}',
                'price': f"{int(price[2].text.replace(' ', ''))} USD",
                'mileage': drive[0].find('li', class_="item-char "
                                                      "js-race").text.strip(),
                'fuel': fuel[0].find_all('li')[2].text.split(',')[0],
               'engine': volume
            }
            car, _ = Car.get_or_create(**autoria)

            price = {
                'name': name[0].find('span', class_="blue bold").text.rstrip(),
                'price': f"{int(price[2].text.replace(' ', ''))} USD"
            }
            price, _ = Price.get_or_create(**price)

            link_for_db = link[0].get('href') if link else None
            link, _ = LinkAuto.get_or_create(car=car, url=link_for_db)

            pprint(autoria)
            autoria_arr.append(autoria)
    print('PAGE SCRAPPED!!!')
    return autoria_arr

def write_json(file):
    with open('autoria.json', 'w') as nfile:
        json.dump(file, nfile, indent=4)

def write_csv():
    fieldnames = (
        'name', 'price', 'year', 'mileage', 'fuel', 'engine', 'link',
    )
    with open('autoria.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for row in autoria_arr:
            writer.writerow(row)


if __name__ == '__main__':
    url = 'https://auto.ria.com/uk/legkovie'
    last_page = 20
    pars_page = choice_car(url, last_page)
    #write_json(pars_page)
    write_csv()
