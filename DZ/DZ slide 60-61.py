import decimal
from datetime import datetime

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    Text, Boolean, DateTime, ForeignKey, Numeric, CheckConstraint, insert, select, \
    asc, desc, update, delete, union, PrimaryKeyConstraint, UniqueConstraint, SmallInteger

from sqlalchemy.orm import declarative_base, Session, relationship

# --------------------------------------|
# # # создание базы в users sql
# # #установка соединения с postgres
# connection = psycopg2.connect(user= 'postgres',password = '1212')
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#
# # Создаем курсор для выполнения операции с базы данных
# cursor = connection.cursor()
#
# # создаем базу данных "slide_60-61"
# sql_create_database_slide_60_61 = "CREATE DATABASE slide_60_61"
# cursor.execute(sql_create_database_slide_60_61)
#
# # закрываем соединение
# cursor.close()
# connection.close()
# --------------------------------------|
Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:1212@localhost/slide_60_61')
engine.connect()
print(engine)

metadata = MetaData()


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer())


class Order_lines(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship('Items')


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now())
    line_items = relationship('Order_lines', backref='order')
    # def __str__(self):
    #     return f'{self.id} {self.customer_id} {self.date_placed}'



class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    # address = Column(String(200), nullable = False)
    # town = Column(String(50), nullable = False)
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now())
    orders = relationship('Orders', backref='customers')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


Base.metadata.create_all(engine)

session = Session(bind=engine)
c1 = Customers(
    first_name='Dima',
    last_name='Yastenko',
    username='Moseend',
    email='yandex'
)

c2 = Customers(
    first_name='Valeria',
    last_name='Gavrilova',
    username='Fyria',
    email='gmail'
)

# print(c1.first_name, c2.last_name)
# session.add(c1)
# session.add(c2)
# print(session.new)
# session.commit()


i1 = Items(name='Chair', cost_price=9.21, selling_price=21.81, quantity=1)
i2 = Items(name='Chair1', cost_price=11.21, selling_price=22.81, quantity=2)
i3 = Items(name='Chair2', cost_price=12.21, selling_price=23.81, quantity=3)
i4 = Items(name='Chair3', cost_price=13.21, selling_price=24.81, quantity=4)
i5 = Items(name='Chair4', cost_price=14.21, selling_price=25.81, quantity=5)
i6 = Items(name='Chair5', cost_price=15.21, selling_price=26.81, quantity=6)
i7 = Items(name='Chair6', cost_price=16.21, selling_price=27.81, quantity=7)
i8 = Items(name='Chair7', cost_price=17.21, selling_price=28.81, quantity=8)

o1 = Orders(customers=c1)
o2 = Orders(customers=c1)

line_item1 = Order_lines(order=o1, item=i1, quantity=3)
line_item2 = Order_lines(order=o1, item=i2, quantity=2)
line_item3 = Order_lines(order=o2, item=i1, quantity=1)
line_item4 = Order_lines(order=o2, item=i2, quantity=4)

# session.add_all([o1, o2])

o3 = Orders(customers=c1)
orderline1 = Order_lines(item=i1, quantity=5)
orderline2 = Order_lines(item=i2, quantity=10)

o3.line_items.append(orderline1)
o3.line_items.append(orderline2)
# session.add_all([o3, ])

# print('все записи из таблицы customers')
# print(session.query(Customers).all())


# q = session.query(Customers)
# for c in q:
#     print(c)
# print(session.query(Customers.id, Customers.first_name).all())

# print(session.query(Items).count())

# print(session.query(Orders).first())

# print(session.get(Customers, 1))

# print(session.query(Customers).filter(Customers.first_name == 'Dima').all())


a = session.query(Customers).join(Orders).all()

for i in a:
    print(i)

# print(c1.first_name, c2.last_name)
# session.add(c1)
# session.add(c2)
# print(session.new)
session.commit()
