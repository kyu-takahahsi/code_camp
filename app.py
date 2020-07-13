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

#MVC
import model.database as db
from model.item import EMP, DEPT, EMP_ALL, EMP_COUNT

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#ホーム画面
@app.route("/", methods=['GET', 'POST'])
def employeeList():
    emp_info = db.tableDataStorage()

    params = {
    "emp_info" : emp_info
    }

    return render_template("all_emp.html", **params)


#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
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


#値を集約
def correctAddEmpValue(add, judge, result, dept_info):
    params = {
        "add" : add,
        "judge" : judge,
        "result" : result,
        "dept_info" : dept_info
    }

    return params


#新規追加URL(部品を集めて実行する)
@app.route("/emp/add", methods=["POST"])
def addNewEmp():
    #値の取得
    add, emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, emp_image = getEmpInfo()

    #画像にパスを通す
    add_emp_image, emp_image = imageSetVariable(emp_image)

    #データベースに接続
    cursor, cnx = db.connectDatabase()

    #部署名セレクターのためのリスト
    dept_info = db.deptInfoData(cursor)

    #クエリの取得
    info_add, img_add = db.setAddEmpQuery(emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, add_emp_image)

    #クエリ実行するかの判定、結果
    judge, result = db.exeAddEmpQuery(cursor, cnx,  emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, add_emp_image, emp_image, info_add, img_add)

    #HTMLに送る全ての値をparamsに格納
    params = correctAddEmpValue(add, judge, result, dept_info)

    #HTMLへ変数を送る
    return render_template("emp_add.html", **params)

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

#編集する社員の情報を取得
def getChangeEmpInfo():
    #編集が押された社員のidを取得
    change_info = request.form.get("change_info", "")
    #編集が押された社員の基本情報を取得
    emp_name = request.form.get("emp_name", "")
    emp_age = request.form.get("emp_age", "")
    emp_sex = request.form.get("emp_sex", "")
    emp_postal = request.form.get("emp_postal", "")
    emp_pref = request.form.get("emp_pref", "")
    emp_address = request.form.get("emp_address", "")
    emp_dept = request.form.get("emp_dept", "")
    join_date = request.form.get("retire_date", "")
    retire_date = request.form.get("retire_date", "")
    emp_image = request.files.get("emp_image", "")
    image_id = request.form.get("image_id", "")

    return change_info, emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, emp_image


#値を集約
def correctEditValue(pref_select, dept_select, dept_info, edit_info, judge, result):
    params = {
        "pref_select" : pref_select,
        "dept_select" : dept_select,
        "dept_info" : dept_info,
        "edit_info" : edit_info,
        "result" : result,
        "judge" : judge
    }

    return params


#編集のURL(部品を集めて実行する)
@app.route("/emp/edit", methods=["POST"])
def editEmp():
    #値の取得
    change_info, emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, emp_image = getChangeEmpInfo()

    #画像にパスを通す
    add_emp_image, emp_image = imageSetVariable(emp_image)

    #データベースに接続
    cursor, cnx = db.connectDatabase()

    #部署名セレクターのためのリスト
    dept_info = db.deptInfoData(cursor)

    #編集を押した従業員のIDと都道府県を格納
    edit_info, dept_select, pref_select = db.getEditEmpinfo(cursor, change_info)

    #クエリの取得
    info_update, img_update = db.setEditEmpQuery(change_info, emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, add_emp_image)

    #クエリ実行するかの判定、結果
    judge, result = db.exeEditQuery(cursor, cnx,  emp_name, emp_age, emp_sex, emp_postal, emp_pref, emp_address, emp_dept, join_date, retire_date, image_id, add_emp_image, emp_image, info_update, img_update)

    #HTMLに送る全ての値をparamsに格納
    params = correctEditValue(pref_select, dept_select, dept_info, edit_info, judge, result)

    #HTMLへ変数を送る
    return render_template("emp_add.html", **params)


#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

#検索条件の取得
def getSearchEmpInfo():
    search_dept = request.form.get("search_dept", "")
    search_emp_id = request.form.get("search_emp_id", "")
    search_name = request.form.get("search_name", "")

    return search_dept, search_emp_id, search_name


#値を集約
def correctSearchEmpValue(search_name, search_emp_id, search_dept, dept_info, emp_info, emp_count):
    params = {
        "search_name" : search_name,
        "search_emp_id" : search_emp_id,
        "search_dept" : search_dept,
        "emp_count" : emp_count,
        "dept_info" : dept_info,
        "emp_info" : emp_info
    }

    return params


#検索のURL(部品を集めて実行する)
@app.route("/emp/search", methods=["POST"])
def searchEmp():
    #検索条件の値の取得
    search_dept, search_emp_id, search_name = getSearchEmpInfo()

    #データベースに接続
    cursor, cnx = db.connectDatabase()

    #部署名セレクターのためのリスト
    dept_info = db.deptInfoData(cursor)

    #クエリの取得
    query = db.setSearchQuery(search_dept, search_emp_id, search_name)

    #クエリ実行するかの判定、結果
    emp_info, emp_count = db.exeSearchEmpQuery(cursor, query)

    #HTMLに送る全ての値をparamsに格納
    params = correctSearchEmpValue(search_name, search_emp_id, search_dept, dept_info, emp_info, emp_count)

    #HTMLへ変数を送る
    return render_template("emp_search.html", **params)


#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#csv出力
@app.route('/emp/output', methods=["GET", "POST"])
def outputCsv():
    cursor, cnx = db.connectDatabase()
    csv = db.downloads(cursor)
    response = make_response(csv)
    response.headers["Content-Disposition"] = f"attachment; filename=employee_information.csv"

    return response


#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

#削除する社員の情報取得
def getDeleteEmpInfo():
    delete_info = request.form.get("delete_info", "")
    emp_name = request.form.get("emp_name", "")

    return delete_info, emp_name


#値を集約
def correctDeleteEmpValue(emp_info, message):
    params = {
        "emp_info" : emp_info,
        "message" : message
    }

    return params


#削除のURL(部品を集めて実行する)
@app.route("/emp/delete", methods=["POST"])
def deleteEmp():
    #検索条件の値の取得
    delete_info, emp_name = getDeleteEmpInfo()

    #データベースに接続
    cursor, cnx = db.connectDatabase()

    #部署名のためのリスト
    dept_info = db.deptInfoData(cursor)

    #クエリの取得
    info_delete, img_delete = db.setDeleteEmpQuery(delete_info)

    #社員情報のリスト
    emp_info = db.tableDataStorage()

    #情報が存在するかの確認
    exist_info = db.comformDeleteEmpInfo(emp_info, delete_info)

    #クエリ実行するかの判定、結果
    message, emp_info = db.exeDeleteEmpQuery(cursor, cnx, info_delete, img_delete, delete_info, emp_name, exist_info)

    #HTMLに送る全ての値をparamsに格納
    params = correctDeleteEmpValue(emp_info, message)

    #HTMLへ変数を送る
    return render_template("all_emp.html", **params)


#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


#部署画面
#ホーム画面
@app.route("/dept", methods=["GET", "POST"])
def deptList():
    #データベース接続
    cursor, cnx = db.connectDatabase()

    #部署データを取得
    dept_info = db.deptInfoData(cursor)

    #値の入った変数やリストをHTMLに渡すための変数に格納
    params = {
        "dept_info" : dept_info
    }

    #HTMLへ変数を送る
    return render_template("all_dept.html", **params)

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


#編集する社員の情報を取得
def getAddDeptInfo():
    add = "新規作成"
    dept_name = request.form.get("dept_name", "")

    return add, dept_name


#値を集約
def correctAddDeptValue(add, judge, result, dept_info):
    params = {
        "add" : add,
        "judge" : judge,
        "result" : result,
        "dept_info" : dept_info
    }

    return params


#新規追加URL(部品を集めて実行する)
@app.route("/dept/add", methods=["POST"])
def addNewDept():
    #追加するための値取得
    add, dept_name = getAddDeptInfo()

    #データベース接続
    cursor, cnx = db.connectDatabase()

    #部署データを取得
    dept_info = db.deptInfoData(cursor)

    #部署を追加するためのクエリ
    dept_add = db.setAddDeptQuery(dept_name)

    #条件による判定
    judge, result = db.exeAddDeptQuery(cursor, cnx, dept_name, dept_add)

    #値を集約
    params = correctAddDeptValue(add, judge, result, dept_info)

    #HTMLへ変数を送る
    return render_template("dept_add.html", **params)


#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

#編集する部署の情報を取得
def getChangeDeptInfo():
    dept_name = request.form.get("dept_name", "")
    change_info = request.form.get("change_info", "")

    return dept_name, change_info


#値を集約
def correctEditDeptValue(judge, result, change_info, dept_name):
    params = {
        "judge" : judge,
        "result" : result,
        "change_info" : change_info,
        "dept_name" : dept_name
    }

    return params


#編集のURL(部品を集めて実行する)
@app.route("/dept/edit", methods=["POST"])
def editDept():
    #追加するための値取得
    dept_name, change_info = getChangeDeptInfo()

    #データベース接続
    cursor, cnx = db.connectDatabase()

    #部署データを取得
    dept_info = db.deptInfoData(cursor)

    #部署を更新するためのクエリ
    dept_update = db.setEditDeptQuery(change_info, dept_name)

    #条件による判定
    judge, result = db.exeEditDeptQuery(cursor, cnx, change_info, dept_name, dept_update)

    #値を集約
    params = correctEditDeptValue(judge, result, change_info, dept_name)

    #HTMLへ変数を送る
    return render_template("dept_add.html", **params)

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

#削除する部署の情報取得
def getDeleteDeptInfo():
    delete_info = request.form.get("delete_info", "")
    dept_name = request.form.get("dept_name", "")

    return delete_info, dept_name


#値を集約
def correctDeleteDeptValue(dept_info, message):
    params = {
        "dept_info" : dept_info,
        "message" : message
    }

    return params


#削除のURL(部品を集めて実行する)
@app.route("/dept/delete", methods=["POST"])
def deleteDept():
    #追加するための値取得
    delete_info, dept_name = getDeleteDeptInfo()

    #データベース接続
    cursor, cnx = db.connectDatabase()

    #部署データを取得
    dept_info = db.deptInfoData(cursor)

    #部署を更新するためのクエリ
    dept_delete = db.setDeleteDeptQuery(delete_info)

    #情報が存在するかの確認
    exist_info = db.comformDeleteInfo(dept_info, delete_info)

    #条件による判定
    message, dept_info = db.exeDeleteDeptQuery(cursor, cnx, delete_info, dept_name, dept_delete, exist_info, dept_info)

    #値を集約
    params = correctDeleteDeptValue(dept_info, message)

    #HTMLへ変数を送る
    return render_template("all_dept.html", **params)
