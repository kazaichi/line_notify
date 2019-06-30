import requests

def lineNotify(message):
    line_notify_token = 'LINEで取得したトークン'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token} 
    requests.post(line_notify_api, data=payload, headers=headers)

if __name__ == "__main__":
    message = "テスト"
    lineNotify(message)