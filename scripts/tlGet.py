#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Tweepyライブラリのインポート
import tweepy

from auth import TwitterAuth

if __name__ == '__main__':
	try:
		auth = tweepy.OAuthHandler(TwitterAuth.consumer_key,TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token,TwitterAuth.access_token_secret)
		cursor = tweepy.Cursor
		# APIインスタンスの作成
		api = tweepy.API(auth)

		input_num = int(input('num: '))

		tweets = []
		
		for tweet in tweepy.Cursor(api.home_timeline,since_id=10000).items(input_num):
			tweets.append(tweet)
			

		for i in range(0,len(tweets)):		
			try:
				print("==============================================================================")
				print(tweets[i].created_at)
				print(tweets[i].user.name,end="")
				print(' / @' + tweets[i].user.screen_name)
				print("")
				print(tweets[i].text)				
			except:
				print("- Error -")

		print("==============================================================================")

	except tweepy.TweepError as e:
		print(e.reason)



