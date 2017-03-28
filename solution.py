import requests
import os

directory = 'Source'
files = os.listdir(directory)

def translater(text, language):
    api_key = 'trnsl.1.1.20170328T084717Z.d8b2934040820452.0f0d6860daf41a6ff6c4be328efbf4f27fe68133'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    
    params = {
        'key': api_key,
        'text': text,
        'lang': language,
    }
    response = requests.get(url, params=params)
    return response.json()

translate_language = input('Language:')
if translate_language == '':
    translate_language = 'ru'
    
for file in files:
  
    with open(os.path.join(directory, file)) as f:
            text = f.readlines()

    with open('result'+file+'.txt','w') as file:
        file.write(' '.join(translater(text, translate_language)['text']))
