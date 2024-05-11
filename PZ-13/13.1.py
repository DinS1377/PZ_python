# В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
# Выполнить замену элементов второй строки исходной матрицы на полученные
# суммы.

from random import randint


# создание матрицы
b = [[randint(1, 10) for _ in range(3)] for _ in range(3)]
print(f'Исходная матрица: {b}')


# вычисление суммы столбцов
summa = [sum(column) for column in zip(*b)]
print(f'Cумма столбцов: {summa}')


#замена элементов
b[1] = summa
print(f'новая матрица: {b}')











