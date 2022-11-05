import re

print(re.match(r'[^0-9]', 'kkd'))

# Find all use strict, and use strict;
text  ='use strict< use strict= use strict> use strict? use strict@ use ' \
       'strictA use strictB use strictC use strict; с065мк8 з724ок14 м976мм76 ' \
       'л147ом31 г944ть6 с206рн345 о034ам908 е678рв652 5 64 370 0645  18792 ' \
       '3767484986023 028736415208410 621053597912443 Прикоп 2-3см 16.874124' \
       ' -24.984161'

print(re.findall(r'use strict\;{0,1}', text))

# Validate Russian car-numbers
print(re.findall(r'[авекмнорстух][0-9]{3}[авекмнорстух]{2}[0-9]{2,3}', text))

# Chek link
link = 'https://cdn1.autoria.kjl https://cdn7.auto.jpg'
print('LINK', re.findall(r'https[\W]{3}cdn[0-9].[a-z]{2,}.jpg', link))

# Validate IMEI (always 15 digits)
print('IMEI', re.findall(r'\b[\d]{15}\b', text)) #\b define begin-end expression

# find all coordinate includ negative
print('COORDINATE', re.findall(r'-{0,1}\b[\d]{1,3}\.[\d]{2,}\b', text))
print('COORDINATE', re.findall(r'-?\d+\.\d+', text))
# -? search or 0 or 1 repetition equal {0,1}, \. - search '.'


# find ONLY protocol http, or https
url = 'https://httpsssssssssssss.com/ggtps/hhttps/'
print('PROTOCOL', re.findall(r'\bhttp[s]?\b', url)) # \b \b ограничения слова

# Найдите все повторяющиеся буквы в тексте . Исполльзуем группы
textn = 'Сломанная лиственница и гостиная, украшенная стеклянными вазами. ' \
        'AABBCCDDEEFFGGHHIIJJKKLLMM'

regex = re.findall(r'([a-zа-яА-ЯA-ZёЁ]{1})\1', textn)
print('REPETITIVE LETTERs', regex)

# Найдите все повторяющиеся последовательности из двух цифр, которые идут друг за другом.
textr = '6996966969534535345377777753453'

print('REPET 2 Digits', re.findall(r'([\d]{2})\1', textr))

# find all odd numbers
# используем скобочные выражения
print('ODD DIGITS', re.findall(r'\b(?:[0-9]{0,}[02468])\b', text))
print('ODD DIGITS', re.findall(r'(?<!\d)-?\d*[02468](?!\d)', text))

textq = '[^START]TextYolka{(END.)}'
# Получить последовательность из любых символов от [^START] до {(END.)}
# Используем скобочные выражение
print('TEXT INSIDE', re.findall(r'(?<=\[\^START\]).+(?=\{\(END\.\)\})', textq))

# Найдите все последовательности x с чётной длиной
seq = 'x xx xxx xxxx xxxxx xxxxxx xxxxxxx xxxxxxxx xxxxxxxxx xxxxxxxxxx ' \
      '+1-926-123-12-12, 8-926-123-12-12'
print('TEXT XXXX', re.findall(r'\b(?:[x]{2}){0,}\b', seq))

# Номера телефонов, кот начин с +1 или 8 и имею паттерн
print('NUMB', re.findall(r'(?:\+1|8)(?:-\d{2,3}){4}', seq))


names = 'carl menson Самарский (государственный) экономический университет'
print(''.join(re.findall(r'\b\w', names)).upper())

print(names.title())

# валидные номера телефонов: Номер может начинаться с 8, 7, +7.
# Разделителями могут быть: пробелы, тире, круглые скобки.
# В номере должно быть 11 цифр
# Так как re.fullmatch, то ответ будет True/False
numb = '7(777)81797104'
print(re.fullmatch(r'^(?:[87]|\+7)(?:[ \-()]*\d){10}', numb) is not None)

# найти в HTML-тексте все значения со знаком ₽
n = '<div class="col-md-2 col-xs-9 _dollar">USD</div><div class="col-md-2 ' \
    'col-xs-9 _right mono-num">62,4031 ₽! Привет, как твои дела? Привет, ' \
    'нормально,'
regex = re.finditer(r'-?\d+.?\d+?.?₽', n)
for i in regex:
    print('HTML_Parser_text',i[0])

# Разделить текст на предложения по знакам препинания  .?!
print(re.split(r'[\.\!\?]', n))

# Вывести названия категорий

stroka = 'Категория: Телефоны\nSupreme Burner\nMotorola ' \
         'Razr\nКатегория: Смарт часы и браслеты\nApple Watch 6\nGarmin ' \
         'Venu\nXiaomi Mi Smart Band 6\nКатегория: Игры\nSpore'

for i in re.split(r'[А-я]+:[А-я\s]+|\\n', stroka):
    print('Товары: ', i)

# Выведите все ссылки, которые находятся в тегах a:
teg = '<a target="_blank" href="https://stepik.org/">Hyperlink</a>' \
      '<a class="hhuy" href="./img/icon.jpg"'
match = re.findall(r"<a.+?href=\"(.+?)\"", teg)
print(*match, sep='\n')