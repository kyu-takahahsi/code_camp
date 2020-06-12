--11章
create database mydb;
--課題1
--character_table作成、データ挿入、表示
CREATE TABLE character_table(
    character_id INT(100),
    character_name VARCHAR(100),
    pref VARCHAR(10)
    );

INSERT INTO character_table(character_id, character_name, pref) VALUES (1, 'ふなっしー', '千葉県');
INSERT INTO character_table(character_id, character_name, pref) VALUES (2, 'ひこにゃん', '滋賀県');
INSERT INTO character_table(character_id, character_name, pref) VALUES (3, 'まりもっこり', '北海道');

SELECT *
FROM character_table;


--emp_table作成、データ挿入、表示
CREATE TABLE emp_table(
    emp_id INT(100),
    emp_name VARCHAR(100),
    job VARCHAR(100),
    age INT(100)
    );

INSERT INTO emp_table(emp_id, emp_name, job, age) VALUES (1, '山田太郎', 'manager', 50);
INSERT INTO emp_table(emp_id, emp_name, job, age) VALUES (2, '伊藤静香', 'manager', 45);
INSERT INTO emp_table(emp_id, emp_name, job, age) VALUES (3, '鈴木三郎', 'analyst', 30);
INSERT INTO emp_table(emp_id, emp_name, job, age) VALUES (4, '山田花子', 'clerk', 24);

SELECT *
FROM emp_table;


--課題2
--goods_table表示
SELECT *
FROM goods_table
WHERE price<=500;

--character_table表示
SELECT DISTINCT
       character_id,
       character_name
FROM character_table
WHERE pref LIKE "%県";

--emp_table表示
SELECT emp_id,
       age
FROM emp_table
WHERE job="clerk";

--emp_table表示
SELECT emp_id,
       emp_name
FROM emp_table
WHERE job="analyst" or age BETWEEN 20 AND 25;



--課題3
--emp_tableのemp_id1のjobをCTOに更新
UPDATE emp_table SET job = "CTO" WHERE emp_id = 1;

SELECT *
FROM emp_table;

--emp_tableのage>=40のレコードを削除
DELETE FROM emp_table WHERE age>=40;

SELECT *
FROM emp_table;

--13章
CREATE TABLE Bulletin_board(
    add_id INT(255),
    add_name VARCHAR(1000),
    add_comment VARCHAR(1000),
    add_time VARCHAR(1000)
    );

DELETE FROM Bulletin_board WHERE add_time = "GETDATE()";