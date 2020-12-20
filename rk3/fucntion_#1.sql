--Написать табличную функцию, возвращающую статистику на сколько и кто опоздал в
--определенную дату. Дату вводить с клавиатуры

create function GetLatecomers(date) returns table
(
    latetime time,
    quantity int
)
as
$$
    select (timet - '09:00:00') , count(ID)
    from(
        select timet, id
	    from uchet
	    where Date = $1 and type = 1 and timet > '09:00:00'
        group by id,timet
        ) as Latecomers
    group by timet

$$ language sql;

select *
from GetLatecomers('14-12-2020');

drop function GetLatecomers(date);