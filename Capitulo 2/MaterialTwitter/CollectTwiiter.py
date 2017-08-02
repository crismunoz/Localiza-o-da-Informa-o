# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:17:05 2016

@author: cristian.munoz
"""

import tweepy
from tweepy import OAuthHandler

def CollectTweets(consumer_key, consumer_secret, access_token, access_token_secret, lang, listwords, numtweets):
    
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    
    api = tweepy.API(auth)
    datatrain=[]
    for item in tweepy.Cursor(api.search, 
                              q=listwords,
                              rpp=100,
                              result_type="recent",
                              include_entities=True,
                              lang=lang).items(numtweets):
        datatrain.append(item.text)

    return datatrain