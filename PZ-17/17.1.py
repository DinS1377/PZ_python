"""
 В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу
"""

import tkinter as tk
from tkinter import ttk


def create_order_form():
    # Create main window
    root = tk.Tk()
    root.title("Создайте заказ")

    # Create main frame
    main_frame = ttk.Frame(root, padding="10 10 10 10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Order information section
    order_info_frame = ttk.LabelFrame(main_frame, text="Информация о заказе", padding="10 10 10 10")
    order_info_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(order_info_frame, text="Номер заказа *").grid(row=0, column=0, sticky=tk.W)
    order_number_entry = ttk.Entry(order_info_frame)
    order_number_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

    ttk.Label(order_info_frame, text="Название товара").grid(row=1, column=0, sticky=tk.W)
    product_name_entry = ttk.Entry(order_info_frame)
    product_name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

    ttk.Label(order_info_frame, text="Количество *").grid(row=2, column=0, sticky=tk.W)
    quantity_entry = ttk.Entry(order_info_frame)
    quantity_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

    # Contact information section
    contact_info_frame = ttk.LabelFrame(main_frame, text="Контактная информация", padding="10 10 10 10")
    contact_info_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(contact_info_frame, text="Ваше имя").grid(row=0, column=0, sticky=tk.W)
    name_entry = ttk.Entry(contact_info_frame)
    name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

    ttk.Label(contact_info_frame, text="Ваш email *").grid(row=1, column=0, sticky=tk.W)
    email_entry = ttk.Entry(contact_info_frame)
    email_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

    ttk.Label(contact_info_frame, text="Ваш телефон *").grid(row=2, column=0, sticky=tk.W)
    phone_entry = ttk.Entry(contact_info_frame)
    phone_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

    # Delivery information section
    delivery_info_frame = ttk.LabelFrame(main_frame, text="Информация о доставке", padding="10 10 10 10")
    delivery_info_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(delivery_info_frame, text="Адрес *").grid(row=0, column=0, sticky=tk.W)
    address_entry = ttk.Entry(delivery_info_frame)
    address_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

    ttk.Label(delivery_info_frame, text="Время доставки").grid(row=1, column=0, sticky=tk.W)

    time_frame = ttk.Frame(delivery_info_frame)
    time_frame.grid(row=1, column=1, sticky=(tk.W, tk.E))

    hours_var = tk.StringVar()
    minutes_var = tk.StringVar()

    hours_spinbox = ttk.Spinbox(time_frame, from_=0, to=23, textvariable=hours_var, width=2, format="%02.0f")
    hours_spinbox.grid(row=0, column=0)
    ttk.Label(time_frame, text=":").grid(row=0, column=1)
    minutes_spinbox = ttk.Spinbox(time_frame, from_=0, to=59, textvariable=minutes_var, width=2, format="%02.0f")
    minutes_spinbox.grid(row=0, column=2)

    # Run the application
    root.mainloop()



create_order_form()