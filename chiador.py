#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from config import *

def chia(chio):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(chio)