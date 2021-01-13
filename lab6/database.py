import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class DataBase:
    def __init__(self):
        self.connect = psycopg2.connect(dbname='fitness', user='postgres',
                                        password='12345678', host='localhost')
        self.connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connect.cursor()

# Количество посетителей мужского пола
    def get_number_of_male_visitors(self):
        self.cursor.execute('''
            select count(name)
            from visitors
            where gender = 'm' ''')
        return self.cursor.fetchall()

# Выводит информацию о всех пользователях: имя, возраст, тип карты, название зала
    def select_all_inf(self):
        self.cursor.execute('''
            select v.name, age, type, ag.name 
            from 
            (abonements join
            gyms on abonements.idgym = gyms.idgym) as ag
            join visitors v on v.idcard = ag.id''')
        return self.cursor.fetchall()

# Выводит средний возраст пользователей абонементов каждого типа
    def select_cte_window(self):
        self.cursor.execute('''
            WITH CTE
            AS (
                select a.type,
                avg(v.age) over(partition by a.type) as AvgAge
                from visitors v join abonements a on v.idcard = a.id)
            SELECT type, AvgAge
            FROM CTE
            GROUP BY type, AvgAge''')
        return self.cursor.fetchall()

# Выводит информацию о таблицах лежащих в public
    def select_metadata(self):
        self.cursor.execute('''
            SELECT table_name, table_type
            FROM information_schema.tables
            WHERE table_schema = 'public'
        ''' )
        return self.cursor.fetchall()

# скалярная функция возвращает количество посетителей данного возраста
    def scalar_func(self, data):
        self.cursor.callproc('a1', [data])
        return self.cursor.fetchall()

# табличаня функция возвращает инфу о посетителях с заданным возрастом
    def table_func(self, data):
        self.cursor.callproc('getvisitors', [data])
        return self.cursor.fetchall()

    def proc(self):
        self.cursor.execute('call age_match(False)')
        return self.cursor.fetchall()

# Возвращает версию
    def version(self):
        self.cursor.callproc('version')
        return self.cursor.fetchall()

# Создаёт таблицу
    def create_table(self, name):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS {name}
            (
                id          SERIAL  PRIMARY KEY,
                name        VARCHAR(30) NOT NULL,
                cost        INTEGER NOT NULL
            )
            '''.format(name = name))
        print('Table {name} successfully created\n'.format(name=name))

# Добавляет данные в новую таблицу
    def insert_data(self, table, name, cost):
        self.cursor.execute('''
            insert into {table} (name, cost) 
            values (%s, %s)
            '''.format(table = table), [name, cost])
        print('Insert into {table} successfully\n'.format(table = table))
        