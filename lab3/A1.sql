-- скалярная функция
-- выводит количество клиентов, которым 25 лет
create function a1() returns varchar as
'
	select count(name)
	from visitors
	where age = 25
' language sql;


select a1();

drop function a1();