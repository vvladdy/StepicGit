ls = [1,4,2,3,-1]
print(sorted(ls)[-3:][::-1])

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
