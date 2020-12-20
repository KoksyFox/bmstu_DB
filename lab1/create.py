import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# создание базы
conn = psycopg2.connect(dbname='postgres', user='postgres', host='localhost', password='12345678')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()
cursor.execute("DROP DATABASE fitness")
cursor.execute("CREATE DATABASE fitness")

conn.commit()
cursor.close()

# подключение
conn = psycopg2.connect(dbname='fitness', user='postgres', host='localhost', password='12345678')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE Visitors(
                ID int not null unique check (ID > 0),
                IDcard int not null unique check (IDcard > 0),
                name varchar(30) not null,
                sex char,
                age integer check (age>=14 and age <=100))''')

cursor.execute('''CREATE TABLE Abonements(
                ID int not null unique check (ID > 0),
                IDgym int not null unique check(ID > 0),
                type varchar(20),
                validity varchar(50))''')

cursor.execute('''CREATE TABLE Gyms(
                IDgym int not null unique check(IDgym > 0),
                name varchar(20),
                address varchar(50))''')

cursor.execute('''alter table Visitors add constraint name check(name ~*'^[a-z]+$')''')
conn.commit()

cursor.execute(''' copy Visitors from 'C:/repositories/bmstu_DB/lab1/people.csv' delimiter ',' csv''')

cursor.execute(''' copy Abonements from 'C:/repositories/bmstu_DB/lab1/cards.csv' delimiter ',' csv''')

cursor.execute(''' copy Gyms from 'C:/repositories/bmstu_DB/lab1/gyms.csv' delimiter ',' csv''')

conn.commit()

'''f = open("people.csv")
for s in f.readlines():
    a = s.split(',')
    cursor.execute("INSERT INTO Visitors (ID, IDcard, name, sex, age) VALUES (%s, %s, %s, %s, %s)", (a[0], a[1], a[2], a[3], a[4]))
f.close()'''

'''f = open("cards.csv")
for s in f.readlines():
    a = s.split(',')
    cursor.execute("INSERT INTO Abonements (ID, IDgym, type, validity) VALUES (%s, %s, %s, %s)", (a[0], a[1], a[2], a[3]))
f.close()

f = open("gyms.csv")
for s in f.readlines():
    a = s.split(',')
    cursor.execute("INSERT INTO Gyms (IDgym, name, address) VALUES (%s, %s, %s)", (a[0], a[1], a[2]))
f.close()'''

conn.commit()
cursor.close()