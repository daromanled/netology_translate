import requests
import os

if __name__ == "__main__":

    def translater(text, language):
        API_KEY = 'trnsl.1.1.20170328T084717Z.d8b2934040820452.0f0d6860daf41a6ff6c4be328efbf4f27fe68133'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        
        params = {
            'key': API_KEY,
            'text': text,
            'lang': language,
        }
        response = requests.get(URL, params=params)
        return response.json()  

    start_language = input('Start_language:')

    translate_language = input('Translate_language:')
    if translate_language == '':
        translate_language = 'ru'
        
    file = input('Name of file:')
    file_result = input('Name of file with result:')
    
    with open(file + '.txt', 'r') as f:
        text = f.readlines()
    
    pair_of_languages = start_language + '-' + translate_language
    
    with open(file_result + '.txt', 'w') as file_with_result:
        file_with_result.write(' '.join(translater(text, pair_of_languages)['text']))
