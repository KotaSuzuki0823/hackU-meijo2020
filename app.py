import hashlib
import os
import time
from flask import *
from azure.cosmosdb.table.tableservice import TableService

app = Flask(__name__, static_folder='static')

# システム変数(環境変数)から取得
STORAGE_KEY = os.getenv(
    'AZURE_STRAGE_KEY',
    None
    )

STORAGE_NAME = os.getenv('AZURE_STRAGE_NAME', 'haku2020')

AZURE_TABLENAME_USER = 'user'
AZURE_TABLENAME_HELP = 'help'

# Azure Table Serviceに接続
TABLE_SERVICE = TableService(account_name=STORAGE_NAME, account_key=STORAGE_KEY)

URL = os.getenv('AZURE_URL', 'http://localhost:5000/')

@app.route("/", methods=['GET', 'POST'])
def main_page():
    return render_template("index.html", profile_url=URL+'profile', help_url=URL+'help', matching_url=URL+'matching')

@app.route("/profile", methods=["GET", "POST"])
def profilepage():
    return render_template("profile.html")

@app.route("/help", methods=["GET", "POST"])
def helppage():
    return render_template("help.html")

@app.route("/matching", methods=["GET", "POST"])
def matchingpage():
    return render_template("matching.html")

@app.route('/user/registration', methods=['POST'])
def user_registration():
    '''
    ユーザー登録
    :return:
    '''
    user_address_form = request.form["user_address"]
        if user_address_form == None:
            user_address_form=""
    try:
        # クエストからユーザ情報を抽出し辞書型に変換
        userdata = {
            # 必須のキー情報,user_idをSHA256でハッシュ化
            'PartitionKey': hashlib.sha256(request.form["user_name"].encode('utf-8')).hexdigest(),
            'RowKey': request.form["user_name"],   # 必須のキー情報，ユーザID
            'user_name': request.form["user_name"],
            'user_nic': request.form["user_nic"],
            'gender': request.form["gender"],
            'user_age': request.form["user_age"],
            'places': request.form["places"],
            'user_address': user_address_form,
            'user_tel': request.form["user_tel"],
            'can_do': request.form["can_do"]
        }
        # DBへユーザ情報を追加
        TABLE_SERVICE.insert_or_replace_entity(AZURE_TABLENAME_USER, userdata)

        result = {
            "result":True,
        }

    except Exception as exceptvar:
        print("except:"+ str(exceptvar))
        result = {
            "result":False,
        }
        abort(500)
    
    make_response(jsonify(result))

    return redirect(URL)

@app.route('/help/registration', methods=['POST'])
def help_registration():
    '''
    お助け情報登録
    :return:
    '''
    try:

        detail = request.form["detail"]
        if detail == None:
            detail=""

        # クエストからユーザ情報を抽出し辞書型に変換
        helpdata = {
            # 必須のキー情報,user_idをSHA256でハッシュ化
            'PartitionKey': hashlib.sha256(str(int(time.time())).encode('utf-8')).hexdigest(),
            'RowKey': str(int(time.time())),   # 必須のキー情報，ユーザID
            'date': request.form["date"],
            'time': request.form["time"],
            'how_long': request.form["how_long"],
            'outline': request.form["outline"],
            'detail': detail
        }

        # DBへユーザ情報を追加
        TABLE_SERVICE.insert_or_replace_entity(AZURE_TABLENAME_HELP, helpdata)

        result = {
            "result":True,
        }

    except Exception as exceptvar:
        print("except:"+ str(exceptvar))
        result = {
            "result":False,
        }
        abort(500)

    make_response(jsonify(result))

    return redirect(URL)

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)
