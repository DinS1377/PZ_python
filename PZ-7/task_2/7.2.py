# Дана строка-предложение на русском языке. Подсчитать количество содержащихся
# в строке знаков препинания.

sentence = "Привет, как дела? Всё хорошо!"

count_punctuation = 0
punctuation_marks = ".,;:!?-"

for char in sentence:
    if char in punctuation_marks:
        count_punctuation += 1

print("Количество знаков препинания в предложении:", count_punctuation)