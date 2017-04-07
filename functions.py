#coding:utf-8
#便利な関数たち

import urllib
import json

#Wikiからタイトルを取得しリスト型で返す関数
#limit : int - 取得するタイトルの上限数
def get_wiki_title(limit=10):
    url = 'http://ja.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=' + str(limit) + '&format=json'
    html = urllib.request.urlopen(url)
    jsonfile = json.loads(html.read().decode('utf-8'))
    text = []
    for i in range(limit):
        text.append(jsonfile['query']['random'][i]['title'])
    return text