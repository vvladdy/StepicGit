def sum_natural(i):
    if i == 1:
        return i
    return (i + sum_natural(i - 1))


print(sum_natural(5))

print('Task 1')


# from typing import Optional
# def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:


def to_power(x: int | float, exp: int) -> int | float:
    if exp < 0:
        raise ValueError('This function works only with exp > 0')
    if exp == 0:
        return 1
    return x * to_power(x, exp - 1)


print(to_power(3.5, 2))
print(to_power(2, 3))
# print(to_power(2, -1))


print('\nTask 2')
"""
Checks if input string is Palindrome
is_palindrome('mom') - True
is_palindrome('sassas')  - True
is_palindrome('o') - True
"""


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if looking_str[:] == looking_str[::-1]:
        return True
    else:
        return False


def is_palindrome_rec(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 1:
        return True
    if looking_str[0] == looking_str[-1]:
        return is_palindrome_rec(looking_str[1:-1])
    else:
        return False


print(is_palindrome_rec('mom'))
print(is_palindrome_rec('sassas'))
print(is_palindrome_rec('ou'))

print('Task 3')
"""
This function works only with positive integers

>>> mult(2, 4) == 8
True

>>> mult(2, 0) == 0
True

>>> mult(2, -4)
ValueError("This function works only with postive integers")
"""


def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError('This function works only with postive integers')
    # print(a)
    if n == 0:
        return 0

    return a + mult(a, n - 1)  # прибавлять а+а+а+...+а (n раз)


print(mult(2, 4))
print(mult(2, 7))
# print(mult(2, -4))


print('\nTask 4')

"""
Function returns reversed input string
>>> reverse("hello") == "olleh"
True
>>> reverse("o") == "o"
True
"""


def reverse(input_str: str) -> str:
    if len(input_str) == 1:
        return input_str
    else:
        return reverse((input_str[1:])) + (input_str[0])


print(reverse('hello'))
print(reverse('o'))

print('\nTask 5')

"""
>>> sum_of_digits('26') == 8
True

>>> sum_of_digits('test')
ValueError("input string must be digit string")
"""


def sum_of_digits(digit_string: str) -> int:
    if digit_string.isdigit() and len(digit_string) == 1:
        return int(digit_string)
    if digit_string.isdigit():
        return int(sum_of_digits(digit_string[1:])) + int(digit_string[0])


print(sum_of_digits('26') == 8)
print(sum_of_digits('26464'))
from time import time
from typing import List, Tuple

# We assume that all lists passed to functions are the same length N

# answers
# 1 - n
# 2 - 1
# 3 - n^2  question3
# 4 - n
# 5 - n^2  question5
# 6 - log n
import time

start1 = time.time()


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


print(question1([14, 31, 4, 8, 9, 8, 1, 7], [1, 2, 3, 4, 5, 7, 12, 78]))
end1 = time.time()
print('F1', end1 - start1)

start = time.time()


def question2(n: int) -> int:
    for _ in range(2):
        n **= 3
    return n


print(question2(2), 8 ** 3)
end = time.time()
print('F2', end - start)

start3 = time.time()


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


print(question1([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
end3 = time.time()
print('F3', end3 - start3)


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


start6 = time.time()


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n


print(question6(22))
end6 = time.time()
print('F6', end6 - start6)
