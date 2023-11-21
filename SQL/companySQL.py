import decimal
from datetime import datetime

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    Text, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint, insert, select, \
    asc, desc, update, delete, union, func
from sqlalchemy.orm import query

# •Создайте базу данных "company";
# connection = psycopg2.connect(user='postgres',password='1212')
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cursor = connection.cursor()
# create_database_company_sql = 'CREATE DATABASE company_sql'
# cursor.execute(create_database_company_sql)
# cursor.close()
# connection.close()


engine = create_engine('postgresql+psycopg2://postgres:1212@localhost/company_sql')
engine.connect()
metadata = MetaData()

# •Создайте таблицу "employees" с полями: id (int, primary key), name (varchar), age (int), salary (int);
employees = Table('employees',metadata,
                      Column('id',Integer(),primary_key=True),
                      Column('name',String()),
                      Column('age',Integer()),
                      Column('salary',Integer())
                      )

# •Создайте таблицу "departments" с полями: id (int, primary key), name (varchar);
departments = Table('department',metadata,
                    Column('id',Integer(),primary_key=True),
                    Column('name',String())
                    )

metadata.create_all(engine)
conn = engine.connect()
conn.commit()

# •Вставите данные в таблицу "employees": (1, 'John', 25, 5000), (2, 'Alice', 30, 6000), (3, 'Bob', 35, 7000);
insert_employees_tabl = [
    {
        'name': 'John', 'age': '25', 'salary': '5000'
    },
    {
        'name': 'Alice', 'age': '30', 'salary': '6000'
    },
    {
        'name': 'Bob', 'age': '35', 'salary': '7000'
    }
]
# r = conn.execute(insert(employees),insert_employees_tabl)
# conn.commit()

# •Вставьте данные в таблицу "departments": (1, 'IT'), (2, 'HR');
insert_departments_tabl = [
    {
        'name': 'John', 'age': '25', 'salary': '5000'
    },
    {
        'name': 'Alice', 'age': '30', 'salary': '6000'
    },
    {
        'name': 'Bob', 'age': '35', 'salary': '7000'
    }
]
# r2 = conn.execute(insert(departments),insert_departments_tabl)
# conn.commit()


# 2) Создание связей между таблицами:
# •Добавить в таблицу "employees" поле "department_id" (int, foreign key references departments(id));
# •Обновить данные в таблице "employees" так, чтобы каждый сотрудник был привязан к отделу (1 - IT, 2 - HR);

# 3) Запросы:
# •Выведите все данные из таблицы "employees";
# •Выведите имена всех сотрудников, возраст которых больше 30;
# •Выведите имена всех сотрудников, у которых зарплата больше 6000;
# •Выведите имена сотрудников и названия отделов, в которых они работают;
# •Выведите имена сотрудников, возраст которых находится в диапазоне от 25 до 35;
# •Посчитайте количество сотрудников в каждом отделе;
# •Выведите имена всех сотрудников, чьи имена начинаются с буквы "A";
# •Выведите первые две записи из таблицы "employees";
# •Выведите имена всех сотрудников, у которых зарплата равна 7000;
# •Выведите имена всех сотрудников, у которых зарплата больше 5000 и возраст меньше 30;
# •Выведите имена всех сотрудников, у которых зарплата не равна 6000;
# •Выведите имена всех сотрудников, у которых возраст не находится в диапазоне от 25 до 35;
# •Удалите все данные из таблицы "employees";
# •Удалите таблицы "employees" и "departments".