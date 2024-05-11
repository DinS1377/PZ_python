# Составить генератор (yield), который выводит из строки только буквы.

text = 'r3oigjwe2orig1jw0eroi'


def letters_only(text):
    for char in text:
        if char.isalpha():
            yield char

print('строка без цифр:', ''.join([i for i in letters_only(text)]))






