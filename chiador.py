#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from config import *

def chia(chio):
    auth = tweepy.OAuthHandler(T_CONSUMER_KEY, T_CONSUMER_SECRET)
    auth.set_access_token(T_ACCESS_KEY, T_ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(chio)