import pickle

"""
task 1
Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки. 
Добавьте методы для вычисления процентных начислений и снятия денег.
"""


class Bank:
    def __init__(self, amount, percent):
        self.amount = amount
        self.percent = percent

    def calculate_interest(self):
        interest = self.amount * (self.percent / 100)
        return interest

    def withdraw(self, amount_to_withdraw):
        if amount_to_withdraw <= self.amount:
            self.amount -= amount_to_withdraw
            return f"{amount_to_withdraw}$ снято."
        else:
            return "недостаточно средств"


safe_1 = Bank(5000, 10)
safe_2 = Bank(10000, 15)

"""
task 2
Создайте класс "Животное", который содержит информацию о виде и возрасте 
животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса 
"Животное" и содержат информацию о породе.
"""

class Animal:
    def __init__(self, kind, age):
        self.kind = kind
        self.age = age


class Dog(Animal):
    def __init__(self, kind, age, breed):
        super().__init__(kind, age)
        self.breed = breed


class Cat(Animal):
    def __init__(self, kind, age, breed):
        super().__init__(kind, age)
        self.breed = breed


dog = Dog("Собака", 5, "Лабрадор")
cat = Cat("Кошка", 3, "Персидская")


print(f"Собака: Вид - {dog.kind}, Возраст - {dog.age}, Порода - {dog.breed}")
print(f"Кошка: Вид - {cat.kind}, Возраст - {cat.age}, Порода - {cat.breed}")

"""
task 3
Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате.
"""


def save_def(safe):
    with open("safes", 'wb') as file:
        pickle.dump(safe, file)


def load_def():
    with open("safes", 'rb') as file:
        return pickle.load(file)


save_def([safe_1, safe_2])

loaded_safes = load_def()

for safe in loaded_safes:
    print(f"Сумма: {safe.amount}")
    print(f"Процент: {safe.percent}")
    print(f"Прибыль год: {safe.calculate_interest()}")