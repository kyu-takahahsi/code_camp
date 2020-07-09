from flask import Flask, render_template, request, make_response, session, flash, redirect, url_for
app = Flask(__name__)
#HTMLに反映
#from flask import render_template
#HTMLから抽出
#from flask import request
#cookie
#from flask import make_response
#session
#from flask import session
#ランダム選択
import random
#データベース操作
import mysql.connector
from mysql.connector import errorcode
#正規表現
import re
#時間取得
import datetime
#画像保存のため
import os
#from PIL import Image
#画像保存のため
from werkzeug.utils import secure_filename
#ランダムな文字列作成
import string
#7章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
#/がアドレスの最後につく
@app.route("/")
def index():
    return "Index Page"

/helloがアドレスの最後につく
@app.route("/hello")
def hello():
    return "Hello, World"
"""

#8章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return "User {}".format(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return "Post {}".format(post_id)

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return "Subpath {}".format(subpath)
"""

#9章ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
@app.route('/hello')
def hello():
    return render_template('hello.html', name="コード太郎")

#nameのなかがnameならばHello,nameと表示され、それ以外ならばHello,worldと表示される
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#usersのなかのものを一つずつ表示する
@app.route('/users')
def show_users():
    users = ["太郎", "花子", "一浪"]
    return render_template('users.html', users=users)
"""

#10章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
GETは、検索結果を表すページなどに使います。
http://www.google.co.jp/search?q=codecamp のように、GETを使ってリクエストパラメータをURLに含めると、検索結果の一覧が出ているページをブックマーク可能
ブラウザのキャッシュ機能により、2回目以降は高速表示が可能という利点があります。
POSTはユーザ名やパスワードなど秘匿性の高い情報を送信する際を代表に、セキュリティの観点から利用します。
なおPOSTを利用したからセキュリティに問題がないわけではなく、GETよりはリスクが軽減されるだけで、セキュリティ対策は別途必要となります。
この2つの使い分けとして、GETを使う明確なメリットがある場合以外は、基本的にPOSTを利用します。

#名前を入力するフォームのためのもの
@app.route("/send")
def send():
    return render_template('send.html')

@app.route("/receive", methods=["GET"])
def receive():
    if "my_name" in request.args.keys() :
        return "ここに入力した名前を表示： {}".format(request.args["my_name"])
    else:
        return "名前が未入力です"

#GET
@app.route("/get_sample")
def get_sample():
    return render_template('get_sample.html', query=request.args["query"] )

#POST
@app.route("/post_sample", methods=["GET"])
def sample(gender=""):
    return render_template('post_sample.html', gender=gender)

@app.route("/post_sample", methods=["POST"])
def post_sample():
"""

#10章課題1
"""
#kadai1のHTMLに反映
@app.route("/kadai1")
def send_name():
    return render_template('kadai1.html')

#入力された名前、性別、チェックを送信
@app.route("/kadai1", methods=["GET"])
def kadai1_post(name="", gender="", mail=""):
    return render_template('kadai1.html', name=name, gender=gender, mail=mail)

#入力された名前、性別、チェックを受信
@app.route("/kadai1", methods=["POST"])
def post_name():
    name = request.form.get("name","")
    gender = request.form.get("gender","")
    mail = request.form.get("mail","")
    return kadai1_post(name,gender,mail)
"""


#10章課題2
"""
#kadai2_send.htmlで送信
@app.route("/kadai2_send")
def kadai2_send():
    return render_template('kadai2_send.html')

#kadai2_recieve.htmlで受信
@app.route("/kadai2_recieve", methods=["POST"])
def kadai2_receive():
    #nameが""以外ならばようこそnameさんと表示、""ならば名前が未入力ですと表示
    if request.form["name"] != "" :
        return "ようこそ" + request.form["name"] + "さん"
    else:
        return "名前が未入力です"
"""

"""
ー試行錯誤ー
@app.route("/kadai2_send")
def kadai2_send(name=""):
    name = request.form.get("name", "")
    return render_template('kadai2_send.html', name=name)

@app.route("/kadai2_recieve", methods=["POST"])
def kadai2_recieve(name):
    return kadai2_send(name)

@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
   if request.method == 'POST':
      result = request.form
      return render_template("confirm.html",result = result)
"""


#10章課題3
"""
#チェックされたハンドを送信
@app.route("/kadai3", methods=["GET"])
def kadai3_post(my_hand="", your_hand="", result=""):
    return render_template('kadai3.html', my_hand=my_hand, your_hand=your_hand, result=result)

#チェックされたハンドと相手のハンドを比較して勝敗を表示
@app.route("/kadai3", methods=["POST"])
def post():
    my_hand = request.form.get("my_hand", "")
    your_hand = random.choice(("グー", "チョキ", "パー"))
    if my_hand == your_hand:
        result = "Draw"
    elif (my_hand == "グー" and your_hand == "パー") or (my_hand == "チョキ" and your_hand == "グー") or (my_hand == "パー" and your_hand == "チョキ"):
        result = "Lose"
    else:
        result = "Win"
    return kadai3_post(my_hand, your_hand, result)
"""


#12章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
#例
@app.route("/mysql_select")
def mysql_select():
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'kaA1ybB2ucC3d2c'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名

    goods = []
    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()
        query = 'SELECT goods_id, goods_name, price FROM goods_table'
        cursor.execute(query)

        for (id, name, price) in cursor:
            item = {"goods_id":id, "goods_name":name, "price":price}
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
    return render_template("goods.html", goods = goods)
"""

"""
@app.route("/mysql_sample")
def mysql_sample():
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'kaA1ybB2ucC3d2c'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名

    order = ""
    if "order" in request.args.keys() :
            order = request.args.get("order")

    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()

        query = 'SELECT goods_name, price FROM goods_table ORDER BY price ' + order
        cursor.execute(query)
        goods = []
        for (name, price) in cursor:
            item = {"name": name, "price":price}
            goods.append(item)
        params = {
        "asc_check" : order == "ASC",
        "desc_check" : order == "DESC",
        "goods" : goods
        }
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return render_template("goods.html", **params)
"""

"""
@app.route("/mysql_change")
def mysql_change():
    # import部分は省略
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'kaA1ybB2ucC3d2c'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名

    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()
        query = "INSERT INTO goods_table(goods_name, price) VALUES('ボールペン', 80)"
        cursor.execute(query)
        cnx.commit() # この処理が無いと変更が反映されません！

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return "終了"
"""

#12章課題1
"""
@app.route("/mysql_kadai")
def challenge_mysql_select():
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'kaA1ybB2ucC3d2c'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名

    order = ""
    if "order" in request.args.keys():
            order = request.args.get("order")

    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()

        if order == "":
            query = "select * from emp_table;"
        else:
            query = f"select * from emp_table where job = '{order}' order; "
        print(query)

        cursor.execute(query)
        jobs = []
        for (emp_id, emp_name, job, age ) in cursor:
            item = { "emp_id": emp_id, "emp_name": emp_name, "job": job, "age": age}
            jobs.append(item)

        params = {
        "all_check" : order == "",
        "manager_check" : order == "manager",
        "analyst_check" : order == "analyst",
        "clerk_check" : order == "clerk",
        "jobs" : jobs
        }

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return render_template("goods.html", **params)
"""

#12章課題2
"""
@app.route("/mysql_kadai")
def mysql_sample():
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'kaA1ybB2ucC3d2c'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名

    add_name = ""
    add_price = ""
    judge = ""

    #空欄に値が入力されていたら取得
    if "add_name" in request.args.keys() and "add_price" in request.args.keys():
        add_name = request.args.get("add_name")
        add_price = request.args.get("add_price")
        print("値：入っています")

    #空欄のままなら何もしない
    else:
        print("値：入っていません")


    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()

        #どんな場合でも実行するSQL
        query = 'SELECT goods_name, price FROM goods_table'

        #空欄の場合
        if add_name == "" and add_price =="":
            cursor.execute(query)
            judge = "追加したい商品の名前と価格を入力してください"
            print("SQL:値が入っていないので実行できません")

        #条件通りadd_nameが文字列、add_priceが数字の場合
        elif (add_name.isdecimal() != True) and (add_price.isdecimal()== True):
            add_query = f"INSERT INTO goods_table (goods_name, price) VALUES ('{add_name}', '{add_price}')"
            cursor.execute(add_query)
            cnx.commit()
            cursor.execute(query)
            judge = "追加成功"
            print("商品：追加完了")

        #条件に当てはまらない場合
        else:
            cursor.execute(query)
            judge = "追加失敗"
            print("商品：追加失敗")


        goods = []
        for (name, price) in cursor:
            item = {"name": name, "price":price}
            goods.append(item)

        params = {
        "judge" : judge,
        "goods" : goods
        }

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return render_template("goods_add.html", **params)
"""

#13章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
@app.route("/Bulletin_board", methods=['GET', 'POST'])
def mysql_sample():
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'kaA1ybB2ucC3d2c'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名

    #htmlから受け取る変数
    add_name = ""
    add_comment = ""
    search_name = ""
    #paramsで送る表示するための変数
    message = ""
    #エラー内容表示
    judge = ""
    #コメント数表示
    comment_count = 0

    #空欄に値が入力されていたら取得
    if "add_name" in request.form.keys() and "add_comment" in request.form.keys():
        add_name = request.form.get("add_name")
        add_comment = request.form.get("add_comment")


    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()
        #検索する時に場合に実行するSQL
        query = "SELECT add_name, add_comment, add_time FROM Bulletin_board ORDER BY add_time DESC"


        #全てが空欄の場合
        if add_name == "" and add_comment == "" and search_name == "":
            judge = "発言なら名前とコメント、 検索なら名前を入力してください"

        #条件通りadd_nameが20文字以内、add_commentが100文字以内の場合
        if  1 <= len(add_name) <= 20 and 1 <= len(add_comment) <=100:
            add_query = f"INSERT INTO Bulletin_board (add_name, add_comment, add_time) VALUES ('{add_name}', '{add_comment}', LOCALTIME())"
            cursor.execute(add_query)
            cnx.commit()
            judge = "追加成功：コメントが正常に追加されました"

        #エラーになる場合
        else:
            #コメントが空欄の場合
            if add_name == "":
                judge = "追加失敗：名前を入力してください"

            #名前が空欄の場合
            elif add_comment == "":
                judge = "追加失敗：コメントを入力してください"

            #名前とコメントが条件に合わない場合
            elif len(add_name) > 20 and len(add_comment) > 100:
                judge = "追加失敗：20文字以内で名前を、100文字以内コメントを入力してください"

            #コメントが条件に合わない場合
            elif len(add_comment) > 100:
                judge = "追加失敗：100文字以内コメントを入力してください"

            #名前が条件に合わない場合
            elif len(add_name) > 20:
                judge = "追加失敗：20文字以内で名前を入力してください"

        #検索欄に値が入力されていたら取得
        if "search_name" in request.form.keys():
            search_name = request.form.get("search_name")
            if search_name != "":
                query = f"SELECT add_name, add_comment, add_time FROM Bulletin_board WHERE add_name = '{search_name}' ORDER BY add_time DESC"
                judge = "検索結果"


        #コメントを表示するSQL
        cursor.execute(query)

        message = []
        for (name, comment, time) in cursor:
            item = {"name": name, "comment" : comment, "time" : time}
            message.append(item)
            comment_count +=1

        params = {
        "judge" : judge,
        "message" : message
        }

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return render_template("Bulletin_board.html", comment_count=comment_count, **params)
"""

#14章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
@app.route("/regrep", methods=['GET', 'POST'])
def regrep():
    message = ""
    phone_number = ""
    if "phone_number" in request.form.keys():
        phone_number = request.form["phone_number"]

        if len(phone_number)==0 :
            message =  '携帯電話番号を入力してください。'
        elif re.match('^[0-9]{3}-[0-9]{4}-[0-9]{4}$', phone_number):
           message = 'あなたの携帯電話番号は「' + phone_number + '」です'
        else:
            message = '形式が違います。xxx-xxxx-xxxxの形式の数値で入力してください'

    return render_template('regrep.html', phone_number=phone_number, message=message)
"""

#14章課題
"""
@app.route("/regist_form", methods=['GET', 'POST'])
def regrep():
    message = ""
    mail = ""
    password = ""

    #もし値が入力されていれば値を変数に代入
    if "mail" in request.form.keys() and "password" in request.form.keys():
        mail = request.form["mail"]
        password = request.form["password"]

    #入力された形式が正しい([0-9]：半角数字、\d：全角)
    if re.search(r'[0-9a-z]@[a-z]', mail) and re.fullmatch(r'[0-9a-z]{6,18}', password):
       message = '登録完了'
    #フォームが両方とも空欄
    elif len(mail)==0 and len(password)==0:
        message =  'メールアドレスとパスワードを入力してください。'
    #フォームのメールアドレスが空欄
    elif len(mail)==0 :
        message =  'メールアドレスを入力してください。'
    #フォームのパスワードが空欄
    elif len(password)==0 :
        message =  'パスワードを入力してください。'
    #入力された形式が間違えている
    else:
        if re.search(r'[a-z]@[a-z]', mail):
            message = 'パスワードの形式が違います。条件に沿って入力してください'
        elif re.fullmatch(r'[0-9a-z]{6,18}', password):
            message = 'メールアドレスの形式が違います。条件に沿って入力してください'
        else:
            message = 'メールアドレス、パスワードの形式が違います。条件に沿って入力してください'

    return render_template('regist_form.html', message=message)
"""
#17章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
@app.route("/transaction", methods=["GET", "POST"])
def transaction():
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'kaA1ybB2ucC3d2c'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名
    customer_id = 1        # 例題のため顧客は1に固定
    payment = 'クレジット'   # 例題のため購入方法はクレジットに固定する
    quantity = 1           # 例題のため数量は1に固定
    goods = []
    cnx = None
    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()
        order = ""
        goods_id = ""
        if "goods_id" in request.form.keys() :
            goods_id = request.form["goods_id"]

            try:
                date = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                sql = "INSERT INTO order_table (customer_id, order_date, payment) VALUES({}, '{}', '{}')".format(customer_id, date, payment)
                cursor.execute(sql)
                order_id = cursor.lastrowid # insertした値を取得できます。

                sql = "INSERT INTO order_detail_table (order_id, goods_id, quantity) VALUES({}, {}, {})".format(order_id, goods_id, quantity)
                cursor.execute(sql)

                cnx.commit()

            except mysql.connector.Error:
                cnx.rollback()
                raise

        sql = 'SELECT goods_id, goods_name, price FROM goods_table'
        cursor.execute(sql)

        for (goods_id, goods_name, price) in cursor:
            item = {"id": goods_id, "name": goods_name, "price":price}
            goods.append(item)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    finally:
        if cnx != None:
            cnx.close()

    return render_template("transaction.html", goods=goods)
"""
#18章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
#画像のためのパスetc
UPLOAD_FOLDER = './static/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#データベースアクセスのための鍵
host = 'localhost' # データベースのホスト名又はIPアドレス
username = 'root'  # MySQLのユーザ名
passwd   = 'kaA1ybB2ucC3d2c'    # MySQLのパスワード
dbname   = 'mydb'    # データベース名

#管理者画面
#ホーム画面
@app.route("/admin", methods=["GET", "POST"])
def admin():
    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try :
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #常時実行するSQL
        query = "SELECT  dt.drink_id as drink_id, dt.drink_image as drink_image, dt.drink_name as drink_name, dt.price as price, st.stock as stock, dt.status as status FROM drink_table as dt LEFT JOIN stock_table as st ON dt.drink_id = st.drink_id"
        cursor.execute(query)


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        goods = []
        for (id, image, name, price, stock, status) in cursor:
            item = {"id" : id, "image" : image, "name" : name, "price" : price, "stock" : stock, "status" : status}
            goods.append(item)


        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
            "goods" : goods
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()


    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("admin.html", **params)


#商品追加画面
@app.route("/admin/add", methods=["POST"])
def admin_add_item():

    #変数定義ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    #追加
    add_image = ""
    add_name = ""
    add_price = ""
    add_number = ""
    status_selector = ""
    filename = ""

    #HTML受け渡し(判定)
    add_message = ""

    #ボタンが押された場合にしか値を受け取らないーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    #商品追加された場合、値を取得
    add_image = request.files.get("add_image", "")
    add_name = request.form.get("add_name", "")
    add_price = request.form.get("add_price", "")
    add_number = request.form.get("add_number", "")
    status_selector = request.form.get("status_selector", "")
    #これでformから受け取った画像を保存する
    filename = secure_filename(add_image.filename)
    if filename != "" and filename != None:
        add_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        add_image = ""


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try :
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #常時実行するSQL
        query = "SELECT  dt.drink_id as drink_id, dt.drink_image as drink_image, dt.drink_name as drink_name, dt.price as price, st.stock as stock, dt.status as status FROM drink_table as dt LEFT JOIN stock_table as st ON dt.drink_id = st.drink_id"

        #SQLに画像のパスを保存する
        if add_image != "" and add_image != None:
            drink_image = "../static/" + filename


        #商品追加のボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        #全ての項目が入力されていない
        if add_image == "" or add_name == "" or add_price == "" or add_number == "" or status_selector == "":
            add_message = "＊追加失敗：全ての項目を条件通り入力してください"

        #在庫数と値段の値が数字ではない
        elif not add_number.isdecimal() or not add_price.isdecimal():
            add_message = "＊追加失敗：在庫数と値段は数字で入力してください"

        elif int(add_price) < 0 or int(add_number) < 0:
            add_message = "＊追加失敗：在庫数と値段は0以上の数字で入力してください"

        #全て入力され、在庫数と値段は0以上の数字(条件通り)
        else:
            drink_query = f"INSERT INTO drink_table (drink_image, drink_name, price, edit_date, update_date, status) VALUES ('{drink_image}', '{add_name}', {add_price}, LOCALTIME(), LOCALTIME(), {status_selector})"
            stock_query = f"INSERT INTO stock_table (drink_name, stock, edit_date, update_date) VALUES ('{add_name}', {add_number}, LOCALTIME(), LOCALTIME())"
            cursor.execute(drink_query)
            cursor.execute(stock_query)
            cnx.commit()
            add_message = "＊追加成功：商品が正常に追加されました"


        #いつでも実行する表示のためのSQLーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        cursor.execute(query)


        #データベース変更後に再度リストに格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        goods = []
        for (id, image, name, price, stock, status) in cursor:
            item = {"id" : id, "image" : image, "name" : name, "price" : price, "stock" : stock, "status" : status}
            goods.append(item)


        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
        "add_message" : add_message,
        "goods" : goods
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()


    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("admin.html", **params)


#在庫数変更
@app.route("/admin/stock", methods=["POST"])
def admin_stock():

    #在庫数変更の商品情報
    drink_id = ""
    drink_name = ""
    stock = ""

    #メッセージ
    change_message = ""


    #在庫数が変更された場合、値を取得
    drink_id = request.form.get("drink_id", "")
    drink_name = request.form.get("drink_name", "")
    stock = request.form.get("stock", "")


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #在庫変更のボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        #空欄
        if stock == "":
            change_message = "＊失敗：金額は空欄ではなく0以上の数字を入力してください"

        #文字列もしくはマイナスの値
        elif not stock.isdecimal() or int(stock) < 0:
            change_message = "＊失敗：金額は0以上の数字で入力してください"

        #0以上の数字(条件通り)
        else:
            stock_update = f'UPDATE stock_table SET stock = {stock} WHERE drink_id = {drink_id}'
            date_update = f'UPDATE stock_table SET update_date = LOCALTIME() WHERE drink_id = {drink_id}'
            cursor.execute(stock_update)
            cursor.execute(date_update)
            cnx.commit()
            change_message = "＊成功：" + drink_name + "の在庫数が変更されました"


        #常時実行するSQL
        query = "SELECT  dt.drink_id as drink_id, dt.drink_image as drink_image, dt.drink_name as drink_name, dt.price as price, st.stock as stock, dt.status as status FROM drink_table as dt LEFT JOIN stock_table as st ON dt.drink_id = st.drink_id"
        cursor.execute(query)


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        goods = []
        for (id, image, name, price, stock, status) in cursor:
            item = {"id" : id, "image" : image, "name" : name, "price" : price, "stock" : stock, "status" : status}
            goods.append(item)


        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
        "change_message" : change_message,
        "goods" : goods
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()


    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("admin.html", **params)


#ステータス変更
@app.route("/admin/status", methods=["POST"])
def admin_status():

    #ステータス変更の商品情報
    drink_id = ""
    drink_name = ""
    next_status = ""

    #メッセージ
    change_message = ""


    #ステータス変更が押された場合、値を取得
    drink_id = request.form.get("drink_id", "")
    drink_name = request.form.get("drink_name", "")
    next_status = request.form.get("change_status", "")


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try :
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #公開・非公開のボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        #押されたボタン(現在のステータス)とは逆のステータスに変更
        if drink_id != "" and drink_id != None:
            status_update = f'UPDATE drink_table SET status = {next_status} WHERE drink_id = {drink_id}'
            date_update = f'UPDATE drink_table SET update_date = LOCALTIME() WHERE drink_id = {drink_id}'
            cursor.execute(status_update)
            cursor.execute(date_update)
            cnx.commit()
            if next_status == "1":
                change_message = "＊成功：" + drink_name + "のステータスを「公開」に変更しました"
            elif next_status == "0":
                change_message = "＊成功：" + drink_name + "のステータスを「非公開」に変更しました"


        #常時実行するSQL
        query = "SELECT  dt.drink_id as drink_id, dt.drink_image as drink_image, dt.drink_name as drink_name, dt.price as price, st.stock as stock, dt.status as status FROM drink_table as dt LEFT JOIN stock_table as st ON dt.drink_id = st.drink_id"
        cursor.execute(query)


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        goods = []
        for (id, image, name, price, stock, status) in cursor:
            item = {"id" : id, "image" : image, "name" : name, "price" : price, "stock" : stock, "status" : status}
            goods.append(item)


        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
            "change_message" : change_message,
            "goods" : goods
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()


    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("admin.html", **params)



#購入者画面-----------------------------------------------------------------
@app.route("/user", methods=["GET", "POST"])
def user():

    #変数定義ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    #購入
    my_money = ""
    drink_id = ""
    drink_name = ""
    drink_price = ""

    #HTML受け渡し(判定)
    message = ""
    judge_money = ""
    judge_select = ""
    home = ""
    success = ""

    #購入金額比較
    bought = ""


    #ボタンが押された場合にしか値を受け取らないーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    #商品追加された場合、値を取得
    my_money = request.form.get("my_money", "")
    drink_id = request.form.get("drink_id", "")
    drink_name = request.form.get("drink_name", "")
    drink_price = request.form.get("drink_price", "")


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try :
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #常時実行するSQL
        query = "SELECT  dt.drink_id as drink_id, dt.drink_image as drink_image, dt.drink_name as drink_name, dt.price as price, st.stock as stock, dt.status as status FROM drink_table as dt LEFT JOIN stock_table as st ON dt.drink_id = st.drink_id WHERE status = 1"
        cursor.execute(query)


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        goods = []
        for (id, image, name, price, stock, status) in cursor:
            item = {"id" : id, "image" : image, "name" : name, "price" : price, "stock" : stock, "status" : status}
            goods.append(item)
            if str(item["id"]) == drink_id:
                bought = item


        #商品購入ボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        if "buy_drink" in request.form.keys():
            if my_money == "" and drink_id == "":
                message = "自動販売機結果"
                judge_money = "＊失敗：お金を投入してください"
                judge_select = "＊失敗：商品を選択してください"

            #金額が入力されていない
            elif my_money == "":
                message = "自動販売機結果"
                judge_money = "＊失敗：お金を投入してください"

            #商品が選択されていない
            elif drink_id == "":
                message = "自動販売機結果"
                judge_select = "＊失敗：商品を選択してください"

            #文字列が入力されている
            elif not my_money.isdecimal():
                message = "自動販売機結果"
                judge_money = "＊失敗：金額は数字で入力してください"

            #金額・商品共に条件通り入力されているが、公開されていない
            elif bought == "" :
                    message = "自動販売機結果"
                    judge_money = "＊失敗：申し訳ありません、この商品は現在お売りすることができません"

            #金額・商品共に条件通り入力されているが、公開されていない
            elif bought["stock"] == 0:
                    message = "自動販売機結果"
                    judge_money = "＊失敗：現在在庫がありません"

            #金額・商品共に条件通り入力されているが、お金が足りていない
            elif int(drink_price) > int(my_money):
                    message = "自動販売機結果"
                    judge_money = "＊失敗：投入金額が" + str(bought["price"]- int(my_money)) + "円足りません"

            #金額・商品共に条件通り入力されている(購入成功)
            else:
                message = "自動販売機結果"
                judge_money = "＊成功：ガシャコン！！" + drink_name + "が買えました！＊"
                judge_select = "<<<お釣りは" + str(int(my_money) - bought["price"]) + "円です>>>"
                #在庫数変更のクエリ
                stock_update = f'UPDATE stock_table SET stock = {bought["stock"]-1} WHERE drink_id = {drink_id}'
                history_update = f'INSERT INTO history_table (drink_id, order_date) VALUES ({drink_id}, LOCALTIME())'
                cursor.execute(stock_update)
                cursor.execute(history_update)
                cnx.commit()
                success = bought["image"]

        else:
            message = "自動販売機"
            home = "home"



        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
            "success" : success,
            "judge_money" : judge_money,
            "judge_select" : judge_select,
            "message" : message,
            "goods" : goods,
            "home" : home
        }



    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("user.html", **params)
"""
#19章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
from flask import Flask
from flask import request
from flask import render_template
import mysql.connector
# from model.employee import Employee
import model.database as db
from model.item import Item


app = Flask(__name__)

@app.route("/mysql_select")
def mysql_select():
    order = ""
    if "order" in request.args.keys() :
            order = request.args.get("order")

    goods = db.get_goods(order)

    params = {
    "asc_check" : order == "ASC",
    "desc_check" : order == "DESC",
    "goods" : goods
    }
    return render_template("goods.html", **params)
"""
#20章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
from flask import make_response
@app.route("/cookie")
def sample_cookie():
    count = request.cookies.get('count')
    if count is None:
        count = 1
    else:
        count = int(count) + 1
    response = make_response("{}回目の訪問です".format(count))
    response.set_cookie('count', str(count))
    return response
"""
"""
app = Flask(__name__)
app.secret_key = 'hogehoge'

@app.route("/session")
def sample_session():
    count = session.get('count')
    if count is None:
        count = 1
    else:
        count = int(count) + 1
    session["count"] = count
    return "{}回目の訪問です".format(count)

"""
#20章課題(cookie)
"""
from flask import make_response
@app.route("/cookie", methods=["GET", "POST"])
def cookie():
    #cookie上のcountとnow_loginの情報を入手å
    count = request.cookies.get('count')
    last_login = request.cookies.get('now_login',"")
    #last_loginの値をセットした後でnow_loginに現在時刻を取得
    now_login = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    if count is None:
        count = 1
    else:
        count = int(count) + 1

    params = {
        "count" : count,
        "last_login" : last_login,
        "now_login" : now_login
    }

    response = make_response(render_template('cookie.html', **params))
    #cookieに値をセットする(例：countは値が更新されている)
    if "delete_cookie" in request.form.keys():
        response.set_cookie('count', str(count), expires=0)
        response.set_cookie('last_login', last_login, expires=0)
        response.set_cookie('now_login', now_login, expires=0)
        print("cookie削除しました")
    else:
        response.set_cookie('count', str(count))
        response.set_cookie('last_login', last_login)
        response.set_cookie('now_login', now_login)
        print("訪問しました")

    return response
"""
#20章課題(sesion)
"""
from flask import session
app = Flask(__name__)
app.secret_key = 'hogehoge'

@app.route("/session", methods=["GET", "POST"])
def sample_session():
    count = session.get('count')
    last_login = session.get('now_login',"")
    now_login = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    if count is None:
        count = 1
    else:
        count = int(count) + 1

    if "delete_cookie" in request.form.keys():
        session["count"] = None
        session["last_login"] = ""
        session["now_login"] = ""
    else:
        session["count"] = count
        session["last_login"] = last_login
        session["now_login"] = now_login

    params = {
        "count" : count,
        "last_login" : last_login,
        "now_login" : now_login
    }

    response = render_template('session.html', **params)

    return response
"""
#21章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#画像のためのパスや定義
UPLOAD_FOLDER = './static/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#データベース接続の鍵
host = 'localhost' # データベースのホスト名又はIPアドレス
username = 'root'  # MySQLのユーザ名
passwd   = 'kaA1ybB2ucC3d2c'    # MySQLのパスワード
dbname   = 'mydb'    # データベース名


#データベースに接続
def connectDatabase():
    cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
    cursor = cnx.cursor()
    return cursor, cnx


#従業員データを取得し、配列に代入する
def tableDataStorage():
    cursor, cnx = connectDatabase()
    query = "SELECT emp_id, emp_name, dept_name FROM emp_info_table as eit JOIN dept_table as dt ON eit.dept_id = dt.dept_id ORDER BY emp_id;"
    cursor.execute(query)
    emp_info = []
    for (id, name, dept) in cursor:
        item = {"id" : id, "name" : name, "dept" : dept}
        emp_info.append(item)
    return emp_info


#社員情報を受け渡すーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
@app.route("/emp", methods=['GET', 'POST'])
def employeeList():
    emp_info = tableDataStorage()
    params = {
    "emp_info" : emp_info
    }
    return render_template("all_emp.html", **params)






#HTMLから情報を受け取る
def getEmpInfo():
    add = "新規追加"
    emp_name = request.form.get("emp_name", "")
    emp_age = request.form.get("emp_age", "")
    emp_sex = request.form.get("emp_sex", "")
    emp_postal = request.form.get("emp_postal", "")
    emp_pref = request.form.get("emp_pref", "")
    emp_address = request.form.get("emp_address", "")
    emp_dept = request.form.get("emp_dept", "")
    join_date = request.form.get("join_date", "")
    retire_date = request.form.get("retire_date", "")
    emp_image = request.files.get("emp_image", "")
    image_id = ""
    for i in range(10):
        image_id += (random.choice(string.ascii_letters))
    return add, emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, emp_image


#画像の有無
def imageSetVariable(emp_image):
    add_emp_image = ""
    if emp_image != "":
        filename = secure_filename(emp_image.filename)
        if filename != "":
            emp_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            add_emp_image = "../static/" + filename
        else:
            emp_image = ""
    return add_emp_image, emp_image


#部署セレクター
def dataDeptSelector(cursor):
    query = "SELECT dept_id, dept_name FROM dept_table ORDER BY dept_id;"
    cursor.execute(query)

    dept_info = []
    for (id, name) in cursor:
        item = {"id" : id, "name" : name}
        dept_info.append(item)

    return dept_info


#新規追加クエリを保管
def setAddQuery(emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, add_emp_image):
    if retire_date == "":
        info_add = f'INSERT INTO emp_info_table (emp_name, age, sex, image_id, post_code, pref, address, dept_id, join_date, retire_date, update_date) VALUES ("{emp_name}", {emp_age}, "{emp_sex}", "{image_id}", "{emp_postal}", "{emp_pref}", "{emp_address}", {emp_dept}, "{join_date}", "在籍", LOCALTIME())'
        img_add = f'INSERT INTO emp_img_table (image_id, emp_image, update_date) VALUES ("{image_id}", "{add_emp_image}", LOCALTIME())'
    else:
        info_add = f'INSERT INTO emp_info_table (emp_name, age, sex, image_id, post_code, pref, address, dept_id, join_date, retire_date, update_date) VALUES ("{emp_name}", {emp_age}, "{emp_sex}", "{image_id}", "{emp_postal}", "{emp_pref}", "{emp_address}", {emp_dept}, "{join_date}", "{retire_date}", LOCALTIME())'
        img_add = f'INSERT INTO emp_img_table (image_id, emp_image, update_date) VALUES ("{image_id}", "{add_emp_image}", LOCALTIME())'
    return info_add, img_add


#設定のボタンが押された場合
def exeAddQuery(cursor, cnx,  emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, add_emp_image, emp_image, info_add, img_add):
    judge = ""
    result = ""
    if "setting" in request.form.keys():
        #値が入力されておらず空欄のまま
        if emp_name == "" or emp_age == "" or emp_sex == "" or emp_postal == "" or emp_pref == "" or emp_address == "" or emp_image == "" or emp_dept == "" or join_date == "":
            judge = "＊失敗：全ての項目を入力してください"
            result = "false"

        #年齢が数字以外で入力されている
        elif not emp_age.isdecimal():
            judge = "＊失敗：年齢は半角数字で入力してください"
            result = "false"

        #郵便番号が数字以外で入力されている
        elif not re.match(r"[0-9]{3}-?[0-9]{4}", emp_postal):
            judge = "＊失敗：郵便番号は半角数字で入力してください"
            result = "false"

        #名前の間に半角で空欄が入ってない
        elif not re.search(r"[ ]", emp_name):
            judge = "＊失敗：名前と苗字の間に半角で空欄を入力してください"
            result = "false"

        #条件通りなので新規追加
        else:
            cursor.execute(info_add)
            cursor.execute(img_add)
            cnx.commit()
            judge = "＊成功：データベースの追加が行われました"
            result = "success"

    return judge, result


#値を集約
def correctValue(add, judge, result, dept_info):
    params = {
        "add" : add,
        "judge" : judge,
        "result" : result,
        "dept_info" : dept_info
    }
    return params


#新規追加URL
@app.route("/emp/add", methods=["POST"])
def addNewEmp():
    add, emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, emp_image = getEmpInfo()

    add_emp_image = imageSetVariable(emp_image)

    cursor, cnx = connectDatabase()
    dept_info = dataDeptSelector(cursor)

    info_add, img_add = setAddQuery(emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, add_emp_image)
    judge, result = exeAddQuery(cursor, cnx,  emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, add_emp_image, emp_image, info_add, img_add)
    params = correctValue(add, judge, result, dept_info)

    return render_template("emp_add.html", **params)









#編集
@app.route("/emp/edit", methods=["POST"])
def emp_edit():

    #追加したい部署名
    emp_name = ""
    emp_age = ""
    emp_sex = ""
    emp_postal = ""
    emp_pref = ""
    emp_address = ""
    emp_image = ""
    emp_dept = ""
    join_date = ""
    retire_date = ""
    image_id = ""

    #セレクターのため
    dept_select = ""
    pref_select = ""

    #画像のための変数
    add_emp_image = ""
    filename = ""

    #情報を編集する社員のID
    change_info = ""

    #メッセージ
    judge = ""
    result = ""


    #変更ボタンがおされた場合、値を取得(ボタンが押されたときに値を取りたい)
    change_info = request.form.get("change_info", "")
    print(change_info)
    #入力された部署名を取得
    emp_name = request.form.get("emp_name", "")
    emp_age = request.form.get("emp_age", "")
    emp_sex = request.form.get("emp_sex", "")
    emp_postal = request.form.get("emp_postal", "")
    emp_pref = request.form.get("emp_pref", "")
    emp_address = request.form.get("emp_address", "")
    emp_dept = request.form.get("emp_dept", "")
    join_date = request.form.get("join_date", "")
    retire_date = request.form.get("retire_date", "")
    emp_image = request.files.get("emp_image", "")
    if emp_image != "":
        filename = secure_filename(emp_image.filename)
        if filename != "":
            emp_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            emp_image = ""
    image_id = request.form.get("image_id", "")


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #編集ボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        if "setting" in request.form.keys():
            if emp_name == "" or emp_age == "" or emp_sex == "" or emp_postal == "" or emp_pref == "" or emp_address == "" or emp_dept == "" or join_date == "" or retire_date == "":
                judge = "＊失敗：データベースの変更ができませんでした"
                result = "fales"

            elif not emp_age.isdecimal():
                judge = "＊失敗：年齢は半角数字で入力してください"
                result = "false"

            elif not re.match(r"[0-9]{3}-?[0-9]{4}", emp_postal):
                judge = "＊失敗：郵便番号は半角数字で入力してください"
                result = "false"

            elif not re.search(r"[ ]", emp_name):
                judge = "＊失敗：名前と苗字の間に半角で空欄を入力してください"
                result = "false"

            elif emp_image == "":
                print("エリフーーーーーーー")
                info_update = f'UPDATE emp_info_table SET emp_name = "{emp_name}", age = {emp_age}, sex = "{emp_sex}", post_code = "{emp_postal}", pref = "{emp_pref}", address = "{emp_address}", dept_id = {emp_dept}, join_date = "{join_date}", retire_date = "{retire_date}", update_date = LOCALTIME() WHERE emp_id = {change_info}'
                cursor.execute(info_update)
                cnx.commit()
                judge = "＊成功：データベースの変更が行われました"
                result = "success"
                print(emp_name, emp_age, emp_sex, emp_pref, emp_address, emp_postal, emp_dept, join_date, retire_date, change_info)

            else:
                print("エルスーーーーーーー")
                info_update = f'UPDATE emp_info_table SET emp_name = "{emp_name}", age = {emp_age}, sex = "{emp_sex}", post_code = "{emp_postal}", pref = "{emp_pref}", address = "{emp_address}", dept_id = {emp_dept}, join_date = "{join_date}", retire_date = "{retire_date}", update_date = LOCALTIME() WHERE emp_id = {change_info}'
                img_update = f'UPDATE emp_img_table SET emp_image = "{add_emp_image}", update_date = LOCALTIME() WHERE image_id = "{image_id}"'
                cursor.execute(info_update)
                cursor.execute(img_update)
                cnx.commit()
                judge = "＊成功：データベースの変更が行われました"
                result = "success"


        #常時実行するSQL
        query = "SELECT info.emp_id as emp_id, emp_name, age, sex, info.image_id, post_code, pref, address, dept_id, join_date, retire_date, emp_image FROM emp_info_table as info JOIN emp_img_table as img ON info.image_id = img.image_id;"
        cursor.execute(query)


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        edit_info = []
        #社員ID、名前、年齢、性別、都道府県、住所、部署ID、入社日、退社日、画像
        for (id, name, age, sex, image_id, post, pref, address, dept, join, retire, image) in cursor:
            item = {"id" : id, "name" : name, "age" : age, "sex" : sex, "image_id" : image_id,"post" : post, "pref" : pref, "address" : address, "dept" : dept, "join" : join, "retire" : retire , "image" : image}
            if str(item["id"]) == change_info:
                edit_info.append(item)
                dept_select = item["dept"]
                pref_select = item["pref"]
        print(edit_info)


        #常時実行するSQL
        query = "SELECT dept_id, dept_name FROM dept_table ORDER BY dept_id;"
        cursor.execute(query)

        #SQLで取得した値を格納(HTMLに送るためのリスト)
        dept_info = []
        for (id, name) in cursor:
            item = {"id" : id, "name" : name}
            dept_info.append(item)

        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
            "pref_select" : pref_select,
            "dept_select" : dept_select,
            "dept_info" : dept_info,
            "edit_info" : edit_info,
            "result" : result,
            "judge" : judge
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("emp_add.html", **params)


#検索
@app.route("/emp/search", methods=["POST"])
def emp_search():

    #検索条件
    search_dept = ""
    search_emp_id = ""
    search_name = ""

    #社員数計測
    emp_count = 0


    #検索条件の取得
    search_dept = request.form.get("search_dept", "")
    search_emp_id = request.form.get("search_emp_id", "")
    search_name = request.form.get("search_name", "")


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try :
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()

        #社員情報のSQL
        query = f'SELECT emp_id, emp_name, dept_name FROM emp_info_table as eit JOIN dept_table as dt ON eit.dept_id = dt.dept_id WHERE emp_id IS NOT NULL '

        #もし検索条件があれば条件を加えていく
        if search_dept != "" or search_emp_id != "" or search_name != "":
            if search_dept != "":
                query += f'AND dt.dept_id = {search_dept} '
                print("所属部署")
            if search_emp_id != "":
                query += f'AND emp_id = {search_emp_id} '
                print("社員番号")
            if search_name != "":
                query += f'AND emp_name LIKE "%{search_name}%" '
                print("名前")

        query += 'ORDER BY emp_id'
        #どんな時でも実行
        cursor.execute(query)


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        emp_info = []
        for (id, name, dept) in cursor:
            item = {"id" : id, "name" : name, "dept" : dept}
            emp_info.append(item)
            emp_count += 1


        #部署セレクターのためのSQL
        query = "SELECT dept_id, dept_name FROM dept_table ORDER BY dept_id;"
        cursor.execute(query)


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        dept_info = []
        for (id, name) in cursor:
            item = {"id" : id, "name" : name}
            dept_info.append(item)

        print(search_dept)


        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
            "search_name" : search_name,
            "search_emp_id" : search_emp_id,
            "search_dept" : search_dept,
            "emp_count" : emp_count,
            "dept_info" : dept_info,
            "emp_info" : emp_info
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()


    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("emp_search.html", **params)


#CSVファイル出力
@app.route("/emp/output", methods=["GET", "POST"])
def emp_output():

    #出力成功の文字
    message = ""

    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try :
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #CSVファイル出力のために実行するSQL
        output_query = "SELECT * FROM emp_info_table INTO OUTFILE '/Users/kytakahashi/Downloads/プログラム/my_project/output/社員情報.csv' FIELDS TERMINATED BY ',';"
        cursor.execute(output_query)
        message = "成功：社員データをCSVファイルに出力しました"


        #常時実行するSQL
        query = "SELECT emp_id, emp_name, dept_name FROM emp_info_table as eit JOIN dept_table as dt ON eit.dept_id = dt.dept_id ORDER BY emp_id;"
        cursor.execute(query)


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        emp_info = []
        for (id, name, dept) in cursor:
            item = {"id" : id, "name" : name, "dept" : dept}
            emp_info.append(item)


        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
            "emp_info" : emp_info,
            "message" : message
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()


    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("all_emp.html", **params)




#削除
@app.route("/emp/delete", methods=["POST"])
def emp_delete():

    #削除ボタンを押された部署のIDと名前
    delete_info = ""
    emp_name = ""

    #メッセージ
    message = ""

    #在削除ボタンが押された時に値取得
    delete_info = request.form.get("delete_info", "")
    emp_name = request.form.get("emp_name", "")


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #在庫変更のボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        if "delete_info" in request.form.keys() and delete_info != "":
            #削除ボタンが押された
            info_delete = f'DELETE FROM emp_info_table WHERE emp_id = {delete_info}'
            img_delete = f'DELETE FROM emp_img_table WHERE emp_id = {delete_info}'
            cursor.execute(info_delete)
            cursor.execute(img_delete)
            cnx.commit()
            message = "＊削除：" + emp_name + "をデータベースから削除しました"


        #常時実行するSQL
        query = "SELECT emp_id, emp_name FROM emp_info_table;"
        cursor.execute(query)


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        emp_info = []
        for (id, name) in cursor:
            item = {"id" : id, "name" : name}
            emp_info.append(item)


        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
            "emp_info" : emp_info,
            "message" : message
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("all_emp.html", **params)



#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


#部署画面
#ホーム画面
@app.route("/dept", methods=["GET", "POST"])
def dept():
    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try :
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #常時実行するSQL
        query = "SELECT dept_id, dept_name FROM dept_table;"
        cursor.execute(query)


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        dept_info = []
        for (id, name) in cursor:
            item = {"id" : id, "name" : name}
            dept_info.append(item)


        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
            "dept_info" : dept_info
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()


    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("all_dept.html", **params)


#新規追加画面
@app.route("/dept/add", methods=["POST"])
def dept_add():

    #追加したい部署名
    dept_name = ""
    add = "新規作成"

    #メッセージ
    result = ""
    judge = ""


    #入力された部署名を取得
    dept_name = request.form.get("dept_name", "")


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()

        #常時実行するSQL
        query = "SELECT dept_id, dept_name FROM dept_table;"
        cursor.execute(query)

        #SQLで取得した値を格納(HTMLに送るためのリスト)
        dept_info = []
        for (id, name) in cursor:
            item = {"id" : id, "name" : name}
            dept_info.append(item)


        #設定のボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        if "setting" in request.form.keys():
            #値が入力されておらず空欄のまま
            if dept_name == "" or not "部" in dept_name:
                judge = "＊失敗：部署名を入力してください"
                result = "success"

            #条件通りなので新規追加
            else:
                dept_add = f"INSERT INTO dept_table (dept_name, edit_date, update_date) VALUES ('{dept_name}', LOCALTIME(), LOCALTIME())"
                cursor.execute(dept_add)
                cnx.commit()
                judge = "＊成功：データベースの追加が行われました"
                result = "success"


        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        cursor.execute(query)
        params = {
            "add" : add,
            "judge" : judge,
            "result" : result,
            "dept_info" : dept_info
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()


    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("dept_add.html", **params)


#編集
@app.route("/dept/edit", methods=["POST"])
def dept_edit():

    #追加したい部署名
    dept_name = ""
    change_info = ""

    #メッセージ
    result = ""
    judge = ""

    #入力された部署名を取得
    dept_name = request.form.get("dept_name", "")
    change_info = request.form.get("change_info", "")


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()

        #常時実行するSQL
        query = "SELECT dept_id, dept_name FROM dept_table;"
        cursor.execute(query)

        #SQLで取得した値を格納(HTMLに送るためのリスト)
        dept_info = []
        for (id, name) in cursor:
            item = {"id" : id, "name" : name}
            dept_info.append(item)


        #設定のボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        if "setting" in request.form.keys() and change_info != "":
            if dept_name == "":
                judge = "＊失敗：データベースの変更ができませんでした"
                result = "fales"

            else:
                name_update = f'UPDATE dept_table SET dept_name = "{dept_name}", update_date = LOCALTIME() WHERE dept_id = {change_info}'
                cursor.execute(name_update)
                cnx.commit()
                judge = "＊成功：データベースの変更が行われました"
                result = "success"


        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
            "judge" : judge,
            "result" : result,
            "change_info" : change_info,
            "dept_name" : dept_name
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()


    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("dept_add.html", **params)



#削除
@app.route("/dept/delete", methods=["POST"])
def dept_delete():

    #削除ボタンを押された部署のIDと名前
    delete_info = ""
    dept_name = ""

    #メッセージ
    message = ""

    #在削除ボタンが押された時に値取得
    delete_info = request.form.get("delete_info", "")
    dept_name = request.form.get("dept_name", "")


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #在庫変更のボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        if "delete_info" in request.form.keys() and delete_info != "":
            #削除ボタンが押された
            dept_delete = f'DELETE FROM dept_table WHERE dept_id = {delete_info}'
            cursor.execute(dept_delete)
            cnx.commit()
            message = "＊削除：" + dept_name + "をデータベースから削除しました"


        #常時実行するSQL
        query = "SELECT dept_id, dept_name FROM dept_table;"
        cursor.execute(query)


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        dept_info = []
        for (id, name) in cursor:
            item = {"id" : id, "name" : name}
            dept_info.append(item)


        #値の入った変数やリストをHTMLに渡すための変数に格納ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        params = {
            "dept_info" : dept_info,
            "message" : message
        }


    #もしユーザー名やパスワードなどに誤りがあった場合エラーを出すーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    #HTMLへ変数を送るーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    return render_template("all_dept.html", **params)
