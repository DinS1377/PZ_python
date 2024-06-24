#Дана строка. Подсчитать общее количество содержащихся в ней строчных
#латинских и русских букв.

from string import ascii_letters

rus_alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
lat = 0
rus = 0
qwerty = 'qаавчОлWwCHKвддфHI'


for i in qwerty:
    if i.isupper():
        continue
    elif i in ascii_letters:
        lat = lat + 1
    elif i in rus_alphabet:
        rus = rus + 1


print(f"общее число букв: {lat+rus}")