import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(dbname='postgres', user='postgres', host='localhost', password='12345678')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()
cursor.execute("DROP DATABASE rk3")
cursor.execute("CREATE DATABASE rk3")
conn.commit()
cursor.close()

conn = psycopg2.connect(dbname='rk3', user='postgres', host='localhost', password='12345678')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE Uchet(
                ID integer not null check (ID > 0),
                Date date,
                DayOfWeek varchar(30),
                Timet time,
                Type integer)''')

cursor.execute('''CREATE TABLE Workers(
                ID integer not null unique check (ID > 0),
                name varchar(30),
                Birthday date,
                department varchar(30))''')


cursor.execute("INSERT INTO Uchet (ID, Date, DayOfWeek, Timet, Type) VALUES (1, '14-12-2020', 'Monday', '09:01:00', 1)")
cursor.execute("INSERT INTO Uchet (ID, Date, DayOfWeek, Timet, Type) VALUES (2, '14-12-2020', 'Monday', '09:20:00' , 1)")
cursor.execute("INSERT INTO Uchet (ID, Date, DayOfWeek, Timet, Type) VALUES (3, '14-12-2020', 'Monday', '09:01:00' , 1)")
cursor.execute("INSERT INTO Uchet (ID, Date, DayOfWeek, Timet, Type) VALUES (2, '17-12-2020', 'Thursday', '09:00:00' , 1)")
cursor.execute("INSERT INTO Uchet (ID, Date, DayOfWeek, Timet, Type) VALUES (3, '17-12-2020', 'Thursday', '09:00:00' , 1)")
cursor.execute("INSERT INTO Uchet (ID, Date, DayOfWeek, Timet, Type) VALUES (1, '19-12-2020', 'Monday', '08:58:00', 1)")
cursor.execute("INSERT INTO Uchet (ID, Date, DayOfWeek, Timet, Type) VALUES (2, '19-12-2020', 'Monday', '09:20:00' , 1)")
cursor.execute("INSERT INTO Uchet (ID, Date, DayOfWeek, Timet, Type) VALUES (3, '19-12-2020', 'Monday', '09:01:00' , 1)")
cursor.execute("INSERT INTO Uchet (ID, Date, DayOfWeek, Timet, Type) VALUES (2, '16-12-2020', 'Monday', '09:20:00' , 1)")
cursor.execute("INSERT INTO Uchet (ID, Date, DayOfWeek, Timet, Type) VALUES (2, '15-12-2020', 'Monday', '09:20:00' , 1)")
cursor.execute("INSERT INTO Uchet (ID, Date, DayOfWeek, Timet, Type) VALUES (2, '13-12-2020', 'Monday', '09:20:00' , 1)")


cursor.execute("INSERT INTO Workers (ID, name, Birthday, department) VALUES (1, 'Ivan Ivanovich Ivanov', '09-01-1992', '#2')")
cursor.execute("INSERT INTO Workers (ID, name, Birthday, department) VALUES (2, 'Ivan Ivanovich Dimov', '20-11-1990', '#2')")
cursor.execute("INSERT INTO Workers (ID, name, Birthday, department) VALUES (3, 'Ivan Ivanovich Kirov', '09-01-1999', '#3')")



conn.commit()
cursor.close()