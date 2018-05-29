#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Tweepyライブラリのインポート
import tweepy
from auth import TwitterAuth


if __name__ == "__main__":
	try:
		auth = tweepy.OAuthHandler(TwitterAuth.consumer_key,TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token,TwitterAuth.access_token_secret)
		cursor = tweepy.Cursor
		# tweepy初期化
		api = tweepy.API(auth)
		my_info = api.me()

		followers_id = api.followers_ids(my_info.id)
		friends_id = api.friends_ids(my_info.id)
	
		new_followBack_count = 0
		print("following..")
		for follower in followers_id:
			if follower not in friends_id:
				new_followBack_count += 1
				api.create_friendship(follower)
				
		if new_followBack_count == 0:
			print('新しいフォロワーはいなかったよ')
		else:
			print(str(new_followBack_count) + '人フォロバしたよ')

	except tweepy.TweepError as e:
		print(e.reason)
