import re

class RomanNumerals:

    def to_roman(self, val):
        def SPQR(m):
            num = int(m[0])
            result = ''
            lst = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                   (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
                   (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
            for arabic, roman in lst:
                result += num // arabic * roman
                num %= arabic
            return result

        pattern = r'[1-9]\d*'

        return (re.sub(pattern, SPQR, str(val)))

    def from_roman(self, roman_num):
        rule_add = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        rule_div = {
            ('I', 'V'): 3,
            ('I', 'X'): 8,
            ('X', 'L'): 30,
            ('X', 'C'): 80,
            ('C', 'D'): 300,
            ('C', 'M'): 800,
        }

        number = 0
        prev_literal = None
        for literal in roman_num:
            if prev_literal and rule_add[prev_literal] < rule_add[literal]:
                number += rule_div[(prev_literal, literal)]
            else:
                number += rule_add[literal]
            prev_literal = literal
        return number

dig = RomanNumerals()
print(dig.to_roman(349))
print(dig.from_roman('CCCXLIX'))


#########################################################################
# variant
#
# ROMANS = {
#     'M': 1000,
#     'CM': 900,
#     'D': 500,
#     'C': 100,
#     'XC': 90,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'IV': 4,
#     'I': 1,
# }
#
#
# class RomanNumerals:
#
#     def to_roman(n):
#         s = ''
#         for key, value in ROMANS.items():
#             while n % value != n:
#                 n = n - value
#                 s += key
#         return s
#
#     def from_roman(r):
#         s = 0
#         for key, value in ROMANS.items():
#             while r.startswith(key):
#                 r = r[len(key):]
#                 s += value
#         return s