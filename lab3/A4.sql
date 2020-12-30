--рекурсивное ОТВ
--возвращает количество залов на заданном уровне иерархии
create or replace function count_hierarchy(level int) returns int as $$
begin
    return
    (WITH recursive LevelTable(parent_id, id, lvl)
    AS
    (SELECT parent_id, id, 0 as lvl
    FROM gymshierarchy
    WHERE parent_id IS NULL
    UNION ALL
    SELECT t1.parent_id, t1.id, t2.lvl + 1
    FROM gymshierarchy AS t1
    JOIN LevelTable as t2 ON t1.parent_id = t2.id)

    select count(*)
    from LevelTable
    where lvl = level);
end;
$$ language plpgsql;

select count_hierarchy(2);


