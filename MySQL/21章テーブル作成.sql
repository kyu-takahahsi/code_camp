--社員情報テーブル：社員ID、名前、年齢、性別、写真ID、郵便番号、都道府県、住所、部署ID、入社日、退社日、更新日
CREATE TABLE emp_info_table(
    --emp_id INT AUTO_INCREMENT,
    emp_name VARCHAR(100),
    age INT(100),
    sex VARCHAR(100),
    image_id VARCHAR(100),
    post_code VARCHAR(100),
    pref VARCHAR(100),
    address VARCHAR(100),
    dept_id INT(100),
    join_date VARCHAR(100),
    retire_date VARCHAR(100),
    --update_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (emp_id)
);
SELECT info.emp_id as emp_id, emp_name, age, sex, pref, address, dept_id, join_date, retire_date, emp_image FROM emp_info_table as info JOIN emp_img_table as img ON info.emp_id = img.emp_id;
SELECT info.emp_id as emp_id, dept_name, emp_name, age, sex FROM emp_info_table as info JOIN dept_table ON info.dept_id = dept_table.dept_id;
SELECT emp_id, emp_name, age, sex, image_id post_code, pref, dept_id, join_date, retire_date. update_date FROM emp_info_table;

--社員画像テーブル：写真ID、画像パス、更新日
CREATE TABLE emp_img_table(
    image_id VARCHAR(100),
    emp_image VARCHAR(100),
    --update_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

--部署情報テーブル：部署ID、部署名、作成日、更新日
CREATE TABLE dept_table(
    --dept_id INT AUTO_INCREMENT,
    dept_name VARCHAR(100),
    --edit_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    --update_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (dept_id)
);

SELECT dept_id, dept_name FROM dept_table;

UPDATE emp_info_table SET emp_name = "山田 孝之", age = 35, sex = "男", post_code = "321-0989", pref = "東京", address = "山田市", dept_id = 14, join_date = "2001-02-03", retire_date = "在籍", update_date = LOCALTIME() WHERE emp_id = 14;

--部署ごとの人数カウント
SELECT dt.dept_id, dept_name, COUNT(DISTINCT dt.dept_id) as count FROM dept_table as dt JOIN emp_info_table as eit ON dt.dept_id = eit.dept_id GROUP BY dept_id;

--CSV出力
--SELECT * FROM emp_info_table INTO OUTFILE '/Users/kytakahashi/Downloads/プログラム/my_project/output/emp_info_table.csv' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';

--/usr/local/mysql/etc/my.cnf
--/etc/my.cnf /etc/mysql/my.cnf /usr/local/mysql/etc/my.cnf ~/.my.cnf