--многооператорная функция
--возвращается id посетителя, чей возраст больше возраста другого
create or replace function older(id1 int, id2 int) returns int as $$
declare
age1 int;
age2 int;
begin
    age1 = (select age from visitors where id = id1);
    age2 = (select age from visitors where id = id2);

    if age1 > age2 then
        return id1;
    else
        return id2;
    end if;
end;
$$ language plpgsql;

select *
from older(228, 773);