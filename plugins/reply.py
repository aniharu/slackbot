from slackbot.bot import respond_to
from slackbot.bot import listen_to
import urllib
import json

@respond_to('疲れた')
@respond_to('つかれた')
def cheer(message):
    message.reply('ファイト!')

@respond_to('ただいま')
def welcome_back(message):
    message.reply('おかえりにゃあ')

@respond_to('おはよう')
def good_morning(message):
    message.reply('にゃあ')

@listen_to('ねこ')
@listen_to('猫')
def neko(message):
    message.send('にゃあ！')


@listen_to('天気')
@listen_to('晴れ')
@listen_to('雨')
@respond_to('天気')
def weather(message):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    # '130010'とすると東京の情報を取得してくれる
    # ここを変えれば任意の地域の天気情報を取得できる
    city_id = '140010'

    html = urllib.request.urlopen(url + city_id)
    jsonfile = json.loads(html.read().decode('utf-8'))
    text = jsonfile['description']['text']
    text = text.replace('ます。','るにゃ。')\
        .replace('でしょう。', 'にゃ。')\
        .replace('です。', 'にゃ。')\
        .replace('ください。', 'にゃ。')\
        .replace('るため、', 'て、')
    message.send(text)


