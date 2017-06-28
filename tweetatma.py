#! /usr/bin/python
import tweepy
consumer_key = "ymahn4aQTwk4eyYEoImVS9kkj"
consumer_secret = "uKW0MBP9eNsQqVg6T1FHeNUtLvg1X46IJoqsRKGjRopwnxRCu2"
access_token = "771826759775891457-NiW7c41OSj6BlucOkzcgIQIxNO1fpbj" 
access_token_secret = "PdDxM1s6NEBye9cA6N7kTNq1HJHtQnDZ7bIUBNPonido7"

giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)
api = tweepy.API(giris)
api.update_status(status = "DENEME")
