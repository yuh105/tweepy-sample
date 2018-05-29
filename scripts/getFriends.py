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
		my_info = api.me()

		friends_ids = []

		for friend_id in tweepy.Cursor(api.friends_ids, user_id=my_info.id).items():
			friends_ids.append(friend_id)

		# 100IDsずつに詳細取得
		for i in range(0, len(friends_ids), 100):
			for user in api.lookup_users(user_ids=friends_ids[i:i+100]):
				try:
					print (user.name + " / @" + user.screen_name)
					friendship = api.show_friendship(source_id = my_info.id, target_id =user.id)
					print(friendship[1].following)
				except:
					print("- Error -")

	except tweepy.TweepError as e:
		print(e.reason)
