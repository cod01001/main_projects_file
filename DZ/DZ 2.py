import decimal
from datetime import datetime


import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    Text, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint, insert, select, \
    asc, desc, update, delete, union

#--------------------------------------|
# # создание базы в users sql
# #установка соединения с postgres
connection = psycopg2.connect(user= 'postgres',password = '1212')
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаем курсор для выполнения операции с базы данных
cursor = connection.cursor()

# создаем базу данных "sqldz slide 50"
sql_create_database_company = "CREATE DATABASE company"
cursor.execute(sql_create_database_company)

# закрываем соединение
cursor.close()
connection.close()
#--------------------------------------|


engine = create_engine('postgresql+psycopg2://postgres:1212@localhost/slide_50')
engine.connect()
print(engine)

metadata = MetaData()