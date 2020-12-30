



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