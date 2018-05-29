#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Tweepyライブラリのインポート
import tweepy

from auth import TwitterAuth

def search_tweet():

	input_string = input('searchWords: ')
	
	div = input_string.split()
	mergerd_string = " AND ".join(div)
	searchwords=[mergerd_string]

	tweets = []	
	for tweet in tweepy.Cursor(api.search,q=searchwords).items(50):
		if isinstance(tweet.in_reply_to_status_id, int):
			tweets.append(api.get_status(tweet.in_reply_to_status_id))
	
	return tweets
	

if __name__ == '__main__':
	try:
		auth = tweepy.OAuthHandler(TwitterAuth.consumer_key,TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token,TwitterAuth.access_token_secret)
		cursor = tweepy.Cursor
		# APIインスタンスの作成
		api = tweepy.API(auth)

		tweets = search_tweet()


		for i in range(0,len(tweets)):
			try:
				print("==============================================================================")
				print(tweets[i].text)	
			except:
				print("- Error -")


		print("==============================================================================")

	except tweepy.TweepError as e:
		print(e.reason)

