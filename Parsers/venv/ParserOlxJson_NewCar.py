import re
from pprint import pprint
import html
import lxml.html

import requests
from bs4 import BeautifulSoup
import json

TIMEOUT = 10

# url = 'https://auto.ria.com/uk/auto_bmw_x5_33470230.html'
url = 'https://auto.ria.com/uk/auto_volkswagen_passat_b8_33472105.html'


with requests.Session() as session:
    responce = requests.get(url, timeout=TIMEOUT)

    content = responce.text
    soup = BeautifulSoup(content, 'lxml')
    idexc = url.split('_')[-1][:8]

    title = soup.select('.head')[0].text.rstrip()

    model = soup.select('.head')[0].text.rstrip().split(
        ' ')[0]
    marka = soup.select('.head')[0].text.rstrip().split(
                        ' ')[1]
    try:
        price = int(''.join(soup.select('#showLeftBarView section div strong')[
            0].text.strip('').split(' ')[0:-1]))
    except Exception:
        price = ''.join(soup.select('#showLeftBarView section div strong')[
                    0].text.strip('').split(' ')[0:-1])
    currency = soup.select('#showLeftBarView section div strong')[
        0].text.strip('').split(' ')[-1]

    sale_name = ' '.join(soup.select('#showLeftBarView section div')[
                    3].text.strip(' ').split(' ')[0:2])
    mile = soup.select('#showLeftBarView section div')[2].text.strip(' '
                                    '').split(' ')[0] + ' тис.км'

    hesh = soup.findAll('script')[38].get('data-hash')

    pictures = soup.select('#photosBlock div div script')[0]
    print(pictures)
    data = lxml.html.fromstring(str(pictures))
    json_text=(json.loads(
        html.unescape(
            data.xpath('//script[@type="application/ld+json"]/text()')[0]
    )))
    # pprint(json_text['image'])
    list_url = []
    for el in json_text['image']:
        if el['contentUrl'][-1] == 'g' and el['contentUrl'][8:12] != 'auto':
            list_url.append(el['contentUrl'][:-5] + 'f' + '.jpg')
    print(list_url)

    print('Link: ', url)
    print(title)
    print('Модель', model)
    print('марка', marka)
    print(price, currency)
    print(mile)
    print(sale_name)
    # print(hesh)

    url = f'https://auto.ria.com/users/phones/{idexc}?hash=' \
           f'{hesh}&expires=2592000'

    jsonhesh = requests.get(url)
    print(jsonhesh.json()['formattedPhoneNumber'])



def post_new_car():

    headers_new = {

        "content-type": "application/json",
        "cookie":  "__utmz=79960839.1663188796.1.1.utmcsr=(direct)|utmccn=("
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
        "adv_id":1891311,"phone_id":"680861298","platform":"desktop"
    }

    response = requests.post(new_car_post_url,
                            params=params, headers=headers_new)
    print('New car number', response.status_code)
    print(response.json())
    print(response.json()['phone_formatted'])

post_new_car()




