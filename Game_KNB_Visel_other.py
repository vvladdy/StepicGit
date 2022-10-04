import random


def game(timur, ruslan):
    my_dict_win = {
        'камень': 'ножницы',
        'бумага': 'камень',
        'ножницы': 'бумага',
        'ящерица': 'бумага',
        'Спок': 'камень'
    }
    my_dict_lost = {
        'камень': 'бумага',
        'бумага': 'ножницы',
        'ножницы': 'камень',
        'Спок': 'ножницы',
    }
    my_dict_Spok = {
        'камень': 'ящерица',
        'ножницы': 'ящерица',
        'бумага': 'Спок',
        'ящерица': 'Спок'
    }
    if timur == ruslan:
        return 'Ничья'
    for k, v in my_dict_win.items():
        if timur == k and ruslan == v:
            return f' Тимур'

    for k, v in my_dict_lost.items():
        if timur == k and ruslan == v:
            return f' Выиграл Руслан'

    for k, v in my_dict_Spok.items():
        if timur == k and ruslan == v:
            return '3 Тимур'
        else:
            return '3 Руслан'

#
# print(game(input('Введи Тимур Камень, ножницы, бумага, ящерица, Спок : '),
#            input('Введи Руслан Камень, ножницы, бумага, ящерица, Спок: ')))


def anton(string: str):
    exam = 'anton'
    newstr = ''
    for i in string:
        if i in exam:
            newstr += i
    if newstr == exam:
        return True
    else:
        return False


print(anton('222anton456'))
print(anton('richarn'))
print((anton('a11n2ton')))


def antonlist(string: list):
    exam = 'anton'
    exam1 = 'anot'
    newstr = ''
    for i in string:
        if i in exam:
            newstr += i
    print(sorted(set(''.join(newstr))))
    if newstr == exam:
        return True
    else:
        return False

antonl = ['222anton45kkkkkkkkkkk006', 'richarn', 'a11n2ton', 'aoooontooo']
new_antonlist = list(map(antonlist, antonl))
print(new_antonlist)
for i in range(len(new_antonlist)):
    if new_antonlist[i] == True:
        print(i+1, end = ' ')

print('\n')

import re

def numbers(message):
    if message == '':
        return True
    elif re.match('^\d.+[a-zA-Z]$', message) == None:
        return False
    res = re.findall('(\d+)([a-zA-Z]+)', message)
    numbar = 0
    numb = 0
    for i in res:
        for k in range(len(i)):
            if k == 0:
                numbar = int(i[k])
            elif k == 1:
                numb = len(i[k])
                if numbar == numb:
                    pass
                else:
                    return False
            else:
                return False
    return True

print(numbers('5hello3hey4hell'))


def remove_rotten(bag_of_fruits: list):
    pass
    new = []
    rotten = 'rotten'
    for i in bag_of_fruits:
        new.append(i.lower().replace(rotten, ''))
    return new

print(remove_rotten(["rottenApple","rottenBanana","rottenApple",
                    "rottenPineapple","Kiwi", 'juce', 'rottenAlb']))


stroka = 'Чехов'
print([i for i in stroka])

strings = 'олдокс Хаскли родился в 1981 году'
print(strings[0].upper()+strings[1:])

string2 = 'Ребенок - это зеркало поступков родителей'
print(string2.replace('о', '0'))

string3 = 'Хемингуэй'
print('Индекс буквы (м) :', string3.index('м'))

print('tree'*4)


import random

def hangman(world):
    n = 0
    stages = ['___________',
              '|    |    |',
              '|    |    |',
              '|    O    |',
              '|  / | \  |',
              '|  _/ \_  |',
              '-----------'
            ]
    print('Угадайте слово из {} букв'.format(len(world)))
    count = len(stages)
    flag = False
    newhung = ''
    newworld = world
    win_word = []
    count_repeat_let = 0
    for i in range(len(world)):
        win_word += "*"
    print(win_word)
    while count != 0:
        hello = input(f'Назовите букву:')
        if hello in world:
            indlet = world.index(hello)
            print(f'Буква {hello} есть')
            win_word[indlet] = hello
            print(win_word)
            world = world[:indlet] + '%' + world[indlet + 1:]
            if ''.join(win_word) == newworld:
                flag = True
                break
        else:
            print(f'Буквы {hello} нет')
            newhung += str(stages[n])+'\n'
            print(newhung, sep='\n')
            n += 1
            count -= 1

    if flag:
        return ('\nВы угадали слово "{}"'.format(newworld.upper()))
    else:
        return ('\nВы не угадали слово "{}"'.format(newworld.upper()))


# words = ['кот', 'бабуин', 'акула', 'свинка', 'кролико']
# print(hangman(random.choice(words)))

#
# words = ["аист", "акула", "бабуин", "баран", "барсук", "бобр", "бык", "варан"]#,
#          # "верблюд", "волк", "вомбат", "воробей", "ворон", "выдра",
#          # "голубь", "гусь", "додо", "дятел", "енот", "ехидна", "еж", "жаба",
#          # "жираф", "журавль", "заяц", "зебра", "землеройка", "зяблик",
#          # "игуана", "кабан", "казуар", "кайман", "какаду", "кальмар", "камбала",
#          # "канарейка", "каракатица", "карп", "кенгуру",
#          # "киви", "кит", "лама", "ламантин", "ласка", "ласточка", "лебедь",
#          # "лев", "лемур", "ленивец", "леопард", "лиса", "лягушка",
#          # "мотылек", "муравьед", "муравей", "мангуст", "медведь", "морж", "муха",
#          # "мышь", "медуза", "нарвал", "носорог", "орел", "омар", "олень",
#          # "овцебык",
#          # "осьминог", "орел", "осел", "оса", "овца", "опоссум", "обезьяна",
#          # "паук", "пескарь", "пингвин", "пиранья", "попугай",
#          # "пчела", "рысь", "рыба", "росомаха", "страус", "сурок", "стрекоза",
#          # "сорока", "сова", "снегирь", "сокол", "собака", "слон",
#          # "слон", "скорпион", "скворец", "скат", "сельдь", "свинья", "сурикат",
#          # "скунс", "слизень", "светлячок", "тюлень", "тукан", "тигр",
#          # "трясогуска", "термит", "тетерев", "тунец", "тритон", "тарантул",
#          # "таракан", "тля", "утконос", "уж", "устрица", "улитка", "угорь",
#          # "фазан", "фламинго",
#          # "форель", "хорек", "хомяк", "хамелеон", "цапля", "цесарка", "цикада",
#          # "черепаха", "червь", "чайка", "шимпанзе", "шиншилла",
#          # "щука", "эму", "ящерица", "ястреб", "як", "ягуар"]
# word = words[random.randrange(5)]
# len_word = len(word)
# health = 10
# test = False
# used_letters = ""
# win_word = []
# # заполнение массива для слова в игре
# for i in range(len(word)):
#     win_word += "_"
#
# while len_word != 0 and health != 0:
#     test = False
#     # ввод буквы и проверка на повтор
#     while True:
#         letter = input("\nвведите букву ")
#         if letter in used_letters or len(letter) > 1:
#             print("\nНе больше одного символа, попробуйте снова!")
#         else:
#             used_letters += letter
#             break
#     count = 0
#     for i in word:
#         if letter in i:
#             len_word -= 1
#             test = True
#             win_word[count] = letter
#         count += 1
#
#     if not test:
#         health -= 1
#         print("Неверно")
#     else:
#         print("Верно")
#         print(win_word)
#
#     print("Ваше здоровье = ", health)
#
# if (len_word == 0):
#     print("\nПОБЕДИТЕЛЬ!!! Слово было", word.upper())
# else:
#     print("\nВЫ ПРОИГРАЛИ! ПОПРОБУЙТЕ СНОВА!")

print('\nClass OOP')
class SquareFigure:

    def __init__(self, weigth: int, lenght: int):
        self.weight = weigth
        self.lenght = lenght

    def square_quadrat(self):
        if self.weight == self.lenght:
            square = self.weight**2
            return square
        else:
            raise ValueError('Different weigth and length')

    def square_rectangle(self):
        square = self.weight*self.lenght
        return square

    def square_triangle(self):
        square = 0.5 * self.weight * self.lenght
        return square

    def perimetr_trapec(self, sideweight, sidelenght):
        perimetr = self.weight + self.lenght + sideweight + sidelenght
        return perimetr


square = SquareFigure(4, 6)
print(f'Площадь прямоугольнка со сторонами {square.weight} x '
      f'{square.lenght}:', square.square_rectangle())
square.weight = 6
print(f'Площадь квадрата со сторонами {square.weight} x {square.lenght}: '
      f'', square.square_quadrat())
print(f'Площадь квадрата со сторонами {square.weight} x {square.lenght}: '
      f'', square.square_triangle())

print(f'Периметр странной трапеции: ',square.perimetr_trapec(5, 7))


class Apple:

    def __init__(self, size, color, sort, condition):
        self.size = size
        self.color = color
        self.sort = sort
        self.condition = condition

    def size_apple(self):
        self.size = 'small'
        return self.size

golden = Apple(2, 'green', 1, 'Apple.GOOD')
print(golden)

print('\n Тема Композиция: \n' )

class Dog():

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():

    def __init__(self, name):
        self.name = name

mike = Person('Mickle')
stan = Dog('Jack', 'booldog', mike)
print('Хозяин собаки: ', stan.owner.name)


print('\nЗакрепление теории')
class Rectangle:

    all_ask = []

    def __init__(self, width: int, leng: int):
        self.width = width
        self.leng = leng
        self.all_ask.append((self.width, self.leng))

    def calculate_perimeter(self):
        perimetr = (self.width + self.leng)*2
        return perimetr

    @staticmethod
    def shape():
        return 'Прямоугольник'


class Square:
    def __init__(self, width: int):
        self.width = width

    def calculate_perimeter(self):
        perimetr = self.width * 4
        return perimetr

    def change_size(self, change):
        self.width = self.width + change

    @staticmethod
    def shape():
        return 'Квадрат'

class Shape(Square, Rectangle):

    def what_am_i(self):
        return f'Я - фигура'

if __name__ == '__main__':
    per_rect = Rectangle(5, 6)
    per_rect1 = Rectangle(3, 9)
    per_rect2 = Rectangle(5, 9)
    per_rect3 = Rectangle(99, 2)
    print('Все запросы на расчет периметров: ', Rectangle.all_ask)

    print('Периметр прямоугольника: ', per_rect.calculate_perimeter())

    per_sq = Square(5)
    print('Периметр квадрата: ', per_sq.calculate_perimeter())
    per_sq.change_size(-1)
    print('Периметр квадрата с изменениями: ', per_sq.calculate_perimeter())
    a = Shape(1)
    print(a.what_am_i())

print('\nNew Example')

class ShapeFig:

    def __init__(self, w, l):
        self.w = w
        self.l = l

    def who_am_i(self, j):
        return f"I am figure {j}"

class Rect(ShapeFig):

    def perimetr_rect(self):
        per = (self.w+self.l)*2
        return per

class Squ(ShapeFig):

    def perimetr_rect(self):
        if self.w != self.l:
            raise ValueError('Стороны должны быть равны')
        else:
            per = ((self.w+self.l)*2)
        return per

obj = Rect(4, 5)
print(obj.who_am_i('Rectangle'))
print('My perimetr is: ', obj.perimetr_rect())

obj1 = Squ(4, 4)
print(obj1.who_am_i('Square'))
print('My perimetr is: ', obj1.perimetr_rect())


class Horse:

    def __init__(self, name, color, rider):
        self.name = name
        self.rider = rider
        self.color = color

    def info(self):
        return f'{self.name} {self.color} {self.rider}'

class Rider:

    def __init__(self, name):
        self.name = name

    # данный магический метод выводит имя  Nikolas вместо
    # <__main__.Rider object at 0x00000233010A2DD0>. То есть мы переназначили
    # то, что будет на выходе
    def __repr__(self):
        return self.name

nike = Rider('Nikolas')
horse = Horse('Best', 'Black', nike)

print(horse.rider.name)
print(horse.name)
print(horse.rider)



