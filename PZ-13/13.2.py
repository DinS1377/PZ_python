# В матрице найти минимальный элемент в предпоследней строке.

from random import randint


# создание матрицы
b = [[randint(1, 10) for _ in range(3)] for _ in range(4)]
print(b)

print(f'Минимальный элемент в предпоследней строке: {min(b[len(b)-2])}')

