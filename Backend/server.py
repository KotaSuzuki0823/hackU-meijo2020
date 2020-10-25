import os
from flask import Flask, jsonify, abort, make_response, request
from azure.cosmosdb.table.tableservice import TableService
import hashlib

# Azure Table Strageを使用
strage_key = os.getenv('AZURE_STRAGE_KEY')
strage_name = os.getenv('AZURE_STRAGE_NAME')

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
            'PartitionKey': hashlib.sha256(request.form["user_id"]).hexdigest(),  # 必須のキー情報
            'RowKey': request.form["user_id"],        # 必須のキー情報
            'user_name': request.form["user_name"],
            'user_nic': request.form["user_nic"],
            'gender': request.form["gender"],
            'user_age': request.form["user_age"],
            'places': request.form["places"],
            'user_tel': request.form["user_tel"],
            'can_do': request.form["can_do"]
        }

        # DBへユーザ情報を追加
        TableService.insert_or_replace_entity('user', userdata)   
    except:
        abort(404)

@api.route('/user/get', methods=['GET'])
def get_user():
    '''
    ユーザー情報の応答
    :return:
    '''
    try:
        # DBへユーザ情報を追加

    except:
        abort(404)
    
    result = {
        "result":True,
        "data":{
            "userId":user.userId,
            "name":user.name,
            "caption":user.caption,
            "old":int(user.old)
            }
        }

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
        # お助け情報の追加
        TableService.insert_or_replace_entity('otasuke', otasukedata)  
    except:
        abort(404)

@api.route('/help_offer/get', methods=['GET'])
def get_help_offer():
    '''
    お助け情報の送信
    :return:
    '''
    try:
        #DBへユーザ情報を追加

    except:
        abort(404)


@api.errorhandler(404)
def not_found(error):
    '''
    404エラー
    :return:
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
