# with open('example.txt', 'w') as file:
#     file.write('pop\ngoes\nthe\nweasel!\n')

with open('example.txt', encoding='utf-8') as file:
    print('Repeat after me:', file.readline().strip())
    for line in file:
        print(line.strip() + '!')