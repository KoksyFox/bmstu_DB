--табличная функция
--возвращает таблицу с данными о посетителях заданного возраста
create or replace function getvisitors(findage int) returns table(
    ID int,
    IDcard int,
    name varchar,
    gender char,
    age integer
)
as
$$
begin
    return query
	select *
	from visitors
	where visitors.age = findage;
end;
$$ language 'plpgsql';

select *
from getvisitors(21);
