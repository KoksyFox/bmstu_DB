-- lab_05

-- 1. Из таблиц базы данных, созданной в первой лабораторной работе, извлечь
-- данные в XML (MSSQL) или JSON(Oracle, Postgres). Для выгрузки в XML
-- проверить все режимы конструкции FOR XML

copy (select ROW_TO_JSON(visitors) from visitors)
to 'C:/repositories/bmstu_DB/lab5/visitors.json';

-- 2. Выполнить загрузку и сохранение XML или JSON файла в таблицу.
-- Созданная таблица после всех манипуляций должна соответствовать таблице
-- базы данных, созданной в первой лабораторной работе.

drop table visitors_copy_help;
select *
from visitors_copy_help;

CREATE TEMP TABLE visitors_copy_help(doc JSON);
COPY visitors_copy_help FROM 'C:/repositories/bmstu_DB/lab5/visitors.json';

CREATE TABLE IF NOT EXISTS visitors_copy(LIKE visitors INCLUDING ALL);
INSERT INTO visitors_copy
SELECT v.*
FROM visitors_copy_help, json_populate_record(null::visitors, doc) AS v;



-- 3. Создать таблицу, в которой будет атрибут(-ы) с типом XML или JSON, или
-- добавить атрибут с типом XML или JSON к уже существующей таблице.
-- Заполнить атрибут правдоподобными данными с помощью команд INSERT
-- или UPDATE.


DROP TABLE visitors_copy;

CREATE TABLE visitors_copy (LIKE visitors INCLUDING ALL);

INSERT INTO visitors_copy
SELECT *
FROM visitors;

ALTER TABLE visitors_copy ADD COLUMN data_json JSON;

DROP TABLE visitors_json;

CREATE TEMP TABLE visitors_json(id SERIAL, doc JSON);
COPY visitors_json(doc) FROM 'C:/repositories/bmstu_DB/lab5/visitors.json';

UPDATE visitors_copy
SET data_json = (SELECT doc FROM visitors_json WHERE visitors_copy.id = visitors_json.id);

select * from visitors_copy;

-- 4. Выполнить следующие действия:

	-- 1. Извлечь XML/JSON фрагмент из XML/JSON документа

SELECT *
FROM json_extract_path('{"name": "Aleksandr", "CardId": "2213", "type":"gold", "Age":"23","validity":"2222-02-02"}',
                       'name');

	-- 2. Извлечь значения конкретных узлов или атрибутов XML/JSON
--документа

SELECT name, (data_json->>'age') AS age
FROM visitors_copy
WHERE data_json->>'age' = '23';

	-- 3. Выполнить проверку существования узла или атрибута

SELECT name, age, (data_json->>'Weight') AS weight
FROM visitors_copy
WHERE data_json::jsonb ? 'weight';

	-- 4. Изменить XML/JSON документ

UPDATE visitors_copy
SET data_json = data_json::jsonb - 'age';

select * from visitors_copy;

	--5. Разделить XML/JSON документ на несколько строк по узлам

SELECT *
FROM json_each_text('{"name": "Aleksandr", "CardId": "2213", "type":"gold", "Age":"23","validity":"2222-02-02"}');