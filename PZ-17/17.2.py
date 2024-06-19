# дано трёхзначное число. Вывести сначала его последнюю цифру
# (единицы) а затем среднюю(десятки)

import tkinter as tk

def check_number():
    try:
        number = int(entry.get())
        if number > 99 and number < 1000:
            result1_label.config(text=f"первая цифра: {number//100}")
            result2_label.config(text=f"средняя цифра: {number % 100 // 10}")
        else:
            result1_label.config(text="Введите ТРЁХЗНАЧНОЕ целое число")
            result2_label.config(text="")

    except ValueError:
        result1_label.config(text="Введите целое число")


# Создаем окно
root = tk.Tk()
root.title("Проверка числа")

# Создаем виджеты
entry_label = tk.Label(root, text="Введите целое число:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Проверить", command=check_number)
check_button.pack()

result1_label = tk.Label(root, text="")
result1_label.pack()

result2_label = tk.Label(root, text="")
result2_label.pack()

# Запускаем цикл обработки событий
root.mainloop()