create function getvisitors(int) returns table(
    ID int,
    IDcard int,
    name varchar,
    gender char,
    age integer
                                              )
as
$$
	select *
	from visitors
	where age = $1;
$$ language sql;

select *
from getvisitors(19);

drop function getvisitors(int)