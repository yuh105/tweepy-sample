#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Tweepyライブラリのインポート

import tweepy
import json
import codecs
from datetime import datetime

from auth import TwitterAuth

#jsonのdatetimeエラー対策
def support_datetime_default(o):
    if isinstance(o, datetime):
        return o.isoformat()
    raise TypeError(repr(o) + " is not JSON serializable")


if __name__ == '__main__':
	try:
		auth = tweepy.OAuthHandler(TwitterAuth.consumer_key,TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token,TwitterAuth.access_token_secret)
		cursor = tweepy.Cursor
		# APIインスタンスの作成
		api = tweepy.API(auth)

		input_num = int(input('num: '))
		input_string = input('searchWords: ')
	
		div = input_string.split()
		mergerd_string = " AND ".join(div)
		searchwords=[mergerd_string]

		tweets = []
		
		for tweet in tweepy.Cursor(api.search,q=searchwords).items(input_num):
			 person = {
                u"user_id": tweet.user.id,
                u"screen_name": tweet.user.screen_name,
                u"description": tweet.user.description,
				u"created_at": tweet.created_at,
                u"text": tweet.text
			 }
			 tweets.append(person)

		try:
			with codecs.open("test.json", 'r', 'utf-8') as f:
				data = json.load(f)
			tweets.extend(data)
			print("done")
		except:
			print("New file")

		with codecs.open("test.json", 'w', 'utf-8') as f:
		   #収集されたデータをJSONファイルに格納する
			json.dump(tweets, f, default=support_datetime_default, indent=4, ensure_ascii=False)      

	except tweepy.TweepError as e:
		print(e.reason)

