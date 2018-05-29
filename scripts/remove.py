#!/usr/bin/env python
#-*- coding:utf-8 -*-

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


if __name__ == "__main__":
	try:
		auth = tweepy.OAuthHandler(TwitterAuth.consumer_key,TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token,TwitterAuth.access_token_secret)
		cursor = tweepy.Cursor
		# tweepy初期化
		api = tweepy.API(auth)
		my_info = api.me()

		try:
			with codecs.open("follow_time.json", 'r', 'utf-8') as f:
				data = json.load(f)
			print("処理中...")
		except:
			print("Not file")

		destroy_index = []
		followed_count = 0
		current_time = datetime.now()
		
		for i in range(0,len(data)):
			follow_id = data[i]['user_id']
			follow_day = data[i]['created_at'].split("T",2)
			follow_day = datetime.strptime(follow_day[0], '%Y-%m-%d')

			followback = current_time - follow_day
			friendship = api.show_friendship(source_id = my_info.id, target_id = follow_id)
			if friendship[1].following:
				destroy_index.append(i)
				followed_count += 1
			if followback.days > 4 and friendship[1].following == False:
				api.destroy_friendship(follow_id)
				destroy_index.append(i)
				if len(destroy_index) > 14:
					break

		print(str(followed_count) + "人フォロバされてました")
		print(str(len(destroy_index) - followed_count) + "人removeしました")
		# removeしたアカウントの削除
		destroy_index.sort(reverse = True)
		for i in destroy_index:
			data.pop(i)

		# file上書き
		with codecs.open("follow_time.json", 'w', 'utf-8') as f:
			json.dump(data, f, default=support_datetime_default, indent=4, ensure_ascii=False)      

	except tweepy.TweepError as e:
		print(e.reason)