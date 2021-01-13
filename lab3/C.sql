--триггер after
--при вставке значений в таблицу visitors, значения также вставляются в таблицу new_visitors
create table new_visitors(ID int generated always as identity primary key,
                name varchar(30) not null,
                IDcard int not null unique check (IDcard > 0),
                age integer check (age>=14 and age <=100));

create or replace function add_new_visitors() returns trigger as $$
begin
    insert into new_visitors(name, IDcard, age) values(new.name, new.Idcard, new.age);
    return new;
end;
$$ language plpgsql;

create trigger spy_visitors after insert on visitors for each row execute function add_new_visitors();

delete from visitors where id = 1;
insert into visitors(ID, IDcard, name, gender, age) values (1, 999, 'Ivanov', 'f', 23);


--триггер instead of
create view visitors_view as
select *
from visitors;

create or replace function increase_age() returns trigger as $$
begin
    update visitors_view
    set age = old.age + 10
    where id = old.id;
    return null;
end;
$$ language plpgsql;

create trigger no_delete instead of delete on visitors_view for each row execute function increase_age();

delete from visitors_view where id = 1;