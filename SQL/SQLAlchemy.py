from datetime import datetime

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, Boolean, DateTime, ForeignKey

# # установка соединения с postgres
# connection = psycopg2.connect(user="postgres", password = "1212")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#
# # создаем курсор для выполнения операции с базой данных
# cursor = connection.cursor('create database sqlalchemy_tyt')
#
# # закрываем соединение
# cursor.close()
# connection.close()

engine = create_engine("postgresql+psycopg2://postgres:1212@localhost/sqlalchemy_tut")
engine.connect()
print(engine)

metadata = MetaData()

user = Table('users', metadata,
             Column('id',Integer(), primary_key=True),
             Column('user', String(200), nullable=False),
             )

blog = Table('blog', metadata,
             Column('id',Integer(), primary_key = True),
             Column('post_title',String(200),nullable=False),
             Column('post_slug',String(200), nullable=False),
             Column('content', Text(), nullable=False),
             Column('published',Boolean(), default=False),
             Column('created_on',DateTime(),default=datetime.now),
             Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now),

             )

posts = Table('posts',metadata,
              Column('id',Integer(),primary_key=True),
              Column('post_title',String(200),nullable=False),
              Column('post_slug',String(200), nullable=False),
              Column('content', Text(), nullable=False),
              Column('user_id',ForeignKey('users.id'))
              )

tags = Table('tags', metadata,
              Column('id',Integer(),primary_key=True),
              Column('tag',String(200),nullable=False),
              Column('tag_slug',String(200),nullable=False),
             )

post_tags = Table('post_tage', metadata,
              Column('post_id',ForeignKey('posts.id')),
              Column('tag_id',ForeignKey('tags.id')),
)


metadata.create_all(engine)

