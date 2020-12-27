import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(dbname='postgres', user='postgres', host='localhost', password='12345678')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()
cursor.execute("DROP DATABASE rk2")
cursor.execute("CREATE DATABASE rk2")
conn.commit()
cursor.close()

conn = psycopg2.connect(dbname='rk2', user='postgres', host='localhost', password='12345678')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE Drivers(
                ID integer not null unique check (ID > 0),
                identnum integer,
                phone integer,
                FIO varchar(30),
                auto varchar(30))''')

cursor.execute('''CREATE TABLE Cars(
                ID integer not null unique check (ID > 0),
                mark varchar(30),
                model varchar(30),
                releaseDate varchar(30),
                registrationDate varchar(30),
                DriverID integer)''')

cursor.execute('''CREATE TABLE Bills(
                ID integer not null unique check (ID > 0),
                typeof varchar(30),
                penalty integer,
                warning varchar(30))''')

cursor.execute('''CREATE TABLE DB(
                ID integer not null unique check (ID > 0),
                DriverId integer,
                BillID integer)''')

cursor.execute("INSERT INTO Drivers (ID, identnum, phone, FIO, auto) VALUES (1, 133, 8345, 'Ivanov Ivan Ivanovich', 2)")
cursor.execute("INSERT INTO Drivers (ID, identnum, phone, FIO, auto) VALUES (2, 129, 7695, 'Olegov Oleg Olegovich', 3)")
cursor.execute("INSERT INTO Drivers (ID, identnum, phone, FIO, auto) VALUES (3, 103, 7915, 'Kirillov Kirill Kirilovich', 1)")
cursor.execute("INSERT INTO Drivers (ID, identnum, phone, FIO, auto) VALUES (4, 221, 8916, 'Dimov Dmitry Dmitrivich', 4)")
cursor.execute("INSERT INTO Drivers (ID, identnum, phone, FIO, auto) VALUES (5, 098, 7495, 'Androv Andrey Ivanovich', 5)")


cursor.execute("INSERT INTO Cars (ID, mark, model, releaseDate, registrationDate, DriverID) VALUES (1, 'audi', 'c23', '05-10-2019', '05-05-2020', 3)")
cursor.execute("INSERT INTO Cars (ID, mark, model, releaseDate, registrationDate, DriverID) VALUES (2, 'toyt', 'y212', '05-10-2019', '05-05-2020', 1)")
cursor.execute("INSERT INTO Cars (ID, mark, model, releaseDate, registrationDate, DriverID) VALUES (3, 'dali', 'g12', '02-05-2019', '05-04-2020', 2)")
cursor.execute("INSERT INTO Cars (ID, mark, model, releaseDate, registrationDate, DriverID) VALUES (4, 'audi', '03', '05-03-2018', '05-07-2020', 4)")
cursor.execute("INSERT INTO Cars (ID, mark, model, releaseDate, registrationDate, DriverID) VALUES (5, 'dar', '12', '05-10-2016', '05-02-2020', 5)")

cursor.execute("INSERT INTO Bills (ID, typeof, penalty, warning) VALUES (1, 'type1', 100, 'war1')")
cursor.execute("INSERT INTO Bills (ID, typeof, penalty, warning) VALUES (2, 'type2', 14, 'war1')")
cursor.execute("INSERT INTO Bills (ID, typeof, penalty, warning) VALUES (3, 'type1', 12, 'war12')")
cursor.execute("INSERT INTO Bills (ID, typeof, penalty, warning) VALUES (4, 'type5', 2, 'war132')")
cursor.execute("INSERT INTO Bills (ID, typeof, penalty, warning) VALUES (5, 'type6', 54, 'war113')")

cursor.execute("INSERT INTO DB (ID, DriverID, BillID) VALUES (1, 2, 3)")
cursor.execute("INSERT INTO DB (ID, DriverID, BillID) VALUES (2, 2, 1)")
cursor.execute("INSERT INTO DB (ID, DriverID, BillID) VALUES (3, 4, 2)")
cursor.execute("INSERT INTO DB (ID, DriverID, BillID) VALUES (4, 5, 4)")
cursor.execute("INSERT INTO DB (ID, DriverID, BillID) VALUES (5, 5, 1)")
cursor.execute("INSERT INTO DB (ID, DriverID, BillID) VALUES (6, 3, 1)")


conn.commit()
cursor.close()