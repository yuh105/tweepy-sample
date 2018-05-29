#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Tweepyライブラリのインポート
import tweepy
import random
import sqlite3

from janome.tokenizer import Tokenizer
from auth import TwitterAuth

if __name__ == '__main__':
	try:
		auth = tweepy.OAuthHandler(TwitterAuth.consumer_key,TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token,TwitterAuth.access_token_secret)
		cursor = tweepy.Cursor
		# APIインスタンスの作成
		api = tweepy.API(auth)

		stateTable = {}

		conn = sqlite3.connect('example.db')
		c = conn.cursor()

		c.execute("SELECT text, time FROM texts")
		for text, time in c.fetchall():
			print(time +" / "+ text)

			t = Tokenizer()
			tokens = t.tokenize(text)

			# Create table
			w1 = w2 =  ""

			for word in tokens:
				if (w1, w2) not in stateTable:
					stateTable[(w1,w2)] = []
				stateTable[(w1,w2)].append(word.surface)
				w1, w2 = w2, word.surface

			if (w1, w2) not in stateTable:
				stateTable[(w1, w2)] = []
			stateTable[(w1, w2)].append("")

		print(stateTable)
		print("======================================================================")
		conn.close()


		w1 = w2 = ""
		sentence = ""

		for i in range(1000):
			values = stateTable[(w1, w2)]
			index = random.randint(0, len(values) - 1)
			sentence += values[index]
			if values[index] == "":
				break
			w1, w2 = w2, values[index]

		print (sentence,end="")
	
	except tweepy.TweepError as e:
		print(e.reason)

