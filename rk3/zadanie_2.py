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
    name = Column(VARCHAR(30))
    birthday = Column(Date)
    department = Column(VARCHAR(255))

def print_menu():
    print("1. Найти все отделы, в которых нет сотрудников моложе 25 лет")
    print("2. Найти сотрудника, который пришел сегодня на работу раньше всех")
    print("3. Найти сотрудников, опоздавших не менее 5-ти раз")

conn = psycopg2.connect(dbname='rk3', user='postgres', host='localhost', password='12345678')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()


engine = create_engine('postgresql+psycopg2://postgres:12345678@localhost:5432/rk3',
    execution_options={
        "isolation_level": "AUTOCOMMIT"
    })
DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

cmp = -1
while cmp != 0:
    print_menu()
    now = datetime.datetime.now()
    cmp = int(input("Ваш выбор: "))
    if cmp == 1:
        cursor.execute('''
        select department
        from workers
        where birthday < current_date - interval '25 years'
        group by department''')
        print(cursor.fetchall())

        '''for department, in session.query(Workers.name).filter((Workers.birthday - now) > 25):
            print(department)'''
        #query = session.query(Workers).filter(Workers.name == 'ed').order_by(Workers.id)
    elif cmp == 2:
        cursor.execute('''
        with worker_min(id, time)
        as(
            select id, min(timet) as time 
            from uchet
            where date = current_date
            group by id)
        select id
        from worker_min
        where time  = (
        select min(time) from worker_min)''')
        print(cursor.fetchall())

    elif cmp == 3:
        cursor.execute('''
                with latecomers(id, latetime)
                as(
                    select id, count(timet)
                    from(
                            select id, timet
	                        from uchet
	                        where type = 1 and timet > '09:00:00'
                            group by id, timet
                    ) as Lates
                    group by id)
                select name
                from workers
                where id = (select id from latecomers where latetime > 4)''')
        print(cursor.fetchall())
    elif cmp == 0:
        conn.commit()
        cursor.close()
    else:
        print("Некорректный ввод")