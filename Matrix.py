# Ход коня
x, y = 0, 0

doska = [['.'] * 12 for i in range(12)]
doska_dict = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7
}
basepoint = 'e4'
basepoint.split()
y = (int(basepoint[1]))
for k, v in doska_dict.items():
    if k == basepoint[0]:
        x = v
print(f'буква: {x} , цифра {y}')

i = int(8-y)
j = int(x)

doska[i][j] = 'N'

doska[i + 2][j + 1] = '*'
doska[i - 2][j + 1] = '*'
doska[i - 1][j + 2] = '*'
doska[i + 1][j + 2] = '*'
doska[i + 2][j - 1] = '*'
doska[i + 1][j - 2] = '*'
doska[i - 1][j - 2] = '*'
doska[i - 2][j - 1] = '*'

for i in range(8):
    for j in range(8):
        print(doska[i][j], end=' ')
    print()

print()
row = 3
col = 4
matr = [['*']* col for i in range(row)]

# 1 вариант:
for i in range(row):
    for j in range(i % 2, col, 2):
        matr[i][j] = '.'

# 2 вариант:
for i in range(row):
    for j in range(col):
        if (i + j) % 2 == 0:
            matr[i][j] = '.'
for i in matr:
    print(*i)

print()
# Дана матрица. Элементы на побочной диагонали = 1, под ней = 2, над ней = 0

n = 4 # int(input('Enter number: '))

matr = [[0]* n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == n-1-j:
            matr[i][j] = 1
        if i > n-1-j:
            matr[i][j] = 2
        print(matr[i][j], end = ' ')
    print()

# Дана матрица. Заполнить ее последовательностью чисел от 1 до N по
# строкам.
print()
row = 3
col = 4
matr = []

for t in range(1, row * col+1):
    matr.append(t)
for x in range(0, len(matr), col):
    chunck = matr[x: x+col]
    print(*chunck)
print()
# 2 вариант:

row = 6
col = 6
matr = [[0]* col for i in range(row)]

for i in range(row):
    for j in range(col):
        matr[i][j] = i*col + j + 1
        print(str(matr[i][j]).ljust(3), end=' ')
    print()

print()

# Дана матрица. Заполнить ее последовательностью чисел от 1 до N по
# столбцам.

for i in range(row):
    for j in range(col):
        matr[i][j] = j*row + i + 1
        print(str(matr[i][j]).ljust(3), end=' ')
    print()

print()

# Заполнение матрицы по спирали

n, m = 4, 5
# n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]

i, j, d = 0, 0, 0
moves = ((0, 1,), (1, 0,), (0, -1,), (-1, 0,),)
for k in range(1, n * m + 1):
    a[i][j] = k

    for l in range(4):
        newD = (d + l) % 4
        di, dj = moves[newD]
        newI, newJ = i + di, j + dj
        if 0 <= newI < n and 0 <= newJ < m and a[newI][newJ] == 0:
            i, j, d = newI, newJ, newD
            break
for row in a:
    print(*row)

print()
print('Fill matr on diagonal')
# Дана матрица. Заполнить матрицу по диагонали последовательностью чисел
n = 3
m = 4
# n, m = map(int, input().split())

a = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == n-1-j:
            matr[i][j] = 1
        if i > n-1-j:
            matr[i][j] = 2
        print(matr[i][j], end = ' ')
    print()

# Ход ферзя
x, y = 'c4' #input('Enter coordinate: ')
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)

for i in range(n):
    for j in range(n):
        if (y == i) or (x == j) or abs(y - i) == abs(x - j):
            board[y][x] = 'Q'
            board[i][j] = '*'

for row in board:
    print(*row)


# Диагонали параллельные главной

n = 6#int(input('Enter number: '))
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))


# Каждый n-й элемент

# На вход подается строка текста.
# Напишите программу, которая разделяет список на вложенные подсписки, где
# n - количество последовательных элементов, прнадлежащих каждому подсписку

def slice(st, step):
    return [st[i::step] for i in range(step)]

stroka = 'a b c d e f g h i j k l m n'.split()
step= 3
print(' Answer: ', slice(stroka, step))