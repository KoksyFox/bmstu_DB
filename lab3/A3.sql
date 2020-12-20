create function getpeople_mult(int) returns table
(
	id int,
	name varchar(30),
	age int
)
as
$$
	select id, name, age
	from visitors
	where age = $1;
$$ language sql;

select *, upper(name)
from getpeople_mult(18);