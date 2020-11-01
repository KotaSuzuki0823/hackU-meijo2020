import requests

def send_user_data_test():

    data = {
        'user_id': "kotasuzuki",        # 必須のキー情報，ユーザID
        'user_name': "鈴木洸太",
        'user_nic': "すずこー",
        'gender': "男",
        'user_age': int("23"),
        'places': "aichi",
        'user_tel': "08000000000",
        'can_do': "買い物"
    }

    response = requests.post('http://localhost:3000/user/registration', data)
    print(response.status_code)    # HTTPのステータスコード取得
    

if __name__ == "__main__":
    send_user_data_test()