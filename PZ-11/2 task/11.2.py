'''
Из предложенного текстового файла (text18-15.txt) вывести на экран его содержимое,
количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно заменив символы нижнего регистра на верхний
'''


f3 = open('text18_15.txt', 'r', encoding='UTF-8')

# содержимое
print('Исходные данные: \n')
[print(line.rstrip()) for line in f3.readlines()]
f3.close()


f3 = open('text18_15.txt', 'r', encoding='UTF-8')
k = [i for i in f3.read()]

# кол во букв нижнего регистра
a = 0
for i in k:
    if i.islower():
        a += 1
    else:
        pass

print(f'количество букв нажнего регистра: {a}')

#замена на верхний
count = 0
for i in k:

    if i.islower():
        k[count] = i.upper()
        count += 1
    else:
        count += 1

f4 = open('text18_15(result).txt', 'w', encoding='UTF-8')
f4.write(''.join(k))





