#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tweepy
import sqlite3
import re

from datetime import timedelta
from auth import TwitterAuth

def search_tweet():
	input_num = int(input('num: '))
	input_string = input('searchWords: ')
	
	div = input_string.split()
	mergerd_string = " + ".join(div) + " +-http +-RT +-https"
	searchwords=[mergerd_string]

	tweets = []	
	for tweet in tweepy.Cursor(api.search,q=searchwords).items(input_num):
		tweets.append(tweet)
	
	return tweets
	

if __name__ == '__main__':
	try:
		auth = tweepy.OAuthHandler(TwitterAuth.consumer_key,TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token,TwitterAuth.access_token_secret)
		cursor = tweepy.Cursor
		# APIインスタンスの作成
		api = tweepy.API(auth)

		conn = sqlite3.connect('example.db')
		c = conn.cursor()
		
		tweets = search_tweet()

		for i in range(0,len(tweets)):		
			try:
				if(len(tweets[i].text) < 50):
					if "@" in tweets[i].text:
						print("@ tweet")
					else:
						tweet_text = tweets[i].text
						tweets[i].created_at += timedelta(hours=9)
						tweet_text = re.sub(r'\n|。'," ",tweet_text)
						tweet_text = tweet_text.split()
						for text in tweet_text:
							print(tweets[i].created_at,end="")
							print(" / " + text)
							c.execute("insert into texts values(?, ?)",(text, tweets[i].created_at))
			except:
				print("- Error -")

		
		conn.commit()
		conn.close()

	except tweepy.TweepError as e:
		print(e.reason)

