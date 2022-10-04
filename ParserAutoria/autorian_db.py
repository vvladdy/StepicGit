from peewee import (
    Model,
    SqliteDatabase,
    CharField,
    ForeignKeyField,
    IntegerField,
)

db = SqliteDatabase('autorian.db')


class BaseModel(Model):

    class Meta:
        database = db


class Price(BaseModel):
    name = CharField(max_length=255)
    price = IntegerField()


class Car(BaseModel):
    name = CharField(max_length=255)
    year = IntegerField()
    mileage = CharField(max_length=50, null=True)
    fuel = CharField(max_length=50, null=True)
    price = ForeignKeyField(Price)
    engine = CharField(max_length=50, null=True)

class LinkAuto(BaseModel):
    car = ForeignKeyField(Car)
    url = CharField(max_length=255)


if __name__ == '__main__':
    db.create_tables([Price, Car, LinkAuto])


# import json
#
# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint
#
# def choice_car(url, last_page):
#     with requests.Session() as session:
#
#         response = session.get(url, timeout=20)
#
#         assert response.status_code == 200, 'Bad response'
#         print(response.status_code)
#
#     #response = requests.get(url=url, headers=headers)
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     page_count = int(soup.find('nav', class_="unstyle pager").find_all('span',
#                  class_="page-item mhide")[-1].text.replace(' ', '').strip())
#     # [-1] значит последняя запись, то есть последняя страница
#
#     print('Всего страниц для парсинга: {}'.format(page_count))
#     page_count = last_page
#     print('Установлено страниц: {}'.format(page_count))
#     autoria_arr = []
#     for page in range(1, page_count + 1):
#         print(f'Обработка {page} страницы...')
#         urlp = f'https://auto.ria.com/uk/legkovie/?page={page}'
#         response = requests.get(url=urlp)
#
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         cars = soup.select('.content ')
#         for car in cars:
#             name = car.select('div')
#            # print(name[0].find('span', class_="blue bold").text.rstrip())
#             year = car.select('a')
#             #print(year[0].text.rstrip().split()[-1])
#             price = car.select('span')
#             #print(int(price[2].text.replace(' ', '')))
#             link = car.select('a')
#             #print(link[0].get('href'))
#             drive = car.select('ul', class_="unstyle characteristic")
#             drive = car.select('ul')
#             # print(drive[0].find('li', class_="item-char js-race").text.strip())
#             fuel = drive
#             # print(fuel[0].find_all('li')[2].text.split(',')[0])
#             valengin = drive
#             try:
#                 volume = valengin[0].find_all('li')[2].text.split(',')[1]
#             except:
#                 volume = None
#             # print(valengin[0].find_all('li')[2].text.split(',')[1])
#
#             autoria = {
#                 'link': link[0].get('href') if link else None,
#                 'name': name[0].find('span', class_="blue bold").text.rstrip(),
#                 'year': f'{year[0].text.rstrip().split()[-1]}',
#                 'price': f"{int(price[2].text.replace(' ', ''))} USD",
#                 'mileage': drive[0].find('li', class_="item-char "
#                                                       "js-race").text.strip(),
#                 'fuel': fuel[0].find_all('li')[2].text.split(',')[0],
#                 'engine': volume
#             }
#             pprint(autoria)
#             autoria_arr.append(autoria)
#     print('PAGE SCRAPPED!!!')
#     return autoria_arr
#
# def write_json(file):
#     with open('autoria.json', 'w') as nfile:
#         json.dump(file, nfile, indent=4)
#
#
# if __name__ == '__main__':
#     url = 'https://auto.ria.com/uk/legkovie'
#     last_page = 3
#     pars_page = choice_car(url, last_page)
#     write_json(pars_page)

#
# price_for_db = {'price': int(price[2].text.replace(' ', ''))}
#                 link_for_db = {'link': link[0].get('href') if link else None}
#                 pricedb, _ = Price.create(**price_for_db)
#                 cardb, _ = Car.get_or_create(**autoria)
#                 linkdb, _ = LinkAuto.get_or_create(**link_for_db)