--процедура с параметром
create or replace procedure age_match(inout is_match boolean) as $$
begin
    is_match = (select min(cnt.count) from (select count(*)
    over (partition by age)
    from visitors) as cnt) = 1;
end;
$$ language plpgsql;

call age_match(false);

--процедура с рекурсивным отв
--создаётся таблица посетителей с годом рождения
drop table tmp2;

select v.id, v.name, v.age
into tmp2
from visitors v
where id < 100
order by id;

alter table tmp2 drop column year;
alter table tmp2 add column year int;
create or replace procedure make_birthyear(i int) as $$
begin
    if i <= (select count(*) from tmp2) then
        update tmp2
        set year = Extract(year from current_date) - age
        where id = i;

        call make_birthyear(i+1);
    end if;
end;
$$ language plpgsql;

call make_birthyear(0);


--процедура с курсором
--выводит список абонементов одного зала в порядке срока действия
create or replace procedure print_list(gym_id int) as $$
declare
    list cursor for select * from abonements where abonements.idgym = gym_id order by validity;
    rec record;
begin
    raise notice 'Список абонементов зала № % ', gym_id;
    for rec in list loop
        raise notice 'id: %  validity: %', rec.id, rec.validity;
    end loop;
end
$$ language plpgsql;

call print_list(43);

--процедура с метаданными
--выводит количество таблиц в системе
create or replace procedure count_tables() as $$
declare cnt int;
begin
    cnt = (select count(*)
           from pg_tables
           where tableowner in (
               select usename
               from pg_user));

    raise notice 'In system % users tables', cnt;
end
$$ language plpgsql;

call count_tables();