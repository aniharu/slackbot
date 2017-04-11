from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random
import datetime
import urllib
import json
import functions
import threading

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

@respond_to('うらない')
def fortune(message):
    kuji = ["大吉", "中吉", "小吉",  "凶", "大凶", "冥府破滅凶", "中古"]
    message.reply('今日の運勢は' + str(random.choice(kuji)) + 'ですにゃ')

@respond_to('天気')
def weather(message):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    # '130010'とすると東京の情報を取得してくれる
    # ここを変えれば任意の地域の天気情報を取得できる
    city_id = '140010'

    html = urllib.request.urlopen(url + city_id)
    jsonfile = json.loads(html.read().decode('utf-8'))
    text = jsonfile['description']['text']
    text = text.replace('\n','')\
        .replace('います','いるにゃ') \
        .replace('あります', 'あるにゃ') \
        .replace('なり', 'にゃり') \
        .replace('でしょう','にゃ') \
        .replace('です', 'にゃ') \
        .replace('ください', 'にゃ')\
        .replace('なる', 'にゃる')\
        .replace('。','。\n')
    message.send(text)

@respond_to('なにしているの')
def wikipedia(message):
    text=functions.get_wiki_title()
    main_text = "今日は" + text[0] + 'で' + text[1] + 'と一緒に' + text[2] + 'をしているにゃ.'
    message.send(main_text)

@respond_to('ムスカ')
def timer(message):
    message.send('3分間待ってにゃる！')
    def hello():
        message.send('時間にゃ！答えを聞こう！')
    timer = threading.Timer(100, hello)
    timer.start()



######################################################################
#                       listen_to はここに書く                          #
######################################################################

@listen_to('ねこ')
@listen_to('猫')
def neko(message):
    message.send('にゃあ！')