from pprint import pprint

import requests
from bs4 import BeautifulSoup
import html
import lxml.html
import json

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36'
}
TIMEOUT = 10
INFO = []


def parse(url, p):
    print(f'Работаем со страницей...{p} - {url}')
    with requests.Session() as session:
        responce = session.get(url, headers=HEADERS, timeout=TIMEOUT)
        assert responce.status_code == 200, 'BAD RESPONCE'
        if responce.status_code:
            print('BEGIN...', responce.status_code)

        soup = BeautifulSoup(responce.content, 'lxml')
        data_id = soup.find_all('div', class_="l-GwW js-productad")[0].get(
            'data-company-id'
        )
        print(data_id)

        for prod in range(0, 28):
            print(f'Позиция........... {prod}')
            name = soup.select('.MafxA script')[prod]
            # print(name)

            data = lxml.html.fromstring(str(name))
            try:
                json_text = (json.loads(
                    html.unescape(
                        data.xpath('//script[@type="application/ld+json"]/text()')[0]
                    )
                ))
                # pprint(json_text)

                print(json_text['name'])
                print(json_text['offers']['price'], json_text['offers'][
                    'priceCurrency'])
                print(json_text['offers']['seller']['name'])
                print(json_text['image'])
                print(str(json_text['offers']['availability']).split('/')[-1])
                print(json_text['url'])
                print(json_text['offers']['seller']['name'])

                INFO.append({
                'name': json_text['name'],
                'price': int(json_text['offers']['price']),
                'currency': json_text['offers']['priceCurrency'],
                'seller': json_text['offers']['seller']['name'],
                'image': json_text['image'],
                'availability': str(json_text['offers']['availability']
                                    ).split('/')[-1],
                'url': json_text['url']
                })

            except Exception as error:
                print('Not Exist')

        with open('prom_muzg_odezgda.json', 'w', encoding='utf-8') as file:
            json.dump(INFO, file, indent=4, ensure_ascii=False)

def main():
    # 'https://prom.ua/ua/Pulsometry'
    # 'https://prom.ua/ua/Bronezhilety'
    pages = 15
    for page in range(1, pages+1):
        url = f'https://prom.ua/ua/Muzhskaya-odezhda;{page}'
        parse(url, page)

if __name__ == '__main__':
    main()