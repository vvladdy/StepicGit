import csv
import pickle
import re
import os
import json
from queue import Queue
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
from requests import Session
from bs4 import BeautifulSoup


queue = Queue()
INFO_ARR = []
TIMEOUT = 20
NUMBER_ARR = []


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
           'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

def controll_connection(url):
    with requests.Session() as session:
        responce = session.get(url, headers=HEADERS, timeout=TIMEOUT)
        assert responce.status_code == 200, 'Bad responce'
        print(responce.status_code)

        if responce.status_code == 200:
            try:
                os.mkdir('C:/Users/User/PycharmProjects/Parsers/venv/Olx')
            except Exception as error:
                print('Дирректория создана', error)
            with open('C:/Users/User/PycharmProjects/Parsers/venv/Olx'
                      '/olxsinglepage_network.html',
                      'w', encoding="utf-8") as pagecontent:
                pagecontent.write(responce.text)

        return responce.status_code, responce.text, responce.content


def activation_in_olx_cab(queue: Queue):
    driver_service = Service(
        executable_path='c:/Users/User/PycharmProjects/chromedriver.exe'
    )
    driver = webdriver.Chrome(
        service=driver_service
    )

    try:
        driver.get('https://www.olx.ua/')
        time.sleep(2)
        # autorisation
        autorisation = driver.find_element(By.XPATH,
                    '//*[@id="topLoginLink"]/span/strong')
        autorisation.click()
        time.sleep(2)
        login_wind = driver.find_element(By.ID, 'userEmail')
        login_wind.send_keys('username@gmail.com')
        time.sleep(1)
        pasword_window = driver.find_element(By.ID, 'userPass')
        pasword_window.send_keys('password')
        time.sleep(1)
        press_enter_button = driver.find_element(By.ID, 'se_userLogin')
        press_enter_button.click()
        # pasword_window.send_keys(Keys.ENTER)
        time.sleep(5)

        while queue.qsize() > 0:
            single_url = queue.get()
            print('WORKING ON: ', single_url)

            driver.get(single_url)

            # driver.get('https://www.olx.ua//d/uk/obyavlenie/telegram-kanal-novin-ukrana-sogodn-IDPJ5gy.html')
            time.sleep(5)

            try:
                get_number_button = driver.find_element(By.XPATH,
                '//*[@id="root"]/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div/button[1]')
                get_number_button.click()
                time.sleep(10)
                #
                phone_number = driver.find_element(By.XPATH,
                '//*[@id="root"]/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div/button[1]/span/a')
                phone_number_text = phone_number.text
                print(phone_number_text)
            except Exception as error:
                print(error)
                print(f'Еще {queue.qsize()} элементов в очереди')

    except Exception as error:
        print(error)
    finally:
        driver.close()
        driver.quit()

def pars_number(queue:Queue, page):
    driver_service = Service(
        executable_path='c:/Users/User/PycharmProjects/chromedriver.exe'
    )

    driver = webdriver.Chrome(
        service=driver_service
    )
    driver.maximize_window()

    while queue.qsize() > 0:
        single_url = queue.get()
        print('WORKING ON: ', single_url)

        try:
            driver.get(single_url)
            time.sleep(4)
            try:
                time.sleep(3)
                driver.execute_script("window.scrollTo(0, 300)")

                time.sleep(4)

                phone_button = driver.find_element(By.XPATH,
                        '//*[@id="root"]/div[1]/div[3]/div[3]/div[2]/div['
                        '1]/div[4]/div/button[1]')
                phone_button.click()
                time.sleep(3)

                phone_number = driver.find_element(By.XPATH,
                '/html/body/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div[1]/button[1]/span/a')
                phone_number_text = phone_number.text
                if phone_number_text == None:
                    phone_number_text = 'Нет номера'
                else:
                    phone_number_text = phone_number.text
                time.sleep(1)
                print(phone_number_text)

                title = driver.find_element(By.XPATH,
                '//*[@id="root"]/div[1]/div[3]/div[3]/div[1]/div[2]/div[2]/h1')
                title_text = title.text
                print(title_text)

                price = driver.find_element(By.XPATH,
                '//*[@id="root"]/div[1]/div[3]/div[3]/div[1]/div[2]/div[3]/h3')
                price_text = price.text
                print(price_text)

                NUMBER_ARR.append({
                    'наименование': title_text,
                    'стоимость': price_text,
                    'телефон': phone_number_text,
                    'ссылка': single_url
                })
                with open(
                        f'C:/Users/User/PycharmProjects/Parsers/venv/Olx/olx_num'
                        f'{price_text}.json', 'w', encoding='utf-8') as file:
                    json.dump(NUMBER_ARR, file, indent=4, ensure_ascii=False)

            except Exception as error:
                print(f'Еще {queue.qsize()} элементов в очереди')
                print(error)
        except Exception as error:
            print(error)
        finally:
            driver.close()
            driver.quit()
        pars_number(queue, page)
    with open(f'C:/Users/User/PycharmProjects/Parsers/venv/Olx/olx_num'
              f'{page}.json', 'w', encoding='utf-8') as file:
        json.dump(NUMBER_ARR, file, indent=4, ensure_ascii=False)


def parsing_urls_category(url, page):
    time.sleep(1)
    print(f'парсинг страницы {page}')
    with requests.Session() as session:
        response = session.get(url, headers=HEADERS, timeout=TIMEOUT)
        assert response.status_code == 200, 'Bad response'
        print(response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.select('.css-19ucd76 a')

        for title in range(len(titles)):
            queue.put(f"https://www.olx.ua/{titles[title].get('href')}")
        print(queue.qsize())

        prices = soup.select('.css-1q7gvpp-Text')
        pricelist = [prices[price] for price in range(len(prices))]
        print(len(pricelist))

        cities = soup.select('.css-p6wsjo-Text')
        busineses_name = soup.select('.css-1pvd0aj-Text')

        for el in range(0, len(pricelist)):
            INFO_ARR.append({
                'название': busineses_name[el].text.rstrip(),
                'стоимость': prices[el].text,
                'город': cities[el].text.split('-')[0].rstrip() if cities[el]
                                                                else None,
                'дата публикации': cities[el].text.split('-')[1].rstrip() if
                                                        cities[el] else None,
                'ссылка на страницу': "https://www.olx.ua/" +
                                    titles[el].get('href'),
            })

            # print(INFO_ARR)

        # with open(f'C:/Users/User/PycharmProjects/Parsers/venv/Olx/olx_x.json',
        #           'w', encoding="utf-8") as jsonfile:
        #     json.dump(INFO_ARR, jsonfile, indent=4, ensure_ascii=False)

        print(f'Страница {page} готова')

        return INFO_ARR


def write_csv(arr):
    fieldnames = (
        'название', 'стоимость', 'город', 'дата публикации',
        'ссылка на страницу'
    )
    with open(f'C:/Users/User/PycharmProjects/Parsers/venv/Olx/olx_x.csv',
                  'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for row in arr:
            writer.writerow(row)

def parsing_number_of_pages(status_code, text_html):
    if status_code == 200:
        soup = BeautifulSoup(text_html, 'html.parser')
        quant_page = soup.select('.css-1mi714g')[-1].text
        return int(quant_page)


def main():
    url = 'https://www.olx.ua/d/uslugi/prodazha-biznesa/'
    # url = 'https://www.olx.ua/d/uslugi/oborudovanie/'
    # page_quant = controll_connection(url)
    # page = parsing_number_of_pages(page_quant[0], page_quant[1])
    # last_page = page
    # last_page=2
    # print('Всего страниц для парсинга: ', page)
    parsing_urls_category(url, 1)
    # for i in range(2, last_page+1):
        # url = f'https://www.olx.ua/d/uslugi/prodazha-biznesa/?page={i}'
        # url = f'https://www.olx.ua/d/uslugi/oborudovanie/?page={i}'
        # parsing_urls_category(url, i)
    # write_csv(INFO_ARR)


    pars_number(queue, 1)


    # activation_in_olx_cab(queue)


    # seek_info()




    # driver_service = Service(
    #     executable_path='c:/Users/User/PycharmProjects/chromedriver.exe'
    # )
    # driver = webdriver.Chrome(
    #     service=driver_service
    # )
    #
    # try:
    #     driver.get('https://www.olx.ua/')
    #     time.sleep(2)
    #     # autorisation
    #     autorisation  = driver.find_element(By.XPATH,
    #                     '//*[@id="topLoginLink"]/span/strong')
    #     autorisation.click()
    #     time.sleep(3)
    #     login_wind = driver.find_element(By.ID, 'userEmail')
    #     login_wind.send_keys('yablon_vl@rambler.ru')
    #     time.sleep(1)
    #     pasword_window = driver.find_element(By.ID, 'userPass')
    #     pasword_window.send_keys('Vladik1981')
    #     time.sleep(1)
    #     press_enter_button = driver.find_element(By.ID, 'se_userLogin')
    #     press_enter_button.click()
    #     # pasword_window.send_keys(Keys.ENTER)
    #     time.sleep(15)

        # my_messages = driver.find_element(By.XPATH,
        #                 '//*[@id="root"]/div[1]/div[1]/div[2]/ul/li[2]/a')
        # my_messages.click()
        # time.sleep(5)

        # driver.get('https://www.olx.ua/')
        # time.sleep(10)
    #
    #     driver.get('https://www.olx.ua//d/uk/obyavlenie/telegram-kanal-novin-ukrana-sogodn-IDPJ5gy.html')
    #     time.sleep(2)
    #     get_number_button = driver.find_element(By.XPATH,
    #     '//*[@id="root"]/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div/button[1]')
    #     get_number_button.click()
    #     time.sleep(8)
    #     #
    #     phone_number = driver.find_element(By.XPATH,
    #     '//*[@id="root"]/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div/button[1]/span/a')
    #     phone_number_text = phone_number.text
    #     print(phone_number_text)
    #
    #     driver.get(
    #         'https://www.olx.ua//d/uk/obyavlenie/prodazha-bazy-otdyha-dlya-rybakov-i-ohotnikov-na-ostrove-v-delte-dunaya-IDM74BB.html')
    #     time.sleep(2)
    #     get_number_button1 = driver.find_element(By.XPATH,
    #         '//*[@id="root"]/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div/button[1]')
    #     get_number_button1.click()
    #     time.sleep(8)
    #     phone_number1 = driver.find_element(By.XPATH,
    #         '//*[@id="root"]/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div/button[1]/span/a')
    #     phone_number_text1 = phone_number1.text
    #     print(phone_number_text1)
    #
    #
    #
    #     driver.get(
    #         'https://www.olx.ua//d/uk/obyavlenie/avtomoyka-biznes-gotovyy-IDMYCD1.html')
    #     time.sleep(2)
    #     get_number_button2 = driver.find_element(By.XPATH,
    #         '//*[@id="root"]/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div/button[1]')
    #     get_number_button2.click()
    #     time.sleep(8)
    #     phone_number2 = driver.find_element(By.XPATH,
    #         '//*[@id="root"]/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/div/button[1]/span/a')
    #     phone_number_text2 = phone_number2.text
    #     print(phone_number_text2)
    #
    # except Exception as error:
    #     print(error)
    # finally:
    #     driver.close()
    #     driver.quit()


if __name__ == '__main__':
    main()


