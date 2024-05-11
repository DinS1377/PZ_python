#Дана строка-предложение на русском языке. Подсчитать количество содержащихся
#в строке знаков препинания.

from string import punctuation


Str = "Завари мне, пожалуйста, чай. Немедленно отойди от дороги!"
number = 0

for i in Str:
    if i in punctuation:
        number = number + 1


print(number)
