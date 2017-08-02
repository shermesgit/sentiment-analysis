# Sentiment Analysis
(sentiment-analysis)
Attempt to implement a simple sentiment analysis using twitter.

This project is an attempt to implement some simple sentiment analysis to predict stock market value based off of toe prevelence of keywords on twitter. Specifically, we implement the Kardashian Theory of sentiment analysis. The frequency of tweets about members of the Kardashian and Jenner families may be used as a general proxy for the mood of the public: more Kardashian-centric tweets means the public is more carefree, which means the economy should be doing well.

As a first step, we put this theory to the test and quantify the association between stock value and various measures of the Kardashianness of the twittersphere. Later we intend to implement a (likely very innacurate) regressor for predicting stock prices. 

In case this isn't clear from the get-go, this proposal is a joke. The code however, is serious.

# What's Included
This repository contains the following files:
  <ol>
    <li><b>README.md:</b> This file. It is a readme. </li>
    <li><b>twitter_scraper.py:</b> A rudimentary twitter scraper using tweepy. At the moment, it scans the twitter api for tweets containing the keyword 'Kardashian' and saves them in json format to an external file 'harvest.json'.</li>
    <li><b>build_dataframe.py:</b> Converts the tweet jsons in 'harvest.json' to a pandas data frame, corresponding to certain fields of interest.</li>
  </ol>
  
# Future Plans
Part of the intent of this project is to log the journey of taking a rough idea and making some actual data analysis out of it. Accordingly, I want to convert the python scripts to a jupyter notebook with some exposition as to what pieces of the code were designed to do, why those decisions were made, and what shortcomings they have.

As far as specific scripts and modules are concerned:
  <ol>
    <li>README.me needs to be proofread. Is there a way to do this easily in git?</li>
    <li>twitter_scraper.py at the moment collects as much data from the specified time frame as twitter will allow, then ends. I would like to automate it to continue to scrape data for different days after the twitter refractory period ends. </li>
    <li>build_dataframe.py still needs to have the data cleaned. From a first go of collecting twitter data, it's clear that there are some challenges with working with tweets. One potentially serious problem is that there is a lot of spam on twitter, especially involving the Kardashians. Some sort of spam control should be implimented. </li>
    <li> The code so far only collects feature data, namely information contained in tweets. I still need to collect stock data. </li>
    <li> Eventually I want to apply some machine learning to these data to build some sentiment analysis scripts. </li>
  </ol>
