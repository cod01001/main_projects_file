import decimal
from datetime import datetime

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    Text, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint, insert, select, asc, desc, update, delete


# # установка соединения с postgres
# connection = psycopg2.connect(user="postgres", password = "1212")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#
# # создаем курсор для выполнения операции с базой данных
# cursor = connection.cursor()
#
# # # Создаем базу данных "sqldz"
# sql_create_database = 'CREATE DATABASE sqldz'
# cursor.execute(sql_create_database)
# закрываем соединение
# cursor.close()
# connection.close()



engine = create_engine("postgresql+psycopg2://postgres:1212@localhost/sqldz")
engine.connect()
print(engine)

metadata = MetaData()




customers = Table('customers', metadata,
                  # первичный ключ
             Column('id',Integer(), primary_key=True),

                  # имя покупателя
             Column('first_name', String(100), nullable=False),

                  # фамилия покупателя
             Column('last_name', String(100), nullable=False),

                  # уникальное имя покупателя
             Column('username', String(50), nullable=False),

                  # уникальный адрес электронной почты
             Column('email', String(200), nullable=False),

                  # адрес
             Column('address', String(200), nullable=False),

                  # город
             Column('town', String(50), nullable=False),

                  # дата и время создания аккаунта
             Column('created_on', DateTime(),default=datetime.now),

                  # дата и время обновления аккаунта
             Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now),
             )



items = Table('items', metadata,
              # первичный ключ
             Column('id',Integer(), primary_key = True),

              # название
             Column('name',String(200),nullable=False),

              # себестоимость товара
             Column('cost_price',Numeric(10, 2), nullable=False),

              # цена продажи
             Column('selling_price', Numeric(10, 2), nullable=False),

              # количество товаров в наличии
             Column('quantity',Integer(), nullable=False),
             CheckConstraint('quantity > 0', name='quantity_check')
             )

orders = Table('orders',metadata,
                # первичный ключ
              Column('id',Integer(),primary_key=True),

                # внешний ключ, указывающий на колонку id таблицы customers
              Column('customer_id',ForeignKey('customers.id')),

                # дата и время отгрузки заказа
              Column('date_placed',DateTime(),default=datetime.now),

                # дата и время отгрузки заказа
              Column('date_shipped ',DateTime(),default=datetime.now),
              )

order_lines = Table('order_lines', metadata,
                # первичный ключ
              Column('id',Integer(),primary_key=True),

                # внешний ключ, указывающий на id таблицы orders
              Column('order_id',ForeignKey('orders.id')),

                # внешний ключ, указывающий на id таблицы items
              Column('item_id',ForeignKey('items.id')),

                # количество товаров в заказе
              Column('quantity',Integer()),

             )

metadata.create_all(engine)



# ins = customers.insert().values(
#     first_name='Dmitriy',
#     last_name='Yatsenko',
#     username='Moseend',
#     email='moseend@mail.com',
#     address='Shemilovskiy 2=Y per., bld. 8/10, appt. 23',
#     town='Vladivostok'
# )
# print(ins)
conn = engine.connect()
# r = conn.execute(ins)
# conn.commit()
#


#
# ins = insert(customers).values(
#     first_name = 'Mark',
#     last_name='Martiros',
#     username= 'Kram',
#     email='smail@gmail.com',
#     address= 'pod mostom',
#     town='Miami'
# )
# conn = engine.connect()
# r = conn.execute(ins)
# conn.commit()
#
# print(r.inserted_primary_key)


items_list = [
    {
        "name":"Chair",
        "cost_price": 9.21,
        "selling_price": 10.81,
        "quantity": 6
    },
    {
        "name":"Pen",
        "cost_price": 3.45,
        "selling_price": 4.51,
        "quantity": 3
    },
    {
        "name":"Headphone",
        "cost_price": 15.52,
        "selling_price": 16.81,
        "quantity": 50
    },
    {
        "name":"Travel Bag",
        "cost_price": 20.1,
        "selling_price": 24.21,
        "quantity": 50
    },
    {
        "name":"Keyboard",
        "cost_price": 20.12,
        "selling_price": 22.11,
        "quantity": 50
    },
    {
        "name":"Monitor",
        "cost_price": 200.14,
        "selling_price": 212.89,
        "quantity": 50
    },
    {
        "name":"Watch",
        "cost_price": 100.58,
        "selling_price": 104.41,
        "quantity": 50
    },
    {
        "name":"Water Bottle",
        "cost_price": 20.89,
        "selling_price": 25.00,
        "quantity": 50
    },
]

order_list = [
    {
        "customer_id": 1
    },
    {
        "customer_id": 1
    }
]

order_line_list = [
    {
        "order_id": 1,
        "item_id": 1,
        "quantity": 5
    },
    {
        "order_id": 1,
        "item_id": 2,
        "quantity": 2
    },
    {
        "order_id": 1,
        "item_id": 3,
        "quantity": 1
    },
    {
        "order_id": 2,
        "item_id": 1,
        "quantity": 5
    },
    {
        "order_id": 2,
        "item_id": 2,
        "quantity": 5
    },
]

# r = conn.execute(insert(items), items_list)
# k = conn.execute(insert(orders), order_list)
# l = conn.execute(insert(order_lines), order_line_list)
# conn.commit()
# s = customers.select()
# print(s)
# r = conn.execute(s)
# print(r.fetchall())



# для вывода из таблицы информации
# s = items.select().where(
#     items.c.cost_price + items.c.selling_price > 50).\
#     where(items.c.quantity > 10)
#
# print(s)
# r = conn.execute(s)
# print(r.fetchall())



# s = items.select().where(
#     (items.c.cost_price > 200) &
#     (items.c.quantity > 5)
# )
# print(s)
# r = conn.execute(s)
# print(r.fetchall())

# s = select([items]).\
#     where(
#
# )



# k = orders.select().where(orders.c.date_shipped == None)
# IS NOT NULL

# select([orders]).where(
#     orders.c
# )

#всех с именеи марк
# s = customers.select().where(
#     customers.c.first_name.in_(['Mark','Rita'])
# )
# r = conn.execute(s)
# print(r.fetchall())



# всех у кого нет имени марк
# s = customers.select().where(
#     customers.c.first_name.notin_(['Mark','Rita'])
# )



# где кост прайс ОТ 10 ДО 20  between ЭТО МЕЖДУ
# s = items.select().where(
#     items.c.cost_price.between(10,20)
# )


# s = items.select().where(
#     items.c.name.like("M%")
# )


# по порядку или алфовиту
s = items.select().order_by(
    desc(items.c.cost_price)
)
print(s)

# # обновление записей
# s = update(items).where(
#     items.c.name== 'Monitor'
# ).values(
#     selling_price = 30,
#     quantity = 60,
# )
# s1 = items.select().order_by(
#     desc(items.c.cost_price)
# )
# rs = conn.execute(s)
# r = conn.execute(s1)
# print(r.fetchall())


# s = delete(items).where(
#     items.c.name.like('Watch')
# )
# r = conn.execute(s)
# conn.commit()
# s1 = items.select().order_by(
#     desc(items.c.cost_price)
# )
# rs = conn.execute(s1)
#
# print(rs.fetchall())




