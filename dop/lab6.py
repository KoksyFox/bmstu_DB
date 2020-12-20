import datetime

import psycopg2
from sqlalchemy import create_engine, Column, Integer, VARCHAR, Date
import sqlalchemy.dialects.postgresql.psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DeclarativeBase = declarative_base()
class Workers(DeclarativeBase):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    fio = Column(VARCHAR(255))
    birthday = Column(Date)
    otdel = Column(VARCHAR(255))

def print_menu():
    print("1. Найти отделы, в которых хоть один сотрудник опаздывает больше 3-х раз в неделю")
    print("2. Найти средний возраст сотрудников, не находящихся на рабочем месте 8 часов в день")
    print("3. Вывести все отделы и количество сотрудников опоздавших хоть раз")

conn = psycopg2.connect(dbname='rk3', user='postgres', host='localhost', password='12345678')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()


# подключение к ржд
engine = create_engine('postgresql+psycopg2://postgres:12345678@localhost:5432/rk3',
    execution_options={
        "isolation_level": "AUTOCOMMIT"
    })
DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

ch = -1
while ch != 0:
    print_menu()
    ch = int(input("Ваш выбор: "))
    if ch == 1:
        new_post = Workers(id=4, fio='Сидоров', birthday=datetime.date(day=26, month=4, year=1986), otdel='Бухгалтерия')
        session.add(new_post)
        session.commit()

        for post in session.query(Workers):
            print(post)

    elif ch == 2:
        print(session.query(Workers).filter(Workers.id == 1).one())
    elif ch == 3:
        pass
    elif ch == 0:
        conn.commit()
        cursor.close()
    else:
        print("Больной?")