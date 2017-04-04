from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to('疲れた')
@respond_to('つかれた')
def cheer(message):
    message.reply('ファイト!')

@respond_to('ただいま')
def welcome_back(message):
    message.reply('おかえりなさい')

@listen_to('おはよう')
def good_morning(message):
    message.send('にゃあ')


@listen_to('天気')
@listen_to('晴れ')
@listen_to('雨')
@respond_to('天気')
def weather(message):
    import urllib
    import json

    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    # '130010'とすると東京の情報を取得してくれる
    # ここを変えれば任意の地域の天気情報を取得できる
    city_id = '130010'

    html = urllib.request.urlopen(url + city_id)
    jsonfile = json.loads(html.read().decode('utf-8'))
    text = jsonfile['description']['text']

    message.send(text)
