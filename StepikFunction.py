# Отсортировать список  в соответствии с суммой минимального и
# максимального элемента кортежа

numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67),
           (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50),
           (34, 78, 65), (-5, 90, -1)]

def seeksum(sortlist):
   return max(sortlist)+min(sortlist)

print(sorted(numbers, key=seeksum))

n=2
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39),
            ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
            ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

print(sorted(athletes, key=lambda x: x[n]))

from functools import reduce

numbers = range(10)
obj = map(lambda x: x + 1, numbers)
obj = filter(lambda x: x % 2 == 1, obj)
result = reduce(lambda x, y: x + y, obj, 0)

print(result)
result = list(map(lambda x: x.split(), ['a', 'a b', 'a b c']))

print(result)

from functools import reduce

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter(lambda name: len(name)>4 if name[::-1] ==
                                                name[::1] else False, words))
reduce_result = reduce(lambda num1, num2: (num1 * num2), numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)

s = 1
for i in numbers:
    s *= i
print(s)

# Вывести максимальное число из списка
mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate',
              'accessory', 'absorb', 1384878, 'sunday', 'about', 454805,
              'saturday', 'abort', 2121919, 2552839, 977970, 1772933,
              1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate',
              1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665,
              'besides', 'bewilder', 1586517, 375290, 1503450, 2713047,
              'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent',
              'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280]

print(max(mixed_list, key=lambda x: x if isinstance(x, int) else 0))


def evaluate(coefficients, x):
    coeflist = coefficients.split()
    print(coefficients)
    ns, cs = [], []
    for c, i in enumerate(coeflist):
        ns.append(int(i))
        cs.append(x ** c)
    print(ns)
    cs = cs[::-1]
    print(cs)
    c3 = [l * r for (l, r) in zip(ns, cs)]
    print(c3)
    out = reduce(lambda num1, num2: (num1 + num2), c3, 0)
    print(out)

    # ex = n0*x**6 + n1*x**5 + n2*x**4 + n3*x**3 + n4*x**2 + n5*x**1 + n6*x**0

evaluate('2 4 3', 10)

# тоже самое только map, reduce

evaluatent = lambda a, x: sum(map(lambda i: x ** i[0] * int(i[1]),
                                  enumerate(a)))
print(evaluatent('2 4 3'.split()[::-1], 10))


func = lambda x: x.lower().startswith('a') and x.lower().endswith('a')
print('EXIT lambda: ',func('absda'))




def is_non_negative_num(x):
    if x.replace('.', '', 1).isdigit():
        return True
    else:
        return False


print(is_non_negative_num('10.34ab'), 'FALSE')
# print(is_non_negative_num('10.45'), 'TRUE')
# print(is_non_negative_num('-18'), 'FALSE')
# print(is_non_negative_num('-34.67'), 'FALSE')
# print(is_non_negative_num('987'), 'TRUE')
# print(is_non_negative_num('abcd'), 'FALSE')
# print(is_non_negative_num('123.122.12'), 'FALSE')
# print(is_non_negative_num('123.122'), 'TRUE')

print(any([0, 0, 0, 0]))
print(all([]))
print(all({'': 'None', 'as': 34}))

print('any'*5)
print(any([True, False]))
# print(any([False, False]))
# print(any([True, True]))
# print(any([10, 100, 1000]))
# print(any([0, 0, 0, 0]))
# print(any(['Python', 'C#']))
# print(any(['', '', 'language']))
# print(any([(1, 2, 3), []]))
# print(any([]))
# print(any([[], []]))
# print(any({0: 'Monday', 1: 'Tuesday', 2: 'Wednesday'}))
# print(any({0: 'Monday'}))
# print(any({'name': 'Timur', 'age': 28}))
# print(any({'': 'None', 'age': 28}))

numbers = [10, 30, 20, 50, 40, 60, 70, 80]

total = 0
for index, number in enumerate(numbers, 1):
    if index % 2 == 0:
        total += number
print(total)

words1 = ['яблоко', 'ананас', 'апельсин', 'хурма', 'гранат', 'мандарин', 'айва']
words2 = ['林檎', 'パイナップル', 'オレンジ', '柿']
words3 = ['apple', 'pineapple', 'orange', 'persimmon', 'pomegranate']

print(list(zip(words1, words2, words3)))

num = [1, 2.0, 3.1, 4, 5, 6, 7.9]
# # использование встроенных функций
# # на примере 'isdigit()'
print([str(x).isdigit() for x in num])
# # [True, False, False, True, True, True, False]
# # использование операции сравнения
print([x > 4 for x in num])
# # [False, False, False, False, True, True, True]
# # использование оператора вхождения `in`
print(['.' in str(x) for x in num])
# # [False, True, True, False, False, False, True]
# # использование оператора идентичности `in`
print([type(x) is int for x in num])
# # [True, False, False, True, True, True, False]
# # использование функции map()
print(list(map(lambda x: x > 1, num)))
# [False, True, True, True, True, True, True]

inp = 'abcGjj7'
def check(p):
    if len(p) < 7:
        return 'NO'
    else:
        pat2 = any(map(lambda x: str(x).isdigit(), p))
        pat3 = any(map(lambda x: str(x).islower(),p))
        pat4 = any(map(lambda x: str(x).isupper(), p))
        if all([pat2, pat3, pat4]):
            return 'YES'
        else:
            return 'NO'

print(check(inp))
#
# s = input()
# print('YES' if all((any(i.isupper() for i in s),
#                     any(i.islower() for i in s),
#                     any(i.isdigit() for i in s),
#                     len(s) >= 7)) else 'NO')

