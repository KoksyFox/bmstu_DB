-- скалярная функция
-- выводит количество клиентов, которым 25 лет
create or replace function a1(fage int) returns varchar as
'
	select count(name)
	from visitors
	where age = fage
' language sql;


select a1();


select name
from visitors
where age = 25;

drop function a1();