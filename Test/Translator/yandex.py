import requests

text = 'text'

url = f"https://translate.api.cloud.yandex.net/translate/v2/translate"
res = requests.get(url, params={'sourceLanguageCode': 'en',
    'targetLanguageCode': 'ru',
    'texts': text})
print(res)
