--1. Инструкция SELECT, использующая предикат сравнения
--   Запрос выводит список посетителей женского пола, старше 25 лет и тип их абонемента:
    SELECT Visitors.name,Visitors.gender,Visitors.age, Abonements.type
    FROM Visitors JOIN Abonements ON Abonements.ID = Visitors.IDcard
    WHERE Visitors.gender = 'f' AND Visitors.age > 25;
-- Distinct - позволяет выбирать уникальные значения из бд

--2. Инструкция SELECT, использующая предикат BETWEEN
--    Выводит ID и тип абонементов  действие которых закончилось в ноябре 2020 года
    SELECT ID, type
    FROM Abonements
    WHERE validity BETWEEN '2020-11-01' AND '2020-11-30';
-- Предикат BETWEEN проверяет, попадают ли значения проверяемого выражения в диапазон,
-- задаваемый пограничными выражениями, соединяемыми служебным словом AND.

--3. Инструкция SELECT, использующая предикат LIKE:
--   Выводит список клиентов женсокго пола
    SELECT Visitors.name,Visitors.gender, Abonements.type
    FROM Visitors JOIN Abonements ON Abonements.ID = Visitors.IDcard
    WHERE Visitors.gender LIKE 'f';
--% - означает, что может быть один или несколько символов, а - только один символ или число

--4. Инструкция SELECT, использующая предикат IN с вложенным подзапросом
--Список абонементов типа 'platinum' использующихся в одном из залов с названием 'Mary'
SELECT ID, IDgym, type, validity
FROM Abonements
WHERE IDgym IN
(
 SELECT IDgym
 FROM Gyms
 WHERE name = 'Mary'
) AND type = 'platinum';
--Предикат IN определяет, будет ли значение проверяемого выражения обнаружено в наборе значений,
-- который либо явно определен, либо получен с помощью табличного подзапроса.


--5.Инструкция SELECT, использующая предикат EXISTS с вложенным подзапросом
--Список клиентов использующих карту типа gold

SELECT visitors.id, visitors.name
FROM visitors
where exists(
    SELECT visitors.id
    FROM visitors JOIN abonements
    ON visitors.idcard = abonements.id
    where abonements.type = 'gold'
          );
-- Предикат языка SQL EXISTS возвращает истину, когда по запросу найдена одна или более строк,
-- соответствующих условию, и ложь, когда не найдено ни одной строки.

--6. Инструкция SELECT, использующая предикат сравнения с квантором.????
--Список клиентов мужчин старше любой из женщин

SELECT id, name, gender, age
FROM visitors
where gender = 'm' and age > ALL(
    select age
    from visitors
    where gender = 'f'
    );

--7. Инструкция SELECT, использующая агрегатные функции в выражениях столбцов.
--Средний возраст всех посетителей
SELECT sum(age)/count(id) as "Average age"
FROM (
    SELECT age, id
    FROM visitors
    Group By age, id
 ) AS AvgAge;

-- count - количество входных строк, для которых значение выражения не равно NULL
-- sum - сумма значений выражения по всем входным данным, отличным от NULL

--8. Инструкция SELECT, использующая скалярные подзапросы в выражениях столбцов.

--Количество клиентов одного зала
SELECT IDgym, name, (
    SELECT count(id)
    FROM abonements
    where idgym = gyms.idgym
    ) AS Clients
FROM Gyms;

--9. Инструкция SELECT, использующая простое выражение CASE.
--В каком году заканчивается действие абонемента клиента

SELECT visitors.id, visitors.name,
    CASE Extract(year from validity)
        WHEN Extract(year from current_date) THEN 'This Year'
        WHEN Extract(year from current_date) - 1 THEN 'Last year'
        WHEN Extract(year from current_date) + 1 THEN 'Next year'
    END as "year of ending"
FROM visitors join abonements on idcard = abonements.id;
-- Функция EXTRACT извлекает отдельные части из даты или даты-времени.

--10. Инструкция SELECT, использующая поисковое выражение CASE.
--Заканчивается ли действие абонемента в этом месяце

SELECT visitors.id, visitors.name,
    CASE
        WHEN ((validity - current_date) > 0) and ((validity - current_date) <= 30) THEN 'In the next month'
        WHEN ((validity - current_date) > 0) and ((validity - current_date) > 30) THEN 'Not in the next month'
        WHEN (validity - current_date) < 0 THEN 'Earlier'
        WHEN (validity - current_date) = 0 THEN 'Today'
    END as "date of ending"
FROM visitors join abonements on idcard = abonements.id;


--11. Создание новой временной локальной таблицы из результирующего набора данных инструкции SELECT.
--Подтаблица клиентов старше 65

SELECT ID, name, age
INTO "Old clients"
FROM visitors
WHERE age >= 65;

--12. Инструкция SELECT, использующая вложенные коррелированные
--подзапросы в качестве производных таблиц в предложении FROM.
--Выводит список данных о клиентах старше 65, у которых действие абонемента заканчивается в ближайший месяц

select OldClients.id, name, age, idcard, validity
from abonements join (
    SELECT ID, idcard, name, age
    FROM visitors
    WHERE age >= 65
    ) as OldClients on idcard = abonements.id
where ((validity - current_date) > 0) and ((validity - current_date) < 30);

--13. Инструкция SELECT, использующая вложенные подзапросы с уровнем вложенности 3.
--Выводит список  посетителей зала с id = 144

select visitors.id, visitors.name, t.CardType, t.GymAddress
from (
     select type as CardType, GymAddress, id
    from (
         select address as GymAddress, idgym
        from gyms
        where idgym = 144
             ) as GT
    inner join abonements on Gt.idgym = abonements.idgym
         ) as T
inner join visitors on T.id = visitors.idcard;

--14. Инструкция SELECT, консолидирующая данные с помощью предложения GROUP BY, но без предложения HAVING.
--Для мужчин и женщин вывести средний возраст

SELECT gender, avg(age) as AvgAge
FROM visitors
GROUP BY gender;

--15. Инструкция SELECT, консолидирующая данные с помощью предложения GROUP BY и предложения HAVING.
--Запрос определяет у кого средний возраст больше у мужчин или женщин
SELECT gender, Avg(age) as AvgAge
FROM visitors
GROUP BY gender
HAVING Avg(age) <
(
    SELECT AVG(age) AS AvgAge
    FROM visitors
);
-- Команда HAVING позволяет фильтровать результат группировки, сделанной с помощью команды group by.

--16. Однострочная инструкция INSERT, выполняющая вставку в таблицу одной
--строки значений.
--Добавляет нового клиента:
INSERT into visitors (id, idcard, name, gender, age)
VALUES (1023, 2001, 'Alex', 'm', 25);


--17. Многострочная инструкция INSERT, выполняющая вставку в таблицу
--результирующего набора данных вложенного подзапроса.
--Заполняет таблицу данными о клиентах с платиновым абонементом

drop table PlatinumClients;
create table PlatinumClients (id int, idcard int, name varchar , gender char, age int);

INSERT into PlatinumClients (id, idcard, name, gender, age)
        select visitors.id, idcard, name, gender, age
        from visitors join abonements on abonements.id = visitors.idcard
        where abonements.type = 'platinum';

--18. Простая инструкция UPDATE.
--Добавляет к сроку работы абонемента 1 месяц
UPDATE abonements
SET validity = validity + interval '1 month';

--19. Инструкция UPDATE со скалярным подзапросом в предложении SET.
--Добавляет к сроку работы абонемента 1 месяц у клиентов фитнес центра с id=3
UPDATE abonements
SET validity =
(
SELECT validity+interval '1 month'
FROM abonements
WHERE abonements.idgym = 3
)
WHERE abonements.idgym = 3;

--20. Простая инструкция DELETE.
DELETE from visitors
where age > 80;

--21. Инструкция DELETE с вложенным коррелированным подзапросом в
--предложении WHERE.
--Удаляет из базы данных всех клиентов,у которых действие абонемента закончилось больше месяца назад
DELETE FROM visitors
WHERE idcard IN
(
 SELECT abonements.id
 FROM abonements
 WHERE (validity - current_date) < -30
 );

--22. Инструкция SELECT, использующая простое обобщенное табличное
--выражение
--Выводит средний возраст обладателей золотого абонемента
WITH ClientsIn (ClientID, age)
AS
(
 SELECT visitors.ID, age
 FROM visitors join abonements on abonements.id = visitors.idcard
 WHERE abonements.type = 'gold'
)
SELECT AVG(age) AS "Средней возраст обладателей золотого абонемента"
FROM ClientsIn;


--23. Инструкция SELECT, использующая рекурсивное обобщенное табличное
--выражение.
--Уровень иерархии залов
CREATE TABLE GymsHierarchy(
                ID int not null unique check (ID > 0),
                parent_id int);

INSERT INTO gymshierarchy
VALUES  (891, NULL),
       (342, 891),
       (525, 891),
       (895, 342),
    (124, 342),
    (912, 895),
    (432, 124);

WITH recursive LevelTable(parent_id, id, lvl)
AS
(
    SELECT parent_id, id, 0 as lvl
    FROM gymshierarchy
    WHERE parent_id IS NULL
    UNION ALL
    SELECT t1.parent_id, t1.id, t2.lvl + 1
    FROM gymshierarchy AS t1
    JOIN LevelTable as t2 ON t1.parent_id = t2.id
    )
SELECT *
FROM LevelTable ORDER BY lvl;

--24. Оконные функции. Использование конструкций MIN/MAX/AVG OVER()
-- Для каждой заданной группы продукта вывести среднее значение цены
--Выводит средний возраст мужчин и женщин сортирует по полу
SELECT id, name, gender, avg(age) over(partition by gender) as AvgAge
FROM visitors;

--25. Оконные фнкции для устранения дублей
--Придумать запрос, в результае которого в данных появляются полные дубли. Устранить
--дублирующиеся строки с использованием функции ROW_NUMBER()

drop table tmp1;

select a.idgym, gyms.name
into tmp1
from gyms join abonements a on gyms.idgym = a.idgym
order by a.idgym;

alter table tmp1 add column id int generated always as identity;

delete
from tmp1
where id in (
    select id
    from (
         select id,
            row_number() over (partition by tmp1.idgym) as n
        from tmp1
        ) as t
    where t.n > 1
    );

