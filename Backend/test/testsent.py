import requests

def send_user_data_test():

    data = {
        'trackId': "12345"
    }

    response = requests.post('http://192.168.92.4:3000/trackingnumber/registration', data)
    re = response.json()    # HTTPのステータスコード取得
    print(re["result"])

if __name__ == "__main__":
    send_user_data_test()