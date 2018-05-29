#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tweepy
import sqlite3
import re

from datetime import timedelta
from auth import TwitterAuth

def search_tweet():
	input_num = int(input('num: '))

	tweets = []	
	for tweet in tweepy.Cursor(api.home_timeline).items(input_num):
		tweets.append(tweet)
	
	return tweets
	

if __name__ == '__main__':
	try:
		auth = tweepy.OAuthHandler(TwitterAuth.consumer_key,TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token,TwitterAuth.access_token_secret)
		cursor = tweepy.Cursor
		# APIインスタンスの作成
		api = tweepy.API(auth)

		conn = sqlite3.connect('home_ex.db')
		c = conn.cursor()
		
		tweets = search_tweet()

		for i in range(0,len(tweets)):		
			try:
				if(len(tweets[i].text) < 50):
					if re.search(r'@| http| RT',tweets[i].text) is None:
						tweet_text = tweets[i].text
						tweets[i].created_at += timedelta(hours=9)
						tweet_text = re.sub(r'\n|。'," ",tweet_text)
						tweet_text = tweet_text.split()
						for text in tweet_text:
							print(tweets[i].created_at,end="")
							print(" / " + text)
							c.execute("insert into texts values(?, ?, ?)",(text, tweets[i].created_at, tweets[i].id))
			except:
				print("- Error -")
	
		conn.commit()
		conn.close()

	except tweepy.TweepError as e:
		print(e.reason)

