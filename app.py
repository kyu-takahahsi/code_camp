from flask import Flask, flash, redirect, url_for
app = Flask(__name__)
#HTMLに反映
from flask import render_template
#HTMLから抽出
from flask import request
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

"""
#10章課題3
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
        add_comment = re
        quest.form.get("add_comment")


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
UPLOAD_FOLDER = '/Users/kytakahashi/Downloads/my_project/static/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#18章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#管理者画面
@app.route("/admin", methods=["GET", "POST"])
def admin():
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'kaA1ybB2ucC3d2c'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名


    #変数定義ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    #追加
    add_image = ""
    add_name = ""
    add_price = ""
    add_number = ""
    status_selector = ""
    filename = ""

    #HTML受け渡し(判定)
    goods = ""
    add_message = ""
    change_message = ""

    #ステータス変更
    change_status = ""
    update_status = ""

    #在庫数変更
    change_stock = ""
    change_stock_id = ""
    update_stock = ""


    #ボタンが押された場合にしか値を受け取らないーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    #商品追加された場合、値を取得
    if "add_drink" in request.form.keys():
        add_image = request.files.get("add_image")
        add_name = request.form.get("add_name")
        add_price = request.form.get("add_price")
        add_number = request.form.get("add_number")
        status_selector = request.form.get("status_selector")
        #これでformから受け取った画像を保存する
        filename = secure_filename(add_image.filename)
        #if re.search(r'jpeg|jpg|png', add_image):
        if filename != "" and filename != None:
            add_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            add_image = ""



    #ステータス変更された場合、値を取得
    if "change_status" in request.form.keys():
        change_status = int(request.form.get("change_status"))

    #在庫数が変更された場合、値を取得
    if "change_stock_id" in request.form.keys():
        change_stock = request.form.get("change_stock")
        change_stock_id = int(request.form.get("change_stock_id"))
        #在庫数の値が数字ならint型に、文字列なら"文字列"に、空欄なら""に
        if change_stock != None and change_stock != "" and change_stock.isdecimal() == True:
            change_stock = int(request.form.get("change_stock"))
        elif change_stock != None and change_stock != "" and change_stock.isdecimal() == False:
            change_stock = "文字列"
        else:
            change_stock = ""


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try :
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #常時実行するSQL
        query = "SELECT  dt.drink_id as drink_id, dt.drink_image as drink_image, dt.drink_name as drink_name, dt.price as price, st.stock as stock, dt.status as status FROM drink_table as dt LEFT JOIN stock_table as st ON dt.drink_id = st.drink_id"

        #SQL実行(在庫数やステータスの値と変更した値の比較のため)
        cursor.execute(query)

        #SQLに画像のパスを保存する
        if add_image != "" or add_image != None:
            drink_image = "../static/" + filename


        #SQLで取得した値を格納(HTMLに送るためのリスト)
        goods = []
        for (id, image, name, price, stock, status) in cursor:
            item = {"id" : id, "image" : image, "name" : name, "price" : price, "stock" : stock, "status" : status}
            goods.append(item)
            #ステータス変更ボタンの押された商品のidと同じ商品の情報を変数に格納
            if item["id"] == change_status:
                update_status = item
            #在庫数変更ボタンの押された商品のidと同じ商品の情報を変数に格納
            if item["id"] == change_stock_id:
                update_stock = item


        #商品追加のボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        if "add_drink" in request.form.keys():
            #全ての項目が入力され、値段と在庫数が整数の場合
            if (add_image != "" and add_name != "" and add_price != "" and add_number != "" and status_selector != "") and (add_number.isdecimal() == True and add_price.isdecimal() == True) and (int(add_price) >= 0 and int(add_number) >= 0) :
                drink_query = f"INSERT INTO drink_table (drink_image, drink_name, price, edit_date, update_date, status) VALUES ('{drink_image}', '{add_name}', {add_price}, LOCALTIME(), LOCALTIME(), {status_selector})"
                stock_query = f"INSERT INTO stock_table (drink_name, stock, edit_date, update_date) VALUES ('{add_name}', {add_number}, LOCALTIME(), LOCALTIME())"
                cursor.execute(drink_query)
                cursor.execute(stock_query)
                cnx.commit()
                add_message = "＊追加成功：商品が正常に追加されました"

            #条件にあっていない入力や空欄がある
            else:
                add_message = "＊追加失敗：全ての項目を条件通り入力してください"


        #在庫変更のボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        elif "change_stock_id" in request.form.keys():
            #入力欄の値が変更されたときのみデータベース更新
            if update_stock["stock"] != change_stock and change_stock != "" and (change_stock != "文字列" and change_stock != "") :
                stock_update_query_1 = f'UPDATE stock_table SET stock = {change_stock}, update_date = LOCALTIME() WHERE drink_id = {update_stock["id"]}'
                stock_update_query_2 = f'UPDATE drink_table SET update_date = LOCALTIME() WHERE drink_id = {update_stock["id"]}'
                cursor.execute(stock_update_query_1)
                cursor.execute(stock_update_query_2)
                cnx.commit()
                change_message = "＊成功：" + update_stock["name"] + "の在庫数が変更されました"

            #入力欄の値が文字列で入力されている
            elif update_stock["stock"] != change_stock and change_stock == "文字列":
                change_message = "＊エラー：在庫数の値は0以上の整数で入力してください"

            #入力欄の値が入力されていない
            elif update_stock["stock"] != change_stock and change_stock == "":
                change_message = "＊エラー：在庫数の値を入力してください"

            #入力欄の値が変更されていない
            else:
                change_message = "＊エラー：" + update_stock["name"] + "の値が変更されていません"


        #公開・非公開のボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        elif "change_status" in request.form.keys():
            #現在のステータスが公開(1)の場合、非公開(0)に変更
            if update_status["status"] == 1:
                status_update_query_1 = f'UPDATE drink_table SET status = 0 WHERE drink_id = {update_status["id"]}'
                status_update_query_2 = f'UPDATE drink_table SET update_date = LOCALTIME() WHERE drink_id = {update_status["id"]}'
                cursor.execute(status_update_query_1)
                cursor.execute(status_update_query_2)
                cnx.commit()
                change_message = "＊成功：" + update_status["name"] + "を非公開にしました"

            #現在のステータスが非公開(0)の場合、公開(1)に変更
            elif update_status["status"] == 0:
                status_update_query_1 = f'UPDATE drink_table SET status = 1 WHERE drink_id = {update_status["id"]}'
                status_update_query_2 = f'UPDATE drink_table SET update_date = LOCALTIME() WHERE drink_id = {update_status["id"]}'
                cursor.execute(status_update_query_1)
                cursor.execute(status_update_query_2)
                cnx.commit()
                change_message = "＊成功：" + update_status["name"] + "を公開にしました"


        #どのボタンも押されていない場合(最初のページを表示するがここでは何もしない)ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        else:
            pass


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
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'kaA1ybB2ucC3d2c'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名


    #変数定義ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    #購入
    my_money = ""
    select_button = ""

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
    if "buy_drink" in request.form.keys():
        my_money = request.form.get("my_money")
        select_button = request.form.get("select_button")
        #取得した値がもし文字列や数字ならdrink_idをint型にネスト(下記で条件分岐するため)
        if select_button != None and select_button != "":
            select_button = int(select_button)


    #mysqlに接続ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    try :
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()


        #いつでも実行する表示のためのSQLーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        query = "SELECT dt.drink_id as drink_id, dt.drink_image as drink_image, dt.drink_name as drink_name, dt.price as price, dt.status as status, st.stock as stock FROM drink_table as dt LEFT JOIN stock_table as st ON dt.drink_id = st.drink_id WHERE stock IS NOT NULL and status = 1"
        cursor.execute(query)


       #SQLで取得した値を格納(HTMLに送るためのリスト)ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        goods = []
        for (id, image, name, price, status, stock) in cursor:
            item = {"id" : id, "image" : image, "name" : name, "price" : price, "status" : status, "stock" : stock}
            goods.append(item)
            #商品購入ボタンの押された商品のidと同じ商品の情報を変数に格納
            if item["id"] == select_button:
                bought = item


        #商品購入ボタンが押された場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        if "buy_drink" in request.form.keys():
            #金額・商品共に数字が入力されており、足りている
            if (my_money != "" and my_money.isdecimal() == True) and select_button != None and bought != "":
                my_money = int(my_money)
                bought["price"] = int(bought["price"])
                bought["stock"] = int(bought["stock"])
                if my_money >= bought["price"] and bought["stock"] > 0 and bought["status"] != "0":
                    message = "自動販売機結果"
                    judge_money = "＊ガシャコン！！" + bought["name"] + "が買えました！＊"
                    judge_select = "<<<お釣りは" + str(my_money - bought["price"]) + "円です>>>"
                    #在庫数変更のクエリ
                    stock_update_query = f'UPDATE stock_table SET stock = {bought["stock"]-1} WHERE drink_id = "{bought["id"]}"'
                    history_query = f'INSERT INTO history_table (drink_id, order_date) VALUES ({bought["id"]}, LOCALTIME())'
                    cursor.execute(stock_update_query)
                    cursor.execute(history_query)
                    cnx.commit()
                    success = bought["image"]

                #金額・商品共に入力されているが、在庫がない
                elif my_money >= bought["price"] and bought["stock"] == 0 and bought["status"] != "0":
                    message = "自動販売機結果"
                    judge_money = "＊現在在庫がありません"

                #金額・商品共に入力されているが、金額が足りていない
                else:
                    message = "自動販売機結果"
                    judge_money = "＊お金が" + str(bought["price"] - my_money) + "円足りません"

            #金額・商品共に数字が入力されており、足りているが公開されていない
            elif (my_money != "" and my_money.isdecimal() == True) and select_button != None and bought == "":
                    message = "自動販売機結果"
                    judge_money = "＊申し訳ありません、この商品は現在お売りすることができません"


            #金額入力もしくは商品の選択が行われていない
            elif (my_money == "" or my_money.isdecimal() == False) or select_button == None:
                #金額、商品共に入力されていない
                if my_money == "" and select_button == None:
                    message = "自動販売機結果"
                    judge_money = "＊お金を投入してください"
                    judge_select = "＊商品を選択してください"

                #商品が選択されていない
                elif my_money == "":
                    message = "自動販売機結果"
                    judge_select = "＊お金を投入してください"

                #金額が入力されていない
                elif select_button == None :
                    message = "自動販売機結果"
                    judge_money = "＊商品を選択してください"

                #金額が数字ではない
                else:
                    message = "自動販売機結果"
                    judge_money = "＊金額は数字で入力してください"


        ##どのボタンも押されていない場合(最初のページを表示する)ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
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