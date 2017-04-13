#coding:utf-8

import requests

URL='https://slack.com/api/chat.postMessage'
TOKEN='xoxb-156491807943-54IF0PPyFEw2ptigqB7evHcu'
param={'token':TOKEN,'channel':'test','text':'testt'}

requests.post(URL,params=param)
