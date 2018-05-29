#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Tweepyライブラリのインポート
import tweepy

# 各種キーのセット
CONSUMER_KEY = 'Mesz9IOVTeGL9QFJT3y4CeVbi'
CONSUMER_SECRET = 'FnOmxZ0ySrqlkyuyXH70hi0lKfnPFmPTS1xgkoalO28qS5hb5v'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = '747363066174574592-8Vp7oD9wD3soJsG4X6HzlAWv4erjeuI'
ACCESS_SECRET = '5SEve4cN3l1NGd75GaeeSGNGzYPjSWVVHxrU4DGCIQQqS'
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# APIインスタンスの作成
api = tweepy.API(auth)

# datetime / locate モジュールのインポート
import datetime

today = datetime.date.today()
heisei = today.year - 1988
print(heisei)
print("今日は" + str(today.year)  +"年" + str(today.month) + "月" + str(today.day) + "日です")

#api.update_status("今日は" + str(today.year)  +"年" + str(today.month) + "月" + str(today.day) + "日です")
print('Done!')
