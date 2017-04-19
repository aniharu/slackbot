from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random
import requests
import datetime
import urllib
import json
import functions
import threading
import re


def multiple_replace(text,adict):
    """ 
    一度に複数の文字列を置換する. 
    - text中からディクショナリのキーに合致する文字列を探し、対応の値で置換して返す 
    """
    # マッチさせたいキー群を正規表現の形にする e.g) (a1|a2|a3...)
    rx = re.compile('|'.join(map(re.escape,adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

#######################################################################
#                       respond_to はここに書く                          #
#######################################################################


@respond_to('てんき')
def weather(message):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    # '130010'とすると東京の情報を取得してくれる
    # ここを変えれば任意の地域の天気情報を取得できる
    city_id = '140010'

    html = urllib.request.urlopen(url + city_id)
    jsonfile = json.loads(html.read().decode('utf-8'))
    text = jsonfile['description']['text']

    adict = {
        "います":"いるにゃ",
        "あります":"あるにゃ",
        "なり":"にゃり",
        "でしょう":"にゃ",
        "です": "にゃ",
        "ください": "にゃ",
        "なる": "にゃる",
        "。": "。\n",
    }

    text = multiple_replace_re(text,adict)

######################################################################
#                       listen_to はここに書く                          #
######################################################################
