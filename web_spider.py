import requests
import json

def translate(keyword):
    url = 'https://fanyi.baidu.com/sug'

    data = {
        'kw' : keyword
    }

    res = requests.post(url, data = data)

    str_json = res.text

    myjson = json.loads(str_json)
    info = myjson['data'][0]['v']
    print(info)

if __name__ == '__main__':
    while True:
        keyword = input('请输入翻译的单词：')
        if keyword == 'q':
            break
        translate(keyword)