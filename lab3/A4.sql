CREATE TABLE GymsHierarchy(
                ID int not null unique check (ID > 0),
                parent_id int)

INSERT INTO gymshierarchy
VALUES  (891, NULL),
       (342, 891),
       (525, 891),
       (895, 342),
    (124, 342),
    (912, 895),
    (432, 124)

WITH recursive LevelTable(parent_id, id, lvl)
AS
(
    SELECT parent_id, id, 0 as lvl
    FROM gymshierarchy
    WHERE parent_id IS NULL
    UNION ALL
    SELECT t1.parent_id, t1.id, t2.lvl + 1
    FROM gymshierarchy AS t1
    JOIN LevelTable as t2 ON t1.parent_id = t2.id
    )
SELECT *
FROM LevelTable ORDER BY lvl

create function recutsivefunc()