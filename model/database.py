'''
import mysql.connector
from mysql.connector import errorcode
from model.const import DB
from model.item import Item

def get_db_cursor():
    cnx = mysql.connector.connect(
                    user=DB["DB_USER_NAME"],
                    password=DB["DB_PASSWORD"],
                    host=DB["DB_HOST"],
                    port=DB["DB_PORT"],
                    database=DB["DB_NAME"])
    return cnx, cnx.cursor()

def get_goods(order="ASC"):
    """
    goods_tableテーブルから商品を全て取得する。

    Returns
    -------
    goods_tableクラスのlist
    """
    goods = []

    try:
        cnx, cursor = get_db_cursor()

        if order != "ASC" and order != "DESC":
            order = "ASC"

        query = ("SELECT goods_id, goods_name, price FROM goods_table  ORDER BY price {}".format(order))
        cursor.execute(query)


        for (id, name, price) in cursor:
            item = Item(id, name, price)
            goods.append(item)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return goods
'''