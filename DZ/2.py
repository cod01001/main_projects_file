import decimal
from datetime import datetime


import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    Text, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint, insert, select, asc, desc, update, delete


#------------------------------------------------------------------------------------------
# создание базы в users sql
# #установка соединения с postgres
# connection = psycopg2.connect(user= 'postgres',password = '1212')
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#
# # Создаем курсор для выполнения операции с базы данных
# cursor = connection.cursor()
#
# # создаем базу данных "sqldz slide 50"
# sql_create_database_dz50 = "CREATE DATABASE slide_50"
# cursor.execute(sql_create_database_dz50)
#
# # закрываем соединение
# cursor.close()
# connection.close()
#----------


engine = create_engine('postgresql+psycopg2://postgres:1212@localhost/slide_50')
engine.connect()
print(engine)

metadata = MetaData()

#|------------------------------------------------------------------------------------------|
# создаем таблицу users
users = Table('users', metadata,
                  # первичный ключ
             Column('id',Integer(), primary_key=True),

                  # имя
             Column('name', String(50), nullable=False),

                  # имейл
             Column('email', String(50), nullable=False),
                  )


metadata.create_all(engine)
conn = engine.connect()

#----

# создаем таблицу books
books = Table('books', metadata,
                  # первичный ключ
             Column('id',Integer(), primary_key=True),

                  # title
             Column('title', String(50), nullable=False),

                  # year
             Column('author', String(50), nullable=False),


             Column('year', String(50), nullable=False)
             )

metadata.create_all(engine)
conn = engine.connect()

#
# # 1 вставка
# ins = insert(books).values(
#     title = 'The Great Gatsby',
#     author = 'F. Scott Fitzgerald',
#     year = '1925'
#     )
# conn.execute(ins)
# conn.commit()
#
#
#
# # # 2 вставка
# ins = insert(books).values(
#     title = 'To Kill a Mockingbird',
#     author = 'Harper Lee',
#     year = '1960'
#     )
# conn.execute(ins)
# conn.commit()
#
# # # 3 вставка
# ins = insert(books).values(
#     title = '1984',
#     author = 'George Orwell',
#     year = '1949'
#     )
# conn.execute(ins)
# conn.commit()


# отсортированный по годам
s = items.select().order_by(desc(items.c.year))

