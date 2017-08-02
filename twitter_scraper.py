# twitter scraper to pull data from twitter API
# Mostly based off of tweepy's getting started tutorial
# http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html
# Marco Bonzanini's tutorial
# https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/ 
# and Hugo Bowne-Anderson's datacamp course
#
# Some notes:
# Data read from twitter's public rest api., which draws from a random subset
# of all tweets. For true access need the firehose api.
# Multiple twitter API's
# REST API used for tweepy tutorial used to read and write twitter data


# import necessary packages

import tweepy
import json


# API keys and secrets (replace 'xxxx' with actual keys and secrets)

consumer_key = 'xxxx'
consumer_secret = 'xxxx'
access_token = 'xxxx'
access_token_secret = 'xxxx'

			
# build tweepy API object

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# find tweets matching query; store in file at file_path

def make_query(query, file_path, start_date=None, end_date=None):
	"""
	Returns as many tweets matching query as api will allow
	and writes them to specified file. To get older tweets
	use start and end dates.
	"""
	cursor = tweepy.Cursor(api.search, q=query, lang='en', since=start_date, until=end_date)
	with open(file_path, mode='a') as file:
		for status in cursor.items():
			file.write(str(status._json) + '\n')


def make_query_window(query, file_path, date):
	"""
	Badly written wrapper for making calls to recent past. Doesn't change months or
	do necessary modular arithmetic. Don't use this.
	"""
	start_date = '2017-07-' + str(date)
	end_date = '2017-07-' + str(date + 1)
	return make_query(query, file_path, start_date, end_date)
	
  
# make a query and store in file
# searches for tweets containing 'Kardashian' and saves them to a file 'harves.json'
 
make_query('Kardashian', 'harvest.json', '2017-07-27', '2017-07-28')
#make_query_window('Kardashian', 'harvest.json', 27)
