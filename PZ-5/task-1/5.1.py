# создать функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов

import random

symbols = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
while True:
    try:
        k = int(input("введите число символов"))
        break
    except ValueError:
         print("что-то пошло не так")
         continue


def string(k):
    string = ""
    for i in range(k):
        string = string + random.choice(symbols)
    print(f"строка: {string}")

string(k)
