"""
Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для автоматизированного контроля затрат на производство продукции. БД должна
содержать таблицу Расходы со следующей структурой записи: Дата, Код продукта, Наименование продукта, Расходы, Сумма.

"""

import sqlite3 as sq

with sq.connect('exspenses.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS expenses(
                data DATE NOT NULL,
                prod_code INT UNIQUE NOT NULL,
                prod_name VARCHAR(20) NOT NULL,
                expenses int NOT NULL,
                sum int)
                 """
                )

    def add_product(data, prod_code, prod_name, expense, summa):
        cur.execute("INSERT INTO expenses(data, prod_code, prod_name, expenses, sum) VALUES(?,?,?,?,?)",
                    (data, prod_code, prod_name, expense, summa))
        con.commit()

    def get_product():
        cur.execute('SELECT * FROM expenses')
#
#
# add_product('20.11.2006', 1, "хлеб", 350, 200)
# add_product('19.05.1991', 2, "молоко", 450, 300)
# add_product('06.11.1935', 3, "овсянка", 150, 400)
# add_product('26.11.1911', 4, "чипсы", 100, 500)
# add_product('13.03.1950', 5, "чебупели", 50, 600)
# add_product('21.08.1961', 6, "сырок творожный", 1000, 700)
# add_product('12.05.1940', 7, "паста томатная", 500, 800)
# add_product('28.07.1970', 8, "пармезан", 600, 900)
# add_product('14.04.1932', 9, "колбаса", 1500, 1000)
# add_product('04.09.2008', 10, "курятина", 5, 1100)
# add_product('06.01.2001', 11, "свинина", 1, 1200)


#select
with sq.connect('exspenses.db') as con:
    cur.execute('SELECT * from expenses where sum > 300 and sum < 800')
    print(cur.fetchall())

with sq.connect('exspenses.db') as con:
    cur.execute('SELECT * from expenses where expenses > 400  and expenses < 1000')
    print(cur.fetchall())

with sq.connect('exspenses.db') as con:
    cur.execute('SELECT * from expenses where sum > 600 and prod_code < 7')
    print(cur.fetchall())


#delete
with sq.connect('exspenses.db') as con:
    cur.execute('DELETE from expenses where prod_name like "свинина" and sum < 800')
    con.commit()


with sq.connect('exspenses.db') as con:
    cur = con.cursor()
    cur.execute('DELETE from expenses where expenses > 300 and prod_code < 10')
    con.commit()


with sq.connect('exspenses.db') as con:
    cur.execute('DELETE from expenses where prod_name like "свинина" and sum < 1300')
    con.commit()


#update
with sq.connect('exspenses.db') as con:
    cur = con.cursor()
    cur.execute('UPDATE expenses SET sum=1000 where prod_name like "хлеб"')


with sq.connect('exspenses.db') as con:
    cur = con.cursor()
    cur.execute('UPDATE expenses SET expenses=1000 where sum > 500')


with sq.connect('exspenses.db') as con:
    cur = con.cursor()
    cur.execute('UPDATE expenses SET prod_name="изменено" where prod_name like "молоко"')


















