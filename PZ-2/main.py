# дано трёхзначное число. Вывести сначала его последнюю цифру
# (единицы) а затем среднюю(десятки)


# обработка исключений
while True:
    try:
        number = int(input("введите трёхзначное число"))  # ввод данных
    except ValueError:
        print("что-то пошло не так")
        continue
    break

# поиск первого числа(единиц)
first_number = number % 100 % 10

# поиск второго числа(десятки)
a = number % 100
second_number = (a - first_number) // 10
a = number % 100
print(f"Первое число(единицы):{first_number}")
print(f"Второе число(десятки):{second_number}")