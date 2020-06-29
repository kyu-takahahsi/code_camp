--社員情報テーブル：社員ID、名前、年齢、性別、住所、部署ID、登録日、更新日
CREATE TABLE emp_info_table(
    --emp_id INT AUTO_INCREMENT,
    emp_name VARCHAR(100),
    age INT(100),
    sex VARCHAR(100),
    address VARCHAR(100),
    dept_id VARCHAR(100),
    join_date VARCHAR(100),
    retire_date VARCHAR(100),
    update_date VARCHAR(100),
    PRIMARY KEY (emp_id)
);


--社員画像テーブル：社員ID、名前、画像パス
CREATE TABLE emp_img_table(
    --emp_id INT AUTO_INCREMENT,
    emp_image VARCHAR(100),
    update_date VARCHAR(100),
    PRIMARY KEY (emp_id)
);

--部署情報テーブル：社員ID、部署名、部署ID
CREATE TABLE dept_table(
    --dept_id INT AUTO_INCREMENT,
    dept_name VARCHAR(100),
    edit_date VARCHAR(100),
    update_date VARCHAR(100),
    PRIMARY KEY (dept_id)
);

SELECT dept_id, dept_name FROM dept_table;
