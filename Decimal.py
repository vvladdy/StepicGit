from decimal import Decimal

print('из str', Decimal('3.6799'))  # OK можно
print('из int',Decimal(56))         # OK можно
print('из float',Decimal(4.6))      # NOT Нельзя
print('из str', Decimal('4.6'))     # OK можно

s = '9.80 4.76 4.67 2.87 3.89 6.98 8.23 7.89'.split(' ')
arr = []
for i in s:
    arr.append(Decimal(i)) # нужно обозначить, что цифры Decimal
print('summa', sum(arr))
print('list', *reversed(sorted(arr)[-5:]))

n = '12.1244354689'
num = Decimal(n)
s = 0
num = Decimal(n)
num_tuple = num.as_tuple()
n_tp = num_tuple.digits
print(num_tuple)
if -1 < num < 1:
    s = 0 + max(n_tp)
else:
    s= max(n_tp)+min(n_tp)
print('summa',s)

from fractions import Fraction

s1 = '9.80 4.76 4.67 2.87 3.89 6.98 8.23 7.89'.split(' ')
arr = []
for i in s1:
    arr.append(Fraction(i)) # нужно обозначить, что цифры Decimal
print('summa fraction', sum(arr))
print('max el', max(arr))


print(Fraction(3, 6))