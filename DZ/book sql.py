import decimal
from datetime import datetime

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    Text, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint, insert, select, \
    asc, desc, update, delete, union, func

# psycopg2 - это библиотека для Python, которая предоставляет доступ к базе
# данных PostgreSQL из Python-приложений. Она позволяет взаимодействовать
# с PostgreSQL, выполнять SQL-запросы, создавать, изменять и управлять данными в базе данных.
# postgres в строке подключения psycopg2.connect(user='postgres', password='1212')
# является именем пользователя базы данных PostgreSQL, к которой вы пытаетесь подключиться.
# connection = psycopg2.connect(user='postgres',password = '1212')


# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# говорит базе данных PostgreSQL, что каждая команда, отправляемая через это соединение,
# должна выполняться как отдельная операция, а не как часть большой групповой транзакции.
# ISOLATION_LEVEL_AUTOCOMMIT, каждая команда немедленно вступает в силу и не ожидает завершения
# всего оставльного ввода команд


# cursor = connection.cursor()
# 1 connection - это переменная, представляющая соединение с базой данных PostgreSQL.
# Это соединение было установлено ранее с помощью psycopg2.connect(), и оно позволяет
# взаимодействовать с базой данных.
# 2 .cursor() - это метод объекта соединения (connection), который создает новый объект-курсор.
# Курсор предоставляет способ выполнения SQL-запросов к базе данных.


# create_database_book_sql = 'CREATE DATABASE book_sql'
# CREATE DATABASE - это часть SQL-запроса, которая указывает,
# что мы хотим создать новую базу данных.


# cursor.execute(create_database_book_sql)
# отправляем в базу данных запрос create_database_book_sql = 'CREATE DATABASE book_sql' который создали
# ранее для создания таблицы


# cursor.close()
# Эта строка закрывает объект-курсор, который был создан ранее с помощью метода .cursor().
# Закрытие курсора освобождает ресурсы, связанные с ним, и завершает его использование.
# После закрытия курсора, вы не можете выполнять дополнительные SQL-запросы с этим курсором.

# connection.close()
# Эта строка закрывает соединение с базой данных PostgreSQL. Закрытие соединения завершает
# соединение с базой данных и освобождает ресурсы, связанные с соединением.
# После закрытия соединения, вы не можете взаимодействовать с базой данных через это соединение



engine = create_engine('postgresql+psycopg2://postgres:1212@localhost/book_sql')
engine.connect()
metadata = MetaData()

authors = Table('Authors',metadata,
                Column('author_id',Integer(),primary_key=True),
                Column('author_name', String()),
                Column('birth_year',Integer())
                )

books = Table('Books',metadata,
                Column('book_id',Integer(),primary_key=True),
                Column('book_title',String()),
                Column('publication_year',Integer()),
                Column('author_id',ForeignKey('Authors.author_id'))
                )
metadata.create_all(engine)
conn = engine.connect()
conn.commit()

authors_list = [
    {
        'author_name': 'Alexander Pushkin',
        'birth_year': '1799'
    },
    {
        'author_name': 'Vladimir Mayakovsky',
        'birth_year': '1893'
    },
    {
        'author_name': 'Lev Tolstoy',
        'birth_year': '1828'
    },
]

r = conn.execute(insert(authors), authors_list)
conn.commit()




# books_list = [
#     {
#         'book_title': 'War and Peace 2 sezon',
#         'publication_year': '1867',
#         'author_id': '3'
#      }
#     {
#         'book_title': 'childhood',
#         'publication_year': '1852',
#         'author_id': '3'
#     },
#     {
#         'book_title': 'what is good',
#         'publication_year': '1929',
#         'author_id': '2'
#     },
#     {
#         'book_title': 'Dubrovsky',
#         'publication_year': '1841',
#         'author_id': '1'
#     },
#]

# r2 = conn.execute(insert(books), books_list)
# conn.commit()

# Получить список всех авторов.
# s = authors.select().order_by()
# r = conn.execute(s)
# print(r.fetchall())


# Получить список книг, опубликованных в определенном году.
# s = books.select().where(books.c.publication_year == 1841)
# r = conn.execute(s)
# print(r.fetchall())


# Получить список книг, у которых название содержит определенное слово или фразу.
# s = books.select().where(books.c.book_title.like('D%'))
# r = conn.execute(s)
# print(r.fetchall())



# Получить список книг, написанных определенным автором (используя оператор JOIN)
# s = books.select().join(authors,books.c.author_id == authors.c.author_id).where(authors.c.author_name == 'Lev Tolstoy')
# r = conn.execute(s)
# print(r.fetchall())




# # Получить средний возраст авторов.
# current_year = datetime.now().year
# average_age = conn.execute(func.avg(current_year - authors.c.birth_year)).scalar()
# print(average_age)



# # Получить список уникальных годов публикации книг.
# x = select(books.c.publication_year).distinct()
# y = conn.execute(x)
# print(y.fetchall())

# # Получить список уникальных годов публикации книг. второй вариант
# s = books.select().distinct(books.c.publication_year)
# r = conn.execute(s)
# print(r.fetchall())



# - Получить наибольший и наименьший год рождения среди авторов.
# x = conn.execute(func.max(authors.c.birth_year)).scalar()
# x2 = conn.execute(func.min(authors.c.birth_year)).scalar()
# print(x)
# print(x2)
























