from pprint import pprint
import sqlite3
from sqlite3 import Error
import requests
from bs4 import BeautifulSoup
from transliterate import translit


def categories_pars(url):
    cat = []
    responce = requests.get(url)
    if responce.status_code == 200:
        soup = BeautifulSoup(responce.content, 'html.parser')

        categories = soup.select('.menu-burger__main li a')

        for categ in range(len(categories)):
            categori = categories[categ].text
            link_categori = categories[categ].get('href')
            cat.append((categori, link_categori))
    return (cat)

def pars_subcategories(url):
    with requests.Session() as session:
        responce = session.get(url, timeout=10)

        all_cat = responce.json()
        # pprint(all_cat)
        womenlist = []
        for cat in all_cat:
            # pprint(cat['name']) # все категории
            if cat['name'] == 'Женщинам':
                for i in range(len(cat['childs'])):
                    name_sub_cat = cat['childs'][i]['name']
                    try:
                        sec_name_sub_cat = cat['childs'][i]['seo']
                    except Exception:
                        continue
                    url_sub_cat = 'https://www.wildberries.ru/' + cat['childs'][i]['url']
                    womenlist.append(( 'Женщинам', name_sub_cat, url_sub_cat,))
        return womenlist


def pars_single_cat(url):
    with requests.Session() as session:
        responce = session.get(url, timeout=10)

        all_cat = responce.json()
        # pprint(all_cat)
        cat_name = []
        for cat in all_cat:
            # pprint(cat['name'])
            if cat['name']:
        #         try:
        #             pprint(cat['childs'])
        #             for i in range(len(cat['childs'])):
        #                 print(cat['childs'][i]['name'])
        #         except Exception:
        #             print(cat['name'], ' NOT CHILDS')
                try:
                    for i in range(len(cat['childs'])):
                        name_sub_cat = cat['childs'][i]['name']
                        try:
                            sec_name_sub_cat = cat['childs'][i]['seo']
                        except Exception:
                            continue
                        url_sub_cat = 'https://www.wildberries.ru/' + cat['childs'][i]['url']
                        # print(cat['childs'][i]['name'])
                        cat_name.append((
                                        cat['name'],
                                        name_sub_cat,
                                        url_sub_cat if url_sub_cat else None,))
                        # print(name_sub_cat, url_sub_cat, sec_name_sub_cat)
                except Exception:
                    continue
        return cat_name

def pars(url):
    with requests.Session() as session:
        responce = session.get(url, timeout=10)
        assert responce.status_code == 200, 'BAD RESPONCE'
        print(responce.status_code)

        url_for_get = 'https://catalog.wb.ru/sellers/filters?appType=1&dest' \
               '=-1029256&supplier=67466'
        response = session.get(url_for_get, timeout=10)
        data_filt = response.json()['data']['filters']
        # print(data_filt)
        pprint(data_filt)
        # здесь нашли все товары по фильтрам. Ключ для фильтрации в поле key
        item = []
        for items in data_filt:
            try:
                item.append(items['items'])
                # print()
            except Exception:
                print('OK')
        for el in range(len(item)):
            for i in item[0]:
                quant = i['count']
                name = i['name']
                name_id = i['id']
                # print(name, f'{quant} шт на скаладе  ID:', name_id)

        url_for_get_price = 'https://catalog.wb.ru/sellers' \
                            '/catalog?dest=-1029256&supplier=67466'

        all_prod = session.get(url_for_get_price)
        data = all_prod.json()['data']['products']
        # pprint(data)

        for it in data:
            name = it['name']
            pricesell = it['priceU']
            pricezero = it['averagePrice']
            benefinwild = it['benefit']
            quant = it['ksale']
        #'https://basket-05{basket}.wb.ru/vol865/part86555/{if_for_foto}
            # 86555457/images/c516x688{big для большой}/1{range(
            # quant_pics)}.jpg'
            # для фото
            id_for_foto = it['id']
            quant_pics = it['pics']
            basket = it['rating']
            print(name, pricezero, pricesell, quant)


# https://basket-01.wb.ru/vol439/part43972/43972921/images/big/6.jpg

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as error:
        print('Wrong connection', error)
    return connection


def create_queries(connection, queries):
    cursor = connection.cursor()
    try:
        cursor.execute(queries)
        connection.commit()
    except Error as error:
        print('Wrong execute', error)


def main():
    url = 'https://www.wildberries.ru/seller/67466'
    # pars(url)
    url_cat = 'https://www.wildberries.ru/'
    categor = categories_pars(url_cat)

    url_sub_categor = 'https://www.wildberries.ru/webapi/menu/main-menu-ru-ru.json'
    sub_categor = pars_subcategories(url_sub_categor)

    many_info = pars_single_cat(url_sub_categor)

    print(translit(str(many_info[0]), 'ru', reversed=True))

    connection = create_connection('Wilberries.db')

    create_products_table = """
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        catlink TEXT UNIQUE
    );
    """

    # create_queries(connection, create_products_table)

    # tables_for_del = F"""
    #         DELETE FROM categories;
    # """
    # create_queries(connection, tables_for_del)

    create_womens_table = """
    CREATE TABLE IF NOT EXISTS womens_product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        catlink TEXT UNIQUE,
        categories_id INTEGER NOT NULL,
        FOREIGN KEY (categories_id) REFERENCES categories (id)
    );
    """

    # create_queries(connection, create_womens_table)

    # pprint(sub_categor)

    with connection:
        cursor = connection.cursor()
        cat_name = sub_categor[0]
        print(cat_name[0])
        idn = f"""
            SELECT id
            FROM categories
            WHERE name = '{cat_name[0]}'
        """
        cursor.execute(idn)
        idnump = cursor.fetchone()
        print(idnump[0])

        for el in sub_categor:
            fill_product_table = f"""
                INSERT INTO womens_product
                    (name, catlink, categories_id)
                VALUES
                    ('{el[1]}', '{el[2]}', '{idnump[0]}')
                """

            # cursor.execute(fill_product_table)
            # connection.commit()

    with connection:
        cursor = connection.cursor()
        for el in categor:
            create_products = f"""
            INSERT INTO
                categories(name, catlink)
            VALUES
                ('{el[0]}',
                '{el[1]}')
            """
            # cursor.execute(create_products)
            # connection.commit()
    # connection.close()

    many_info = pars_single_cat(url_sub_categor)

    with connection:
        for el in many_info:
            cursor = connection.cursor()
            cat_name = el[0]
            print(cat_name)
            idn = f"""
                SELECT id
                FROM categories
                WHERE name = '{cat_name}'
            """
            cursor.execute(idn)
            idnump = cursor.fetchone()
            print(idnump[0])
            try:
                fill_product_table = f"""
                    INSERT INTO womens_product
                        (name, catlink, categories_id)
                    VALUES
                        ('{el[1]}', '{el[2]}', '{idnump[0]}')
                    """

                cursor.execute(fill_product_table)
                connection.commit()
            except sqlite3.IntegrityError as error:
                print('Такой элемент уже есть', error)


if __name__ == '__main__':
    main()