# -*- coding: utf-8 -*-

from os import getenv

#Configuración secrets para twitter
twitter = {
    'CONSUMER_KEY':'',
    'CONSUMER_SECRET':'',
    'ACCESS_KEY':'',
    'ACCESS_SECRET':''
}

ficheiros = {
    'DATAFILE':'data/vacas_habi.csv',
    'USEDFILE':'data/usado.csv'
}

programacion = {
    'hora':'22:00'
}

def carga():
    global CONSUMER_KEY
    try:
        CONSUMER_KEY = getenv("CONSUMER_KEY")
    except:
        pass

    global CONSUMER_SECRET
    try:
        CONSUMER_SECRET = getenv("CONSUMER_SECRET")
    except:
        pass

    global ACCESS_KEY
    try:
        ACCESS_KEY = getenv("ACCESS_KEY")
    except:
        pass

    global ACCESS_SECRET
    try:
        ACCESS_SECRET = getenv("ACCESS_SECRET")
    except:
        pass

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

    global hora
    try:
        hora = getenv("hora")
    except:
        pass

carga()

if CONSUMER_KEY is None:
    CONSUMER_KEY = twitter['CONSUMER_KEY']

if CONSUMER_SECRET is None:
    CONSUMER_SECRET = twitter['CONSUMER_SECRET']

if ACCESS_KEY is None:
    ACCESS_KEY = twitter['ACCESS_KEY']

if ACCESS_SECRET is None:
    ACCESS_SECRET = twitter['ACCESS_SECRET']

if DATAFILE is None:
    DATAFILE = ficheiros['DATAFILE']

if USEDFILE is None:
    USEDFILE = ficheiros['USEDFILE']

if hora is None:
    hora = programacion['hora']