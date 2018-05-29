#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Tweepyライブラリのインポート
import tweepy

# 各種キーのセット
CONSUMER_KEY = 'Mesz9IOVTeGL9QFJT3y4CeVbi'
CONSUMER_SECRET = 'FnOmxZ0ySrqlkyuyXH70hi0lKfnPFmPTS1xgkoalO28qS5hb5v'
ACCESS_TOKEN = '747363066174574592-8Vp7oD9wD3soJsG4X6HzlAWv4erjeuI'
ACCESS_SECRET = '5SEve4cN3l1NGd75GaeeSGNGzYPjSWVVHxrU4DGCIQQqS'

if __name__ == '__main__':
	try:
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
		cursor = tweepy.Cursor
		# APIインスタンスの作成
		api = tweepy.API(auth)

		fav_tweet = list()

		for status in tweepy.Cursor(api.home_timeline,count=10).items():	
			print('favorite_count:' + str(status.favorite_count))
			fav_tweet.append(status)

	except tweepy.TweepError as e:
		print(e.reason)

