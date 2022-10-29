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


            soup = BeautifulSoup(responce.content, 'html.parser')
            links1 = soup.select('.head-ticket div a')

            public_dates = soup.select('.footer_ticket span span')

            for link in range(len(links1)):
                print(links1[link].get('href').split('/'))
                for el in links[link].get('href').split('/'):
                    if el == 'newauto':
                        print(links[link].get('href'))
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
        print('NEW AUTO', self.queue_new_auto.qsize())
        while self.queue_new_auto.qsize() > 0:
            print(f'Нужно обработать {self.queue_new_auto.qsize()} ссылок')
            date = self.queue_new_auto.get()
            self.url = date[0]
            print(self.url)
            self.public_date = date[1]
            print('WORKIN ON: ', self.url, self.public_date,
                  self.queue_new_auto.qsize())
            with requests.Session() as session:
                responce = session.get(self.url, headers=self.HEADERS,
                                       timeout=self.TIMEOUT)

                soup_new = BeautifulSoup(responce.text, 'lxml')

                try:
                    phone_id = soup_new.findAll('script')[6]
                    json_text = re.findall(r'"phone_id":"\d+', phone_id.string)[
                        0].replace('"phone_id":"', '')

                    print(json_text)

                    headers_new = {

                        "content-type": "application/json",
                        "cookie": "__utmz=79960839.1663188796.1.1.utmcsr=(direct)|utmccn=("
                                  "direct)|utmcmd=(none); _gcl_au=1.1.680757332.1663188796; "
                                  "_fbp=fb.1.1663188797468.674172798; ui=8a0e3d79413f200b; "
                                  "__gads=ID=7f1a6e9bfd29383b:T=1663188798:S"
                                  "=ALNI_MbOG0v4pK2iexTt0sqtDy-t-de1VQ; "
                                  "_gid=GA1.2.381724096.1666815392; "
                                  "_ga=GA1.3.1725317400.1663188796; ipp=20; "
                                  "__utmc=79960839; showNewFeatures=7; extendedSearch=1; "
                                  "showNewFinalPage=1; showNewNextAdvertisement=-10; "
                                  "PHPLOGINSESSID=ns116fjf2scoms9tt11j0ia4b5; "
                                  "project_id=18; "
                                  "project_base_url=https%3A%2F%2Fchat.ria.com%2Fiframe-ria"
                                  "-login; slonik_utm_campaign=; slonik_utm_medium=; "
                                  "slonik_utm_source=; test_new_features=664; "
                                  "advanced_search_test=42; "
                                  "PHPSESSID=eyJ3ZWJTZXNzaW9uQXZhaWxhYmxlIjp0cnVlLCJ3ZWJQZX"
                                  "Jzb25JZCI6MCwid2ViQ2xpZW50SWQiOjIzMTYxODkwNDksIndlYkNsaWVu"
                                  "dENvZGUiOjEwOTQ2NTYwMTEsIndlYkNsaWVudENvb2tpZSI6IjhhMGUzZD"
                                  "c5NDEzZjIwMGIiLCJfZXhwaXJlIjoxNjY3MDMzMjk3NzY3LCJfbWF4QWdl"
                                  "Ijo4NjQwMDAwMH0=; informerIndex=1; "
                                  "__utma=1.1725317400.1663188796.1666947011.1666947011.1; "
                                  "__utmc=1; "
                                  "__utmz=1.1666947011.1.1.utmcsr=auto.ria.com|utmccn=("
                                  "referral)|utmcmd=referral|utmcct=/uk/car/mercedes-benz/; "
                                  "_ga_V4H4L9D6JB=GS1.1.1666947011.1.0.1666947011.0.0.0; "
                                  "_ga_QLXD2N77X6=GS1.1.1666947011.1.0.1666947011.60.0.0; "
                                  "_clck=mrp956|1|f63|0; "
                                  "__utma=79960839.1725317400.1663188796.1666946896"
                                  ".1666985497.13; PHPSESSID=N2xce2eKu3_0VOH1dwEkz6efeZsZxco8;"
                                  " __gpi=UID=00000b3cf3c83e03:T=1663188798:RT=1666985498:S"
                                  "=ALNI_Mbv7zT5KMk9LauSn_LHjgQ_GN_jJg; "
                                  "sid=w7AhWfzzcgLV5mzhZXWwJA6spiCJCGqe"
                                  "+00vr9jiAxABgQpfqy5D4FXcsg76daNMAZcqMzWawjmuQacRQft"
                                  "/+Wbf5JXyq5DQ5V85znSLs2r4xqAESCDhBbA+dpLi2i7X; "
                                  "AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1725317400.1663188796;"
                                  " _dc_gtm_UA-110070444-1=1; _gat_newauto_commercial=1;"
                                  " _gid=GA1.3.381724096.1666815392; _gat=1; "
                                  "_clsk=15wfs9|1666993203034|2|1|e.clarity.ms/collect; "
                                  "_ga_QE9NBY8W7X=GS1.1.1666993195.3.1.1666993207.0.0.0"
                    }

                    new_car_post_url = 'https://auto.ria.com/newauto/api/auth/dc'

                    params = {
                        "adv_id": 1891271, "phone_id": f"{json_text}", "platform": "desktop"
                    }

                    response = requests.post(new_car_post_url,
                                            params=params, headers=headers_new)
                    print('New car number', response.status_code)
                    self.phone_number_new_car = response.json()[
                        'phone_formatted']
                    print(self.phone_number_new_car)
                except Exception:
                    print('Such does not exist')

    def main(self):
        url = 'https://auto.ria.com/uk/car/' + self.model
        self.parsing_url_for_pages(url)
        handle_page = 2
        for page in range(1, handle_page):#int(self.pages)+1):
            print(f'Парсим страницу {page} из {self.pages} страниц')
            url_from_page = 'https://auto.ria.com/uk/car/' + self.model + \
                            f'/?page={page}'
            self.parsing_for_links(url_from_page)
            time.sleep(1)
            self.get_number_old_car()
            self.get_number_new_car()
            self.write_json()


if __name__ == '__main__':
    car = AutoParser('citroen')
    car.main()
    car.json_to_excel(f'C:/Users/User/PycharmProjects/Parsers/venv'
                        f'/autoriaPars{(car.model)}.json')

