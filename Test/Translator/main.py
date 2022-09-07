import requests
from clear import clear


while True:
    try:
        text = input('Enter english text: ')
    except:
        print('\nEntered wrong data, please re-enter it!')
        clear()
        continue
    try:
        int(text)
    except:
        clear('wait')
        break

url = f"https://translate.yandex.ru/?lang=en-ru&text={text}"
res = requests.get(url)
if res.status_code == 200:
    print(res.headers)
else:
    print('Sorry, can`t connect to server :(')
    raise SystemExit
