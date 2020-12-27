-- Инструкция SELECT, использующая предикат сравнения с квантором.
-- Выводит список машин старше любой из красных машин
select CarId, model
from cars
where year < ALL (
    select year
    from cars
    where color = 'red'
    )

-- Инструкция SELECT, использующая скалярные подзапросы в выражениях столбцов.
-- Запрос выводит количество машин у каждого водителя
Select DriverID, FIO,(
    select count(CarID)
    FROM DC
    where dc.driverid = Drivers.DriverID
) as Cars
From Drivers

--Инструкция SELECT, консолидирующая данные с помощью предложения GROUP BY и
--предложения HAVING.
-- Выводит выводит типы штрафов, среднее количество которых больше общего среднего количества штрафов
select FineType, AVG(amount)
from fines
group by FineType
having avg(amount) >
       (
           select avg(Amount)
           from fines
        )
