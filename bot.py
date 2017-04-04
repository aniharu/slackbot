#coding:utf-8
#pycharm access test by jackee777
import requests

URL='https://slack.com/api/chat.postMessage'
TOKEN='xoxb-156491807943-Zp2XO0yH9KGxO4wcR3IZc0hY'
param={'token':TOKEN,'channel':'test','text':'testt'}

requests.post(URL,params=param)
