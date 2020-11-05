'''
    Azure上で動かすバックエンドサーバプログラム
'''
import hashlib
import os

from azure.cosmosdb.table.tableservice import TableService
from flask import Flask, abort, jsonify, make_response, request

# システム変数(環境変数)から取得
STORAGE_KEY = os.getenv('AZURE_STRAGE_KEY')
STORAGE_NAME = os.getenv('AZURE_STRAGE_NAME')

AZURE_TABLENAME_USER = 'user'
AZURE_TABLENAME_HELP = 'help'

# REAT api用
app = Flask(__name__)

# Azure Table Serviceに接続
TABLE_SERVICE = TableService(account_name=STORAGE_NAME, account_key=STORAGE_KEY)

@app.route('/user/registration', methods=['POST'])
def user_registration():
    '''
    ユーザー登録
    :return:
    '''
    print("user registration")
    try:
        # クエストからユーザ情報を抽出し辞書型に変換
        userdata = {
            # 必須のキー情報,user_idをSHA256でハッシュ化
            'PartitionKey': hashlib.sha256(request.form["user_id"].encode('utf-8')).hexdigest(),
            'RowKey': request.form["user_id"],   # 必須のキー情報，ユーザID
            'user_name': request.form["user_name"],
            'user_nic': request.form["user_nic"],
            'gender': request.form["gender"],
            'user_age': int(request.form["user_age"]),
            'places': request.form["places"],
            'user_address': request.form["user_address"],
            'user_tel': request.form["user_tel"],
            'can_do': request.form["can_do"]
        }
        print(userdata)

        # DBへユーザ情報を追加
        TABLE_SERVICE.insert_or_replace_entity(AZURE_TABLENAME_USER, userdata)
        print("send data to azure")

        result = {
            "result":True,
            "data":{
                "userId":userdata['RowKey'],
                "user_hash":userdata["PartitionKey"]
            }
        }

    except Exception as exceptvar:
        print("except:"+ str(exceptvar))
        abort(500)

    return make_response(jsonify(result))

@app.route('/user/get', methods=['GET'])
def get_user():
    '''
    ユーザー情報の応答
    :return:
    '''
    try:
        # クエリ文字列から検索するエリアを指定
        # http://localhost:3000/user/get?area=aichi&num=1
        user_area = request.args.get('area')

        # 辞書表示に使うインデックス
        number = int(request.args.get('num')) - 1

        # テーブルからエリア条件に一致するユーザを取得
        userlist = TABLE_SERVICE.query_entities(
            table_name=AZURE_TABLENAME_USER,
            filter="places eq " + user_area
        )

        result = {}
        for i in range(8):
            if (i + (number*8)) < len(userlist):
                user = userlist[i + (number*8)]

                result[i] = {
                    "data":{
                        "userId":user["RowKey"],
                        "user_name":user['user_name'],
                        "user_gender":user['gender'],
                        "user_age":user['user_age']
                    }
                }

            else:
                print("これ以上はありません．")
                result[i] = {
                    "data":None
                }

    except Exception as except_var:
        print("except:"+except_var)
        abort(500)

    return make_response(jsonify(result))

@app.route('/help_offer/registration', methods=['POST'])
def help_offer_registration():
    '''
    お助け情報の登録
    :return:
    '''
    try:
        helpdata = {
            # 必須のキー情報,user_idをSHA256でハッシュ化
            'PartitionKey': hashlib.sha256(request.form["user_id"]).hexdigest(),
            # 必須のキー情報，ユーザID
            'RowKey': request.form["help_id"],
            'outline': request.form["outline"],
            'detail': request.form["detail"],
            'can_do': request.form["can_do"]
        }

        # お助け情報の追加
        TABLE_SERVICE.insert_or_replace_entity(AZURE_TABLENAME_HELP, helpdata)
        print("send data to azure")

        result = {
            "result":True,
            "data":{
                "helpId":helpdata['RowKey'],
                "help_hash":helpdata["PartitionKey"]
            }
        }

    except Exception as except_var:
        print("except:"+except_var)
        abort(500)

    return make_response(jsonify(result))

@app.route('/help_offer/get', methods=['GET'])
def get_help_offer():
    '''
    お助け情報の送信
    :return:
    '''
    pass

@app.errorhandler(404)
def not_found(error):
    '''
    404エラー
    :return:
    '''
    print(error)
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
