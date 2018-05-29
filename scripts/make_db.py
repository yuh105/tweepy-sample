#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sqlite3

if __name__ == '__main__':

	# Connect database
	#conn = sqlite3.connect('example.db')
	conn = sqlite3.connect('home_ex.db')

	c = conn.cursor()
	# Create table

#	c.execute("create table texts(text,time)")
	c.execute("create table texts(text,time,id)")

	conn.close()