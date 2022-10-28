import re
import time
from queue import Queue
import requests
from bs4 import BeautifulSoup
import json
import openpyxl
import telebot
import MyInfo
from telebot import types



class AutoParser:

    INFO = []
    LINKS = []
    queue_old_auto = Queue()
    queue_new_auto = Queue()
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    TIMEOUT = 10

    def __init__(self, model):
        self.model = model


    def parsing_url_for_pages(self, url):
        print(url)
        with requests.Session() as session:
            responce = session.get(url, headers=self.HEADERS)
            assert responce.status_code == 200, 'BAD RESPONCE'

            print(responce.status_code)

            soup = BeautifulSoup(responce.content, 'html.parser')

            self.pages = int(soup.select('.page-item')[-3].text.strip())

            print('Total pages', self.pages)


    def parsing_for_links(self, url):
        print('Working with link', url)
        with requests.Session() as session:
            responce = session.get(url, headers=self.HEADERS)
            assert responce.status_code == 200, 'BAD RESPONCE'

            print(responce.status_code)

            soup = BeautifulSoup(responce.content, 'html.parser')

            links = soup.select('.head-ticket div a')

            # LINKS = [links[link].get('href') for link in range(len(links))]

            public_dates = soup.select('.footer_ticket span span')

            # можно использовать очередь
            for link in range(len(links)):
                for el in links[link].get('href').split('/'):
                    if el == 'newauto':
                        break
                else:
                    self.queue_old_auto.put((
                        links[link].get('href'),
                        public_dates[link].text.strip(' ')))


            for link in range(len(links)):
                for el in links[link].get('href').split('/'):
                    if el == 'newauto':
                        self.queue_new_auto.put((
                            links[link].get('href'),
                            public_dates[link].text.strip(' ')))


    def get_number_old_car(self):
        while self.queue_old_auto.qsize() > 0:
            print(f'Нужно обработать {self.queue_old_auto.qsize()} ссылок')
            date = self.queue_old_auto.get()
            self.url = date[0]
            self.public_date = date[1]
            print('WORKIN ON: ', self.url, self.public_date,
                  self.queue_old_auto.qsize())
            with requests.Session() as session:
                responce = session.get(self.url, headers=self.HEADERS,
                                       timeout=self.TIMEOUT)

                content = responce.text
                soup = BeautifulSoup(content, 'lxml')
                idexc = self.url.split('_')[-1][:8]
                self.marca_model = self.url.split('_')[-2]

                try:

                    self.title = soup.select('.head')[0].text.rstrip()
                    self.manufacture_year = self.title.lstrip()[-4:]
                    self.price = soup.select('#showLeftBarView section div '
                        'strong')[0].text.strip(' ')
                    self.sale_name = ' '.join(
                        soup.select('#showLeftBarView section div')[
                        3].text.strip(' ').split(' ')[0:2]).replace('На', '')
                    self.mile = \
                        soup.select('#showLeftBarView section div')[
                            2].text.strip(' '
                                          '').split(' ')[0] + ' тис.км'

                    hesh = soup.findAll('script')[38].get('data-hash')

                    print(self.title)
                    print(self.price)
                    print(self.mile)
                    print(self.sale_name)
                    print(self.url)

                    url = f'https://auto.ria.com/users/phones/{idexc}?hash=' \
                          f'{hesh}&expires=2592000'

                    jsonhesh = requests.get(url)
                    print(jsonhesh.json()['formattedPhoneNumber'])
                    self.phone_number = jsonhesh.json()['formattedPhoneNumber']

                except Exception:
                    print('Such does not work')
            self.generate_info()


    def generate_info(self):
        self.INFO.append({
            'car model': self.title,
            'marka modeli': self.marca_model,
            'manufacture year': self.manufacture_year,
            'price': self.price,
            'miles': self.mile,
            'public date': self.public_date,
            'saller': self.sale_name,
            'phone': self.phone_number,
            'link': self.url
        })

    def json_to_excel(self, file):
        with open(file, 'rb') as f:
            datas = json.load(f)
        filecontent = openpyxl.Workbook()

        sheet = filecontent.active

        sheet['A1'] = 'car model'.upper()
        sheet['B1'] = 'year'.upper()
        sheet['C1'] = 'price'.upper()
        sheet['D1'] = 'miles'.upper()
        sheet['E1'] = 'public date'.upper()
        sheet['F1'] = 'saller'.upper()
        sheet['G1'] = 'phone'.upper()
        sheet['H1'] = 'link'.upper()

        row = 2
        for info in datas:
            sheet[row][0].value = info['car model']
            sheet[row][1].value = info['manufacture year']
            sheet[row][2].value = info['price']
            sheet[row][3].value = info['miles']
            sheet[row][4].value = info['public date']
            sheet[row][5].value = info['saller']
            sheet[row][6].value = info['phone']
            sheet[row][7].value = info['link']

            row += 1

        filecontent.save(f'Parser{self.model}.xlsx')
        filecontent.close()


    def write_json(self):
        with open(f'autoriaPars{self.model}.json', 'w', encoding='utf-8') as \
                self.file:
            json.dump(self.INFO, self.file, indent=4, ensure_ascii=False)

        return self.file

    def write_database(self):
        pass

    def get_number_new_car(self):
        while self.queue_old_auto.qsize() > 0:
            print(f'Нужно обработать {self.queue_old_auto.qsize()} ссылок')
            url = self.queue_old_auto.get()
            print('WORKIN ON: ', url)
            with requests.Session() as session:
                responce = session.get(url, headers=self.HEADERS,
                                       timeout=self.TIMEOUT)


                #url_new_car = 'https://auto.ria.com/uk/newauto/auto-hyundai-tucson
                # -1893570.html'

                soup_new = BeautifulSoup(responce.text, 'lxml')

                try:
                    phone_id = soup_new.findAll('script')[6]
                    json_text = re.findall(r'"phone_id":"\d+', phone_id.string)[
                        0].replace('"phone_id":"', '')

                    print(json_text)

                    headers_new = {
                        "accept": "*/*",
                        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                        "cache-control": "no-cache",
                        "content-type": "application/json;charset=UTF-8",
                        "pragma": "no-cache",
                        "sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "Windows",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                    }

                    new_car_post_url = 'https://auto.ria.com/newauto/api/auth/dc'

                    params = {
                        "adv_id": 1891271, "phone_id": f"{json_text}", "platform": "desktop"
                    }

                    response = requests.get(new_car_post_url,
                                            data=params, headers=headers_new)
                    print('New car number', response.status_code)
                    print(response.text)
                except Exception:
                    print('Such does not exist')

    def main(self):
        url = 'https://auto.ria.com/uk/car/' + self.model
        self.parsing_url_for_pages(url)
        handle_page = 10
        for page in range(1, handle_page):#int(self.pages)+1):
            print(f'Парсим страницу {page} из {self.pages} страниц')
            url_from_page = 'https://auto.ria.com/uk/car/' + self.model + \
                            f'/?page={page}'
            self.parsing_for_links(url_from_page)
            time.sleep(1)
            self.get_number_old_car()
            self.write_json()


if __name__ == '__main__':
    car = AutoParser('Mercedes-Benz')
    # car.main()
    car.json_to_excel(f'C:/Users/User/PycharmProjects/Parsers/venv'
                        f'/autoriaPars{(car.model)}.json')

