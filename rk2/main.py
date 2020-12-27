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
                DriverID integer not null unique check (DriverID > 0),
                DriverLicense integer unique ,
                FIO varchar(30),
                phone integer)''')

cursor.execute('''CREATE TABLE Cars(
                CarID integer not null unique check (CarID > 0),
                model varchar(30),
                color varchar (30),
                year varchar(30),
                registrationDate date)''')

cursor.execute('''CREATE TABLE Fines(
                FineID integer not null unique check (FineID > 0),
                DriverID integer not null check (DriverID > 0),
                FineType varchar(30),
                Amount integer,
                FineDate date)''')

cursor.execute('''CREATE TABLE DC(
                ID integer not null unique check (ID > 0),
                DriverID integer,
                CarID integer)''')

cursor.execute("INSERT INTO Drivers (DriverID, DriverLicense, FIO, phone) VALUES (1, 133, 'Ivanov Ivan Ivanovich', 9845)")
cursor.execute("INSERT INTO Drivers (DriverID, DriverLicense, FIO, phone) VALUES (2, 129, 'Olegov Oleg Olegovich', 9854)")
cursor.execute("INSERT INTO Drivers (DriverID, DriverLicense, FIO, phone) VALUES (3, 103, 'Kirillov Kirill Kirilovich', 8800)")
cursor.execute("INSERT INTO Drivers (DriverID, DriverLicense, FIO, phone) VALUES (4, 221, 'Dimov Dmitry Dmitrivich', 7654)")
cursor.execute("INSERT INTO Drivers (DriverID, DriverLicense, FIO, phone) VALUES (5, 098, 'Androv Andrey Ivanovich', 2323)")


cursor.execute("INSERT INTO Cars (CarID, model, color, year, registrationDate) VALUES (1, 'audi', 'red', '2017', '05-05-2020')")
cursor.execute("INSERT INTO Cars (CarID, model, color, year, registrationDate) VALUES (2, 'toyota', 'white', '2016', '05-05-2020')")
cursor.execute("INSERT INTO Cars (CarID, model, color, year, registrationDate) VALUES (3, 'reno', 'yellow', '2018', '02-04-2019')")
cursor.execute("INSERT INTO Cars (CarID, model, color, year, registrationDate) VALUES (4, 'audi', 'red', '2016', '05-07-2018')")
cursor.execute("INSERT INTO Cars (CarID, model, color, year, registrationDate) VALUES (5, 'hower', 'blue', '2013', '05-02-2020')")

cursor.execute("INSERT INTO Fines (FineID, DriverID, FineType, Amount, FineDate) VALUES (1, 2, 'type1', 2, '05-10-2020')")
cursor.execute("INSERT INTO Fines (FineID, DriverID, FineType, Amount, FineDate) VALUES (2, 2, 'type2', 1, '05-10-2020')")
cursor.execute("INSERT INTO Fines (FineID, DriverID, FineType, Amount, FineDate) VALUES (3, 4, 'type1', 12, '12-12-2019')")
cursor.execute("INSERT INTO Fines (FineID, DriverID, FineType, Amount, FineDate) VALUES (4, 3, 'type5', 2, '05-07-2020')")
cursor.execute("INSERT INTO Fines (FineID, DriverID, FineType, Amount, FineDate) VALUES (5, 4, 'type6', 1, '09-01-2020')")

cursor.execute("INSERT INTO DC (ID, DriverID, CarID) VALUES (1, 1, 1)")
cursor.execute("INSERT INTO DC (ID, DriverID, CarID) VALUES (2, 2, 3)")
cursor.execute("INSERT INTO DC (ID, DriverID, CarID) VALUES (3, 2, 4)")
cursor.execute("INSERT INTO DC (ID, DriverID, CarID) VALUES (4, 3, 2)")
cursor.execute("INSERT INTO DC (ID, DriverID, CarID) VALUES (5, 5, 5)")


conn.commit()
cursor.close()