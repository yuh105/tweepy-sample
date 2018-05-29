#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tweepy
import json
import codecs
from datetime import datetime
from datetime import timedelta

from auth import TwitterAuth

#jsonのdatetimeエラー対策
def support_datetime_default(o):
    if isinstance(o, datetime):
        return o.isoformat()
    raise TypeError(repr(o) + " is not JSON serializable")

def search_tweet():

	input_num = int(input('num: '))
	input_string = input('searchWords: ')
	div = input_string.split()
	mergerd_string = " AND ".join(div)
	searchwords=[mergerd_string]

	tweets = []
	for tweet in tweepy.Cursor(api.search,q=searchwords).items(input_num):
		tweets.append(tweet)	
	return tweets

def follow():

	follow_time = []
	follow_count = 0
	already_followed = 0
	
	print("")
	print("following...")
	
	for i in range(0,len(tweets)):
		friendship = api.show_friendship(source_id = my_info.id, target_id = tweets[i].user.id)
		if friendship[0].following:
			already_followed += 1
		else:
			follow_count += 1
			tweets[i].created_at += timedelta(hours=9)
			api.create_friendship(tweets[i].user.id)
			time_info = {
				u"user_id": tweets[i].user.id,
				u"created_at": tweets[i].created_at,
			}
			follow_time.append(time_info)
	
	print(str(follow_count) + "人フォロ-したよ")	
	return follow_time


def save_json(follow_time):
	# jsonファイルにフォローした日時を保存
	try:
		with codecs.open("follow_time.json", 'r', 'utf-8') as f:
			data = json.load(f)
		follow_time.extend(data)
		print("Save file")
	except:
		print("New file")

	with codecs.open("follow_time.json", 'w', 'utf-8') as f:
		#収集されたデータをJSONファイルに格納する
		json.dump(follow_time, f, default=support_datetime_default, indent=4, ensure_ascii=False)      


if __name__ == "__main__":
	try:
		auth = tweepy.OAuthHandler(TwitterAuth.consumer_key,TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token,TwitterAuth.access_token_secret)
		cursor = tweepy.Cursor
		# tweepy初期化
		api = tweepy.API(auth)
		my_info = api.me()

		tweets = search_tweet()
		follow_time = follow()			
		save_json(follow_time)
	
	except tweepy.TweepError as e:
		print(e.reason)
