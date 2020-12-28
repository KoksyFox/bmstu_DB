import datetime
import psycopg2
from sqlalchemy import create_engine, Column, Integer, VARCHAR, Date, Time, ForeignKey
import sqlalchemy.dialects.postgresql.psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import current_date

DeclarativeBase = declarative_base()
class Worker(DeclarativeBase):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))
    birthday = Column(Date)
    department = Column(VARCHAR(255))

    def __repr__(self):
        return 'worker'


class Record(DeclarativeBase):
    __tablename__ = 'log'
    id = Column(Integer, autoincrement='auto', primary_key=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))
    date = Column(Date)
    weekday = Column(VARCHAR(255))
    time = Column(Time)
    action = Column(Integer)


def print_menu():
    print("------------На стороне БД---------------")
    print("1. Отделы, где нет сотрудников моложе 25")
    print("2. Сотрудник сегодня пришел раньше всех")
    print("3. Опоздал больше 5 раз за все время")
    print("-----------------ORM--------------------")
    print("4. Отделы, где нет сотрудников моложе 25")
    print("5. Сотрудник сегодня пришел раньше всех")
    print("6. Опоздал больше 5 раз за все время")


conn = psycopg2.connect(dbname='rk3', user='postgres', host='localhost', password='bmstu')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

engine = create_engine('postgresql+psycopg2://postgres:bmstu@localhost:5432/rzd',
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
        cursor.execute('''
select department
from workers
where birthday < current_date - interval '25 years'
group by department;
        ''')
        print(cursor.fetchall())
    elif ch == 2:
        cursor.execute('''
with min_worker(worker_id, time)
as (
    select worker_id, min(time) as time
    from log
    where date = current_date
    group by worker_id
)
select worker_id
from min_worker
where time = (select min(min_worker.time) from min_worker);
                ''')
        print(cursor.fetchall())
    elif ch == 3:
        cursor.execute('''
select worker_id
from (
select worker_id
from log
group by worker_id, date
having min(time) > '9:00') as date_later
group by worker_id
having count(*) >= 5
        ''')
        print(cursor.fetchall())
    elif ch == 4:
        deltatime = datetime.date(year=25, day=1, month=1)
        session.query('workers').filter(Worker.birthday < (datetime.datetime.date(datetime.datetime.today()) - deltatime))
        res = session.commit()
        print(res)
    elif ch == 5:
        pass
    elif ch == 6:
        pass
    elif ch == 0:
        conn.commit()
        cursor.close()
    else:
        print("Больной?")