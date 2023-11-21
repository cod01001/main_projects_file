from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, ForeignKeyConstraint, Index, PrimaryKeyConstraint, UniqueConstraint

from sqlalchemy.orm import declarative_base
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from datetime import datetime

# connection = psycopg2.connect(user= 'postgres',password = '1212')
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#
# # Создаем курсор для выполнения операции с базы данных
# cursor = connection.cursor()
#
# # создаем базу данных "sqldz slide 50"
# sql_create_database_dz50 = "CREATE DATABASE batabase"
# cursor.execute(sql_create_database_dz50)
#
# # закрываем соединение
# cursor.close()
# connection.close()
# # ----------
#
#
# engine = create_engine('postgresql+psycopg2://postgres:1212@localhost/batabase')
# engine.connect()
# print(engine)
#
# metadata = MetaData()

Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:1212@localhost/batabase")
engine.connect()


class User(Base):
    __tablename__ = 'users' 
    id = Column(Integer)
    username = Column(String(100), nullable = False)
    email = Column(String(100), nullable = False)
    password = Column(String(200), nullable = False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        UniqueConstraint('username'),
        UniqueConstraint('email')
    )



class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    content = Column(String(50), nullable=False)
    pyblished = Column(String(200), nullable=False, default=False)
    user_id = Column(Integer(),nullable= False)
    created_on = Column(DateTime(), default=datetime.now())
    update_on = Column(DateTime, default=datetime.now, onupdate=datetime.now())
    __table_args__ = (
        ForeignKeyConstraint(['user_id'],['users.id']),
        Index('title_content_index' 'title', 'content'), #composit index on title and content
    )

Base.metadata.create_all(engine)



