from slackbot.bot import respond_to
from slackbot.bot import listen_to
import urllib
import json
import random
import datetime


#######################################################################
#                       respond_to はここに書く                          #
#######################################################################

@respond_to('乱数')
def rnd(message):
    message.reply(str(random.randint(0,99)))

@respond_to('今何時')
def print_now(message):
    todaydetail = datetime.datetime.today()
    message.reply("%s" % todaydetail)

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

@respond_to('たかっしー')
def takashima(message):
    message.reply('にゃっはー！！')

@respond_to('わたり')
def watari(message):
    kuji = ["大吉", "吉", "中吉", "小吉", "末吉", "凶", "大凶", "矢鋪", "中古"]
    message.reply('今日のわたりは' + str(random.choice(kuji)) + 'ですにゃ')

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


######################################################################
#                       listen_to はここに書く                          #
######################################################################

@listen_to('ねこ')
@listen_to('猫')
def neko(message):
    message.send('にゃあ！')