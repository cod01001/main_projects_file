import decimal
from datetime import datetime

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    Text, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint, insert, select, \
    asc, desc, update, delete, union, func
from sqlalchemy.orm import query

# connection = psycopg2.connect(user='postgres',password='1212')
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cursor = connection.cursor()
# create_database_employeessql = 'CREATE DATABASE employeessql'
# cursor.execute(create_database_employeessql)
# cursor.close()
# connection.close()

engine = create_engine('postgresql+psycopg2://postgres:1212@localhost/employeessql')
engine.connect()
metadata = MetaData()

employees = Table('employees',metadata,
                  Column('id',Integer(),primary_key=True),
                  Column('name',String()),
                  Column('age',Integer()),
                  Column('position',String()),
                  Column('salary',Integer())
                  )

metadata.create_all(engine)
conn = engine.connect()
conn.commit()
# #
# list_1 = [
#     {
#         'name': 'Murma', 'age': '26', 'position': 'tester', 'salary': '0'
#     },
#     {
#         'name': 'Artem', 'age': '16', 'position': 'night watchman', 'salary': '3500'
#     },
#     {
#         'name': 'Anna', 'age': '41', 'position': 'developer', 'salary': '0'
#     }
# ]
# r = conn.execute(insert(employees), list_1)
# conn.commit()



# 3. Обновите данные в таблице "employees" с помощью оператора UPDATE:
#    - Обновите поле salary для записи с id=2 и установите значение 4500

# s = update(employees).where(employees.c.id == 2).values \
#     (
#     salary = '4500'
#     )
# p = conn.execute(s)
# conn.commit()



# 4. Удалите данные из таблицы "employees" с помощью оператора DELETE:
#    - Удалите запись с id=3
# s = delete(employees).where(employees.c.id == 3)
# r = conn.execute(s)
# conn.commit()

print()
#5. Используйте оператор SELECT для выполнения следующих запросов:
   # - Выведите все записи из таблицы "employees"
def x():
    y = conn.execute(select(employees))
    return y.fetchall()
# print(x())

   # - Выведите уникальные значения поля position из таблицы "employees"
# пока не знаю как сделать


   # - Выведите записи из таблицы "employees", где возраст (age) больше 30
def x3():
    y = conn.execute(select(employees).where(employees.c.age > 30))
    return y.fetchall()
# print(x3())

   # - Выведите записи из таблицы "employees", отсортированные по возрастанию поля salary
def x4():
    y = conn.execute(select(employees).order_by(employees.c.salary))
    return y.fetchall()
# print(x4())

   # - Выведите первые 3 записи из таблицы "employees"
def x5():
    y = conn.execute(select(employees).limit(3))
    return y.fetchall()
# print(x5())

   # - Выведите записи из таблицы "employees", где имя (name) содержит букву 'a'
def x6():
    y = conn.execute(select(employees).where(employees.c.name.like('%a%')))
    return y.fetchall()
# print(x6())

   # - Выведите записи из таблицы "employees", где должность (position) равна 'Manager' или 'Developer'
def x7():
    y = conn.execute(select(employees).where(employees.c.position.in_(['Manager','Developer'])))
    return y.fetchall()
# print(x7())

   # - Выведите записи из таблицы "employees", где возраст (age) находится в диапазоне от 25 до 35
def x8():
    y = conn.execute(select(employees).where(employees.c.age.between(25,35)))
    return y.fetchall()
# print(x8())

   # - Выведите записи из таблицы "employees", где поле salary имеет значение NULL
def x9():
    y = conn.execute(select(employees).where(employees.c.salary == '0'))
    return y.fetchall()
# print(x9())

   # - Выведите записи из таблицы "employees", где поле salary имеет значение больше 4000
def x10():
    y = conn.execute(select(employees).where(employees.c.salary > '4000'))
    return y.fetchall()
# print(x10())

   # - Выведите количество сотрудников в таблице "employees"
def x11():
    y = conn.execute(select(employees).func.count())
    return y.fetchall()
# не знаю как сделать через conn.execute(select(employees).func.count()) такой формат
# print(x11())

   # - Выведите минимальную и максимальную зарплату сотрудников в таблице "employees"
def x12():
    y = conn.execute(func.max(employees.c.salary)).scalar()
    y0 = conn.execute(select(employees.c.name).where(employees.c.salary == y)).scalar()
    x = conn.execute(func.min(employees.c.salary)).scalar()
    x0 = conn.execute(select(employees.c.name).where(employees.c.salary == x)).scalar()
    return f'''{y0}-{y} максимальное значение 
{x0}-{x} минимальное значение'''
# print(x12())
# поавда это не все значения с минимальной заралатой(

   # - Выведите среднюю зарплату сотрудников в таблице "employees"
def x13():
    y = conn.execute(func.avg(employees.c.salary)).scalar()
    return y
#print(x13())

   # - Выведите сумму зарплат сотрудников в таблице "employees"
def x14():
    y = conn.execute(func.sum(employees.c.salary)).scalar()
    return y
#print(x14())


