# LAST MODIFIED: 02/08/2017
#
# return selected data from twitter jsons
#
# NOTES: jsons collected from twitter_scraper have ' and " mixed up.
# To fix this we use the literal_eval function from the ast package
# this is a bit of a hack which should be fixed in future versions.
# 
# This script builds a pandas data frame consisting of fields of
# interest harvested from twitter data. Additional fields of interest
# should be specified in the fields_dict dictionary.


# json quote Fix: 

import ast
import pandas as pd

with open('harvest.json', mode='r') as file:	
	tweets = file.readlines()
	# convert json strings to dicts with ast.literal_eval
tweets = [ast.literal_eval(tweet) for tweet in tweets]


def get_node(path, dictionary):
	"""
	Returns contents in a dictionary of dicts found at path.
	"""
	if len(path) > 1:
		return(get_node(path[1:], dictionary[path[0]]))
	else:
		return(dictionary[path[0]])


# Some tests for get_node function

test_dict = {'a':{'b':1, 'c':2}, 'd':3}
assert get_node(['a', 'c'], test_dict) == 2
assert get_node(['d'], test_dict) == 3
assert get_node(['a'], test_dict) == {'b':1, 'c':2}


# dictionary of what fields to be put into data frame; key is column name, value is path in tweet tree

fields_dict = {'created_at':['created_at'], 
               'id_str':['id_str'], 
                 'text':['text'], 
          'screen_name':['user', 'screen_name'], 
      'followers_count':['user', 'followers_count'],
             'verified':['user', 'verified'],
        'retweet_count':['retweet_count'],
       'favorite_count':['favorite_count']
    }


def build_df(fields_dict, tweets):
	"""
	Returns a pandas data frame from tweets data with columns specified by fields dictionary.
	"""
	df_dict = {}
	for key, path in fields_dict.items():
		df_dict[key] = [get_node(path, tweet) for tweet in tweets]	
	return(pd.DataFrame(df_dict))
	

# build tweets_df data frame for data analysis

tweets_df = build_df(fields_dict, tweets)
