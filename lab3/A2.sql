create function getvisitors(int) returns visitors as
$$
	select *
	from visitors
	where age = $1;
$$ language sql;

select *
from getvisitors(18);

drop function getvisitors(int)