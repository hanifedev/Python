#! /usr/bin/python
import tweepy
consumer_key = ""
consumer_secret = ""
access_token = "" 
access_token_secret = ""

giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)
api = tweepy.API(giris)
api.update_status(status = "DENEME")
