import decimal
from datetime import datetime


import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    Text, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint, insert, select, \
    asc, desc, update, delete, union

#------------------------------------------------------------------------------------------
# # создание базы в users sql
# #установка соединения с postgres
connection = psycopg2.connect(user= 'postgres',password = '1212')
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаем курсор для выполнения операции с базы данных
cursor = connection.cursor()

# создаем базу данных "sqldz slide 50"
sql_create_database_dz50 = "CREATE DATABASE slide_50"
cursor.execute(sql_create_database_dz50)

# закрываем соединение
cursor.close()
connection.close()
# ----------


engine = create_engine('postgresql+psycopg2://postgres:1212@localhost/slide_50')
engine.connect()
print(engine)

metadata = MetaData()



# задание 3
engine = create_engine("postgresql+psycopg2://postgres:1212@localhost/slide_50")
engine.connect()
metadata = MetaData()
students_lesson_3 = Table('students_lesson_3', metadata,
         #первичный ключ
         Column('id', Integer(), primary_key=True),

         #имя
         Column('name', String(50), nullable=False),

         #возраст
         Column('age', Integer(), nullable=False)
         )

metadata.create_all(engine)
conn = engine.connect()
conn.commit()



#---------------------------------------\
# # вставить 3 записи
# students_lesson_3_insert = [{
#         'name': 'John',
#         'age': 20,
#     },
#     {
#         'name': 'Jane',
#         'age': 22,
#     },
#     {
#         'name': 'Bob',
#         'age': 19,
#     }
# ]
#
# l = conn.execute(insert(students_lesson_3), students_lesson_3_insert)
# conn.commit()
# #---------------------------------------\
# # изменение возраста в ячейке с id 1
# s = update(students_lesson_3).where(students_lesson_3.c.id == 1).values\
#         (
#     age = 21
# )
# p = conn.execute(s)
# conn.commit()

#---------------------------------------\
# # по порядку и возрастанию
# s = union(students_lesson_3.select().where(students_lesson_3.c.age > 20)).order_by(asc('id'))
# rs = conn.execute(s)
# print(rs.fetchall())
#---------------------------------------\



# # задание 4
# engine = create_engine("postgresql+psycopg2://postgres:1212@localhost/slide_50")
# engine.connect()
# metadata = MetaData()
# students_lesson_4 = Table('students_lesson_4', metadata,
#          # первичный ключ
#          Column('id', Integer(), primary_key=True),
#
#          # имя
#          Column('name', String(50), nullable=False),
#
#          # фамилия
#          Column('last name', String(50), nullable=False),
#
#          # возраст
#          Column('age', Integer(), nullable=False),
#
#          # группа
#          Column('group', String(50), nullable=False),
#                           )
#
# metadata.create_all(engine)
# conn = engine.connect()
# conn.commit()

#---------------------------------------\
# вставляем произвальные записи о студентах
# students_lesson_4_insert = [{
#     'name': 'Kris',
#     'last name': 'Pampilo',
#     'age': 51,
#     'group': '1F'
#     },
#     {
#     'name': 'Jorg',
#     'last name': 'Petrosian',
#     'age': 22,
#     'group': '8M'
#     },
#     {
#     'name': 'Irina',
#     'last name': 'Marads',
#     'age': 11,
#     'group': '64p'
#     }
# ]
# l = conn.execute(insert(students_lesson_4), students_lesson_4_insert)
# conn.commit()
#---------------------------------------\

#---------------------------------------\
# # изменение возраста одного из студентов
# s = update(students_lesson_4).where(students_lesson_4.c.id == 2).values\
#         (
#     age = 50
# )
# p = conn.execute(s)
# conn.commit()
#---------------------------------------\

#---------------------------------------\
# удалить информацию о студенте
# s = delete(students_lesson_4).where(
#     students_lesson_4.c.name.like('Mark')
# )
# r = conn.execute(s)
# conn.commit()
#---------------------------------------\

#---------------------------------------\
# извлечь данные всех студентов в возрасте от 1 до 55
# s = students_lesson_4.select().order_by(asc(students_lesson_4.c.age))
# rs = conn.execute(s)
# print(rs.fetchall())



# задание 5
engine = create_engine("postgresql+psycopg2://postgres:1212@localhost/slide_50")
engine.connect()
metadata = MetaData()
books_lesson_5 = Table('books_lesson_5', metadata,
         # первичный ключ
         Column('id', Integer(), primary_key=True),

         # имя
         Column('name', String(50), nullable=False),

         # автор
         Column('author', String(50), nullable=False),

         # год издания
         Column('the_year_of_publishing', Integer(), nullable=False),

         # сколько страниц
         Column('how_many_pages', Integer(), nullable=False),
                          )

metadata.create_all(engine)
conn = engine.connect()
conn.commit()

#---------------------------------------\
# вставьте данные для несколькох книг
# books_lesson_5_insert = [{
#     'name': 'razy Town',
#     'author': 'Sterling R. Braswell',
#     'the_year_of_publishing': 2022,
#     'how_many_pages': 267
#     },
#     {
#     'name': 'Under the Influence?',
#     'author': 'Jacques Normand',
#     'the_year_of_publishing': 1994,
#     'how_many_pages': 321
#     },
#     {
#     'name': 'Reducing Underage Drinking',
#     'author': 'Dewey G. Cornell',
#     'the_year_of_publishing': 2004,
#     'how_many_pages': 317
#     }
# ]
# l = conn.execute(insert(books_lesson_5), books_lesson_5_insert)
# conn.commit()
#---------------------------------------\

#---------------------------------------\
# изменение количество страниц для одной из книг
# s = update(books_lesson_5).where(books_lesson_5.c.id == 3).values\
#         (
#     how_many_pages = 50
# )
# p = conn.execute(s)
# conn.commit()
#---------------------------------------\

#---------------------------------------\
# удалить информацию о книге
# s = delete(books_lesson_5).where(books_lesson_5.c.id == 2)
# s = conn.execute(s)
# conn.commit()
#---------------------------------------\
# вывести информация о книге написанной автором 'Dewey G. Cornell'
# s = select(books_lesson_5).where(books_lesson_5.c.author == 'Dewey G. Cornell')
# s = conn.execute(s)
# print(s.fetchall())
























