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


message = 'S O S'

symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
morse_codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
               '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-',
               '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--',
               '--..', '.----', '..---', '...--', '....-', '.....', '-....',
               '--...', '---..', '----.', '-----']

message = message.split(' ')
my_dict = dict(zip(symbols, morse_codes))
print(my_dict)

decod = []
for i in message:
    for k, v in my_dict.items():
        if i == k:
            decod.append(v)
print(' '.join(decod))


n = 9587456281
ld = []
ld = list(str(n))
if len(str(n)) == 10 and (ld[0] == '7' or ld[0] == '8' or ld[0] == '9'):
    print('YES', len(ld))
else:
    print('NO')


from collections import defaultdict

# areas = defaultdict(lambda: defaultdict(list))
#
# areas['area1']['district1'].append('addr1')

kodword = '*!*!*?'
thirddict = {}
let = {'a': 3, 'n': 2, 'c': 1} # enter dict
revdict = {v:k for k, v in let.items()}
print('revdict', revdict)
for sign in kodword:
    thirddict[sign] = thirddict.get(sign, 0) + 1
print('thirddict', thirddict)
digstr = ''
for let in kodword:
    for k_i, v_i in thirddict.items():
        if k_i == let:
            digstr += str(v_i)
print(digstr)
outstr = ''
for dig in digstr:
    for k, v in revdict.items():
        if dig == str(k):
            outstr += v
print(outstr)

# Используя генератор создать словарь, в которм ключ - позиция чиса в списке
# начиная с 0, а значение его квадрат
numb = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35]
for i, n in enumerate(numb):
    res = {i: n**2 for i, n in enumerate(numb)}
print(res)


s = '1:men 2:kind 90:number'.split(' ')
resultdict = {}
for el in s:
    el = el.split(':')
    resultdict[int(el[0])] = resultdict.setdefault(int(el[0]), el[1])
print(resultdict)

# используя генератор словарей

resgendict = {int(k): v for k, v in [l.split(':') for l in s]}
print(resgendict)

# создать словарь, где ключом будет элемент списка, а значением список всех
# его делителей включая само число
numb = [34, 10, 4, 6, 23]
print({x: [y for y in range(1, x+1) if x % y == 0] for x in
       numb})

# создать словарь, где ключом будет элемент списка, а значением список всех
# его букв в ASCII (ord())
numbtext = ['yes', 'hello', 'buy', 'stepic']
print({x: [ord(x[y]) for y in range(len(x))] for x in numbtext})
# или
print({word: [ord(letter) for letter in word] for word in numbtext})

# задача на генератор словарей
# создать словарь, содержащий инф-ю о росте > 180 и весе < 70
students = {
    'Timur': (170, 75), 'Ruslan': (180, 105), 'Sultan': (192, 68),
    'Roman': (175, 70), 'Milen': (160, 50), 'Ivan': (170, 55),
    'Tom': (190, 90), 'Anna': (163, 52), 'Alis': (168, 59)
}

results = {k: v for k, v in students.items() if (v[0] < 180 and v[1] < 70)}
print(results)

st_ids = ['s001', 's002', 's003']
st_names = ['Camila', 'Anna', 'Ivan']
st_grades = [86, 98, 89]
answdict = [{x: {y: z}} for x, y, z in zip(st_ids, st_names, st_grades)]
print(answdict)
# или
outdict = [{st_ids[i]: {st_names[i]: st_grades[i]}} for i in range(len(
    st_ids))]
print(outdict)
# или
lists = zip(st_ids, st_names, st_grades)
listoutdict = [{k[0]: {k[1]: k[2]}} for k in lists]
print(listoutdict)
