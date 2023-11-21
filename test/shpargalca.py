from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, ForeignKeyConstraint, Index, \
    PrimaryKeyConstraint, UniqueConstraint, select, func, not_

from sqlalchemy.orm import declarative_base
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from datetime import datetime



# Создает соединение с базой данных PostgreSQL.
# connection = psycopg2.connect(user='postgres',password = '1212')


# connection.set c_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cursor = connection.cursor()
# create_database_book_sql = 'CREATE DATABASE book_sql'
# cursor.execute(create_database_book_sql)
# cursor.close()
# connection.close()






engine = create_engine('postgresql+psycopg2://postgres:1212@localhost/baza_sql')
engine.connect()
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




#---------------------------------------------------------------------------------
# # Обновите данные в таблице "users", изменив email
# и/или phone для одного или нескольких пользователей.

# Обновление данных выполняется с помощью функции update()

# users это имя таблицы

# where это оператор отвечающий за условие

# users.c.id это название столбца и прописана логина
# где в users.c.id равняеться 2 заменить у этого пользователя email на 'gmail.22'

# values оператор задает новые значения для столбцов,
# которые вы хотите обновить в соответствии с условием, указанным в where.

# s = update(users).where(users.c.id == 2).values\
#         (
#     email = 'gmail.22'
# )

# тут мы отправляет изменения в базу данных
#p = conn.execute(s)
# тут мы пишем что хотим сохранить эти изменения
#conn.commit()
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
# - Получить список всех пользователей

# .order_by() - это метод в SQLAlchemy, который используется для
# указания порядка сортировки результатов SQL-запроса.
# Он позволяет упорядочить строки, возвращенные из базы данных,
# по значениям одного или нескольких столбцов.
# если мы вставить order_by(users.c.name) то отсортирован будет по именам
# по стандарту сортирует по id
# s = users.select().order_by()

# conn - это объект подключения к базе данных, который должен
# быть создан и настроен для взаимодействия с
# конкретной базой данных

# engine = create_engine('postgresql+psycopg2://postgres:1212@localhost/baza_sql')
# conn = engine.connect()
# так выглядит подключение conn к базе данных
# r = conn.execute(s)


# fetchall() извлекает набор записей из результата. Если их нет, то вернет None
# print(r.fetchall())
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
# - Получить список пользователей, у которых нет заказов.

# select(users) - это часть SQL-запроса, которая указывает, что мы
# хотим выбрать все столбцы из таблицы users

# where(~(users.c.id.in_(select(orders.c.user_id)))) - это часть SQL-запроса,
# которая определяет условие для выбора данных.
# Здесь мы используем ~ (можем заменить его на not_), чтобы выбрать тех
# покупателей у которых пустая корзина
# Мы выбираем пользователей, у которых id не находится в результатах
# подзапроса select(orders.c.user_id), что означает пользователей, у которых нет заказов.

# conn - это объект подключения к базе данных, который должен
# быть создан и настроен для взаимодействия с
# конкретной базой данных
# execute переводится как выполнять и отвечает за подключение к забе данных

# query = select(users).where(~(users.c.id.in_(select(orders.c.user_id))))
# result = conn.execute(query)
# print(result.fetchall())
# for row in result:
#     print(row)
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
# удалить информацию о студенте
# s = delete(students_lesson_4).where(
#     students_lesson_4.c.name.like('Mark')
# )
# r = conn.execute(s)
# conn.commit()
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
# s = items.select().where(
#     items.c.name.like("M%")
# )
#---------------------------------------------------------------------------------





