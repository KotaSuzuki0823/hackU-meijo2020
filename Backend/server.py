import os
from flask import Flask, jsonify, abort, make_response, request
from azure.cosmosdb.table.tableservice import TableService
import hashlib

# Azure Table Strageを使用
strage_key = os.getenv('AZURE_STRAGE_KEY')
strage_name = os.getenv('AZURE_STRAGE_NAME')

AZURE_TABLENAME_USER = 'user'
AZURE_TABLENAME_HELP = 'help'

api = Flask(__name__)

@api.route('/user/registration', methods=['POST'])
def user_registration():
    '''
    ユーザー登録
    :return:
    '''
    try:
        # クエストからユーザ情報を抽出し辞書型に変換
        userdata = {
            'PartitionKey': hashlib.sha256(request.form["user_id"]).hexdigest(),  # 必須のキー情報,user_idをSHA256でハッシュ化
            'RowKey': request.form["user_id"],        # 必須のキー情報，ユーザID
            'user_name': request.form["user_name"],
            'user_nic': request.form["user_nic"],
            'gender': request.form["gender"],
            'user_age': int(request.form["user_age"]),
            'places': request.form["places"],
            'user_tel': request.form["user_tel"],
            'can_do': request.form["can_do"]
        }

        # DBへユーザ情報を追加
        TableService.insert_or_replace_entity(AZURE_TABLENAME_USER, userdata)   
    except:
        abort(500)

@api.route('/user/get', methods=['GET'])
def get_user():
    '''
    ユーザー情報の応答
    :return:
    '''
    try:
        # クエリ文字列から検索するエリアを指定
        # http://ocalhost:3000/user/get?area=aichi&num=1
        user_area = request.args.get('area')

        # 辞書表示に使うインデックス
        number = request.args.get('num') - 1

        # テーブルからエリア条件に一致するユーザを取得
        userlist = TableService.query_entities(
            table_name=AZURE_TABLENAME_USER,
            places=user_area
        )

        if number < len(userlist):
            user = userlist[number]

            result = {
            "result":True,
            "data":{
                "userId":user.userId,
                "user_name":user.name,
                "user_gender":user.gender,
                "user_age":user_age
                }
            }

        else:
            print("これ以上はありません．")
            result = {
                "result":False
            }

    except:
        abort(500)

    return make_response(jsonify(result))

def get_user_by_userid(userid):
    '''
    useridから情報を取得
    :return:useridに対応するユーザ情報
    '''
    userdata = table_service.get_entity(
        table_name='user',
        partition_key=hashlib.sha256(request.form["user_id"]).hexdigest(),
        row_key=userid)
    
    return userdata

@api.route('/help_offer/registration', methods=['POST'])
def help_offer_registration():
    '''
    お助け情報の登録
    :return:
    '''
    try:
        helpdata = {
            'PartitionKey': hashlib.sha256(request.form["user_id"]).hexdigest(),  # 必須のキー情報,user_idをSHA256でハッシュ化
            'RowKey': request.form["user_id"],        # 必須のキー情報，ユーザID
            'user_name': request.form["outline"],
            'user_nic': request.form["detail"],
            'can_do': request.form["can_do"]
        }
        # お助け情報の追加
        TableService.insert_or_replace_entity(AZURE_TABLENAME_HELP, helpdata)  
    except:
        abort(500)

@api.route('/help_offer/get', methods=['GET'])
def get_help_offer():
    '''
    お助け情報の送信
    :return:
    '''
    try:
        #DBへユーザ情報を追加

    except:
        abort(500)


@api.errorhandler(404)
def not_found(error):
    '''
    404エラー
    :return:
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
