# new_dict={0: '',
#           1: 'I',
#           2: 'II',
#           3: 'III',
#           4: 'IV',
#           5: 'V',
#           6: 'VI',
#           7: 'VII',
#           8: 'VIII',
#           9: 'IX',
#           10: 'X',
#           20: 'XX',
#           30: 'XXX',
#           40: 'XL',
#           50: 'L',
#           60: 'LX',
#           70: 'LXX',
#           80: 'LXXX',
#           90: 'XC',
#           100: 'C'}
# n = int(input('Enter arabic digit:   '))
# if 0 <= n <= 109:
#     numb1 = n//10
#     numb1_2 = n % 10
# print(new_dict.get(numb1*10)+new_dict.get(numb1_2))

# Calendar

# my_cal = {31: ['January', 'March', 'May', 'July', 'August', 'October', 'December'],
#           28: ['February'],
#           30: ['Aprile', 'June', 'September', 'November']}
# enter_quant_days = int(input('Enter quant days:  '))
# if enter_quant_days == 30:
#     print(list(my_cal.get(enter_quant_days)))
# elif enter_quant_days == 31:
#     print(my_cal.get(enter_quant_days))
# elif enter_quant_days == 28:
#     print(my_cal.get(enter_quant_days))
# else:
#     print('Enter number of days')

#  Задачи из Stepic

# Создать словарь ключами которого будут числа от 1 до 15, а значениями квадраты этих чисел
result1 = {}
for num in range(1,16):
    result1[num] = result1.get(num, num*num)
print(result1)

# Добавить в новый словарь элементы из существуюих 2 и значеня ключей просуммировать
result2 = {}
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# или
# for k in dict1:
#     result2[k] = dict1.get(k,0) + dict2.get(k,0)

# или
row = list(dict1.keys()) + list(dict2.keys())
print (row)
for i in row:
    result2[i] = dict1.get(i,0) + dict2.get(i,0)
print(result2)

# Дана строка. Найти какие буквы в ней и в каком количестве
text1 = 'dhfgdhgfhdgfhdfgdfhdfdghgdlglkfdjgkdgkdsgf'
result5 = {}
for w in text1:
    result5[w] = result5.get(w,0)+1
print(result5)

# Программа должна выводить информацию о курсе при вводе номера курса: CS101, CS102, CS103 и т.д.
# d = {
#     "CS101": "3004, Хайнс, 8:00",
#     "CS102": "4501, Альварадо, 9:00",
#     "CS103": "6755, Рич, 10:00",
#     "NT110": "1244, Берк, 11:00",
#     "CM241": "1411, Ли, 13:00",
# }
#
# cours = input(' Enter number of course:  ',)
# for key, val in d.items():
#     if key == cours:
#         print(f'{key}: {val}')


# Программа кнопочный телефон.
d = {
    '1': '.,?!:',
    '2': 'ABC'.lower(),
    '3': 'DEF'.lower(),
    '4': 'GHI'.lower(),
    '5': 'JKL'.lower(),
    '6': 'MNO'.lower(),
    '7': 'PQRS'.lower(),
    '8': 'TUV'.lower(),
    '9': 'WXYZ'.lower(),
    '0': ' '
}

buttom = ''

text = input('Enter sentence:   ').lower().replace('"', '')
#text = 'Hello, "World'#.replace('"', '')
for i in text:
    for key, val in d.items():
        for j in range(len(val)):
            if i == val[j]:
                buttom += key*(j+1)
print('Answer', buttom)

import requests
from bs4 import BeautifulSoup

def request_train():
    with requests.Session() as session:
        response = session.get(url='https://starkovden.github.io/API-doc-sites'
                                   '-list.html', timeout=10) # timeout можно без
        assert response.status_code == 200, 'Bad response'
        print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')
    inf = soup.select('ol li a')
    listlink = []
    for i in inf:
        listlink.append(i.get('href'))

    for c, j in enumerate(listlink):
        print(c, j)

# request_train()


from pprint import pprint
import datetime
import time
import schedule # модуль планировщика задач

def currency(timer):
    count = 0
    while count != 1:
        with requests.Session() as sess:
            r = sess.get(' https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
            assert r.status_code == 200, 'bad response'
            kurs = r.json()

        a = datetime.datetime.now()

        kursDict = {
            a.strftime('%d-%m-%Y %H:%M'): kurs[0:2]
        }
        pprint(kursDict)

        count += 1
        time.sleep(timer)

if __name__ == '__main__':
    ...
    # currency(2)
    # schedule.every(5).seconds.do(currency(1))
    # schedule.run_pending()


import threading

# DDos attack после нее заблокировали IP

def dos(url):
    count = 0
    while count != 2:
        print('begin...')
        with requests.Session() as session:
            session.get(url)
        count += 1
        print(count)
def st():
    url = 'https://www.example.com'
    for _ in range(2):
        threading.Thread(target=dos, args=(url, )).start()
    print('Thread quant', threading.active_count())
# st()

stroka = ['ppdlkdksldsklkl']
print(*[stroka[i][1:7] for i in range(len(stroka))])
# for i in range(len(stroka)):
#     print(stroka[i][1:7])