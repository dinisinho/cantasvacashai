# -*- coding: utf-8 -*-

from os import getenv

#Configuración secrets para twitter
twitter = {
    'T_CONSUMER_KEY':'',
    'T_CONSUMER_SECRET':'',
    'T_ACCESS_KEY':'',
    'T_ACCESS_SECRET':''
}

mastodon = {
    'M_ACCESS_TOKEN':'',
    'M_API_BASE_URL':'https://botsin.space'
}

ficheiros = {
    'DATAFILE':'data/vacas_habi.csv',
    'USEDFILE':'data/usado.csv'
}

programacion = {
    'hora':'22:00'
}

def carga():
    # TWITTER
    global TWITTER
    try:
        TWITTER = (getenv('TWITTER') == 'true')
    except:
        pass

    global T_CONSUMER_KEY
    try:
        T_CONSUMER_KEY = getenv("T_CONSUMER_KEY")
    except:
        pass

    global T_CONSUMER_SECRET
    try:
        T_CONSUMER_SECRET = getenv("T_CONSUMER_SECRET")
    except:
        pass

    global T_ACCESS_KEY
    try:
        T_ACCESS_KEY = getenv("T_ACCESS_KEY")
    except:
        pass

    global T_ACCESS_SECRET
    try:
        T_ACCESS_SECRET = getenv("T_ACCESS_SECRET")
    except:
        pass

    # MASTODON 
    global MASTODON
    try:
        MASTODON = (getenv('MASTODON') == 'true')
    except:
        pass

    global M_ACCESS_TOKEN
    try:
        M_ACCESS_TOKEN = getenv("M_ACCESS_TOKEN")
    except:
        pass

    global M_API_BASE_URL
    try:
        M_API_BASE_URL = getenv("M_API_BASE_URL")
    except:
        pass

    # FICHEIROS
    global DATAFILE
    try:
        DATAFILE = getenv("DATAFILE")
    except:
        pass

    global USEDFILE
    try:
        USEDFILE = getenv("USEDFILE")
    except:
        pass

    # PROGRAMACIÓN
    global hora
    try:
        hora = getenv("hora")
    except:
        pass

carga()

if T_CONSUMER_KEY is None:
    T_CONSUMER_KEY = twitter['T_CONSUMER_KEY']

if T_CONSUMER_SECRET is None:
    T_CONSUMER_SECRET = twitter['T_CONSUMER_SECRET']

if T_ACCESS_KEY is None:
    T_ACCESS_KEY = twitter['T_ACCESS_KEY']

if T_ACCESS_SECRET is None:
    T_ACCESS_SECRET = twitter['T_ACCESS_SECRET']

if M_ACCESS_TOKEN is None:
    M_ACCESS_TOKEN = mastodon['M_ACCESS_TOKEN']

if M_API_BASE_URL is None:
    M_API_BASE_URL = mastodon['M_API_BASE_URL']

if DATAFILE is None:
    DATAFILE = ficheiros['DATAFILE']

if USEDFILE is None:
    USEDFILE = ficheiros['USEDFILE']

if hora is None:
    hora = programacion['hora']
