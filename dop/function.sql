create function getvisitorsAge(date) returns int
as
$$
	select count(ID)
	from uchet
	where datet = $1 and typet = 1 and timet > '09:00:00';
$$ language sql;

select *
from getvisitorsAge('14-12-2020');

drop function getvisitorsAge(date);