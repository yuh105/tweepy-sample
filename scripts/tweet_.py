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

input_str = input('tweet!: ')
print('...')
api.update_status(input_str)