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

-- Идея добавить это как многооператорную функцию с аргументом айди зала
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
