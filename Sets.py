sentence = '''My very photogenic mother died in a freak accident (picnic,  
lightning) when I was three, and, save for a pocket of warmth in the  darkest  
past, nothing of her subsists within the hollows and dells of memory, over 
which, if you can still stand my style (I am writing under observation), 
the sun of my infancy had set: surely, you all know those redolent remnants 
of day suspended, with the midges, about some hedge in bloom or suddenly 
entered and traversed by the rambler, at the bottom of a hill, in the 
summer dusk; a furry warmth, golden midges.'''.replace(',', '').\
    replace(':', '').replace(';', '').replace('(', '').replace(')', '').replace('.', '')
out = {i.lower() for i in sentence.split()}
print(*sorted(out), sep = ' ')

out1 = {i.lower() for i in sentence.split() if len(i) < 4}
print(*sorted(out1), sep = ' ')


print()

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org',
         'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg',
         'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png',
         'input.tXt', 'split.pop', 'solution.Py', 'stepik.org',
         'kotlin.ko', 'github.git']
new = []
for i in files:
    new.append(i.lower())

outfiles = {i.lower() for i in files if 'png' in i.lower()}

print(outfiles)


set1 = {'yellow', 'orange', 'black'}
set2 = {'orange', 'blue', 'pink'}
set1.difference_update(set2)
print(set1)

set1.update(['hi', 'yellow'])
print(set1)


set3 = {10, 20, 30, 40, 50}
set4 = {60, 70, 10, 30, 40, 80, 20, 50}
print(set3.issubset(set4))
print(set4.issuperset(set3))

# Проверить новая версия ПО или старая 10.10 новее, чем 10.4

version1 = '10.10'
version2 = '10.4'

ver1 = version1
ver2 = version2
print(ver1)
print(ver2)

def compare(t1, t2):
    return [int(i) for i in t1.split(".")] >= [int(i) for i in t2.split(".")]

print(compare(ver1, ver2))


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