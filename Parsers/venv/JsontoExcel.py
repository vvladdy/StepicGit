import openpyxl
import json
from pprint import pprint

# загрузка и чтение json-файла
with open('toExcel.json') as file:
    data = json.load(file)
    # print(type(data))
    book = openpyxl.Workbook()

    # по факту заполняем первую строку
    sheet = book.active
    sheet['A1'] = 'ID'.upper()
    sheet['B1'] = 'Title'.upper()
    sheet['C1'] = 'Year'.upper()
    sheet['D1'] = 'Genres'.upper()
    sheet['E1'] = 'Director'.upper()
    sheet['F1'] = 'Actors'.upper()
    sheet['G1'] = 'posterUrl'.upper()

    row = 2

    for movie in data["movies"]:
        print(movie)
        sheet[row][0].value = movie["id"]
        sheet[row][1].value = movie["title"]
        sheet[row][2].value = movie["year"]
        sheet[row][3].value = ' '.join(movie["genres"])
        sheet[row][4].value = movie["director"]
        sheet[row][5].value = movie["actors"]
        sheet[row][6].value = movie["posterUrl"]

        row += 1
    book.save('mybook.xlsx')
    book.close()

#############################################################################
import openpyxl
import json

with open('freelanse.json', 'rb') as file:
    datas = json.load(file)
    # print(datas)

    for data in datas:
        # print(data)
        title = data['title']
        task = data['task']
        link = data['link']
        # print(title, task, link)

        xlsbook = openpyxl.Workbook()

        sheet = xlsbook.active
        sheet['A1'] = 'TITLE'.upper()
        sheet['B1'] = 'TASK'.upper()
        sheet['C1'] = 'LINK'.upper()

    row = 2
    for info in datas:
        print(info)
        sheet[row][0].value = info['title']
        sheet[row][1].value = info['link']
        sheet[row][2].value = info['task']
        row += 1
    xlsbook.save('frelanse.xlsx')
    xlsbook.close()

#############################################################################
import openpyxl
import json

with open('C:/Users/User/PycharmProjects/Parsers/venv/Olx/olx_n.json',
          'rb') as file:
    datas = json.load(file)
    print(type(datas))

    # for data in datas:
    #     name = data["название"]
    #     price = data["стоимость"]
    #     public_date = data["дата публикации"]
    #     city = data["город"]
    #     link = data["ссылка на страницу"]

    filecontent = openpyxl.Workbook()
    sheet = filecontent.active

    sheet['A1'] = 'название'.upper()
    sheet['B1'] = 'стоимость'.upper()
    sheet['C1'] = 'дата публикации'.upper()
    sheet['D1'] = 'город'.upper()
    sheet['E1'] = 'ссылка на страницу'.upper()

    row = 2
    for info in datas:
        # print(info['название'])
        sheet[row][0].value = info['название']
        sheet[row][1].value = info["стоимость"]
        sheet[row][2].value = info["дата публикации"]
        sheet[row][3].value = info["город"]
        sheet[row][4].value = info['ссылка на страницу']
        row += 1

    filecontent.save('C:/Users/User/PycharmProjects/Parsers/venv/Olx/Busines OLX.xlsx')
    filecontent.close()


# import openpyxl
#
# book = openpyxl.Workbook()
# sheet = book.active
#
# # запись данных по клеточкам
# sheet['a2'] = 100
# sheet['b3'] = 'hello'
# # запись данных по клеточкам
# sheet[1][0].value = 'world'
# # запись данных по колонкам
# sheet.cell(row=1, column=1).value = 'hello world'
#
# book.save('mybook.xlsx')
# book.close()
