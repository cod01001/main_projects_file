import decimal
from datetime import datetime
from multiprocessing import connection

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    Text, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint, insert, select, \
    asc, desc, update, delete, union, func

#------------------------------------------------------------------------------------------
# создание базы в users sql
#установка соединения с postgres
# connection = psycopg2.connect(user= 'postgres',password = '1212')
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#
# # Создаем курсор для выполнения операции с базы данных
# cursor = connection.cursor()
#
# # создаем базу данных "sqldz slide 50"
# sql_create_database_baza_sql = "CREATE DATABASE baza_sql"
# cursor.execute(sql_create_database_baza_sql)
#
# # закрываем соединение
# cursor.close()
# connection.close()
# ----------


engine = create_engine('postgresql+psycopg2://postgres:1212@localhost/baza_sql')
engine.connect()
print(engine)
metadata = MetaData()

users = Table('users', metadata,
         # первичный ключ
         Column('id', Integer(), primary_key=True),

         # имя
         Column('name', String(50), nullable=False),

         #возраст
         Column('email', String(100), nullable=False),

         Column('phone', String(20), nullable=False)
         )

orders = Table('orders', metadata,
         #первичный ключ
         Column('id', Integer(), primary_key=True),

         Column('user_id', ForeignKey('users.id')),

         Column('product', String(100), nullable=False),

         Column('price', Integer(), nullable=False)
         )

metadata.create_all(engine)
conn = engine.connect()
conn.commit()



#
# items_list = [
#     {
#         "name": 'Kirill',
#         "email": 'gmail.gmail',
#         "phone": '111'
#     },
#     {
#         "name": 'Mihsa',
#         "email": 'mail',
#         "phone": '222'
#     },
#     {
#         "name": 'Alex',
#         "email": 'yandex',
#         "phone": '333'
#     },
#     {
#         "name": 'Sania',
#         "email": 'mazila',
#         "phone": '444'
#     },
#     {
#         "name": 'Grisha',
#         "email": 'forex',
#         "phone": '555'
#     },
# ]

# r = conn.execute(insert(users), items_list)
# conn.commit()

# orders_list = [
#     {
#         "user_id": 1,
#         "product": 'carrot',
#         "price": 22
#     },
#     {
#         "user_id": 1,
#         "product": 'potato',
#         "price": 25
#     },
#     {
#         "user_id": 1,
#         "product": 'beet',
#         "price": 11
#     },
#     {
#         "user_id": 2,
#         "product": 'tea',
#         "price": 2
#     },
#     {
#         "user_id": 2,
#         "product": 'coffee',
#         "price": 3
#     },
#     {
#         "user_id": 2,
#         "product": 'sugar',
#         "price": 5
#     },
#     {
#         "user_id": 3,
#         "product": 'apple',
#         "price": 15
#     },
#     {
#         "user_id": 3,
#         "product": 'pear',
#         "price": 17
#     },
#     {
#         "user_id": 4,
#         "product": 'lighter',
#         "price": 10
#     },
#     {
#         "user_id": 4,
#         "product": 'matches',
#         "price": 6
#     },
# ]
# r = conn.execute(insert(orders), orders_list)
# conn.commit()


#---------------------------------------\
# # Обновите данные в таблице "users", изменив email
# и/или phone для одного или нескольких пользователей.
# s = update(users).where(users.c.id == 2).values\
#         (
#     email = 'gmail.22'
# )
# p = conn.execute(s)
# conn.commit()
#---------------------------------------\_


#---------------------------------------
# - Получить список всех пользователей и их заказов.
# s = users.select().order_by()
# s2 = orders.select().order_by()
# r = conn.execute(s)
# r2 = conn.execute(s2)
# print(r.fetchall())
# print(r2.fetchall())
#---------------------------------------



#---------------------------------------
# - Получить список пользователей, у которых есть заказы.
# s = orders.select().where()
# r = conn.execute(s)
# #print(r.fetchall())
# for row in r:
#     print(row)
#---------------------------------------


#----------------------------------+__
# ins = insert(users).values(
#     name = 'Rodrigez',
#     email = 'Rodrigez@gmail',
#     phone = '32112322'
#     )
# conn.execute(ins)
# conn.commit()
# Создайте объекты для запроса
#----------------------------------


#----------------------------------
# Получить список пользователей, у которых нет заказов.
# query = select(users).where(~users.c.id.in_(select(orders.c.user_id)))
# result = conn.execute(query)
# print(result.fetchall())
# for row in result:
#     print(row)


# так не пишем для списка пользователей у которых нет заказов!!!!
# query = users.select().join(orders, users.c.id == orders.c.user_id).where(orders.c.user_id == None).group_by(users.c.id)
# r = conn.execute(query)
# print(r.fetchall())

#----------------------------------


#----------------------------------
# - Получить список заказов с указанием имени пользователя.
# query = select(users).where(users.c.id.in_(select(orders.c.user_id)))
# result = conn.execute(query)
# for row in result:
#     print(row)
#----------------------------------


#----------------------------------
#   - Получить список заказов, у которых цена превышает определенную сумму.
# subquery = select(orders.c.user_id).where(orders.c.price > 8)
# query = select(users).where(users.c.id.in_(subquery))
# result = conn.execute(query)
# for row in result:
#     print(row)
#----------------------------------


#----------------------------------
#   - Получить общую сумму всех заказов для каждого пользователя.
# subquery = select(users.c.name,func.sum(orders.c.price)).where(users.c.id == orders.c.user_id).group_by(users.c.id)
# result = conn.execute(subquery)
# for row in result:
#     print(row)
#----------------------------------


#----------------------------------
#   - Получить среднюю цену заказов для каждого пользователя.


#----------------------------------


#----------------------------------
# - Получить список всех пользователей и их заказов.
# s = users.select().order_by()
# s2 = orders.select().order_by()
# r = conn.execute(s)
# r2 = conn.execute(s2)
#
# print(r)

# for row in r:
#     print(row)

# print('\nзаказы\n')
# for row2 in r2:
#     print(row2)






