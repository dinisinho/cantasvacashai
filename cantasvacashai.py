#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import random
import os
import sys
import tweepy

def obter_datos(ficheiro):
    datos = open(ficheiro, "r")
    numero_lineas = len(open(ficheiro, "r").readlines())
    ficheiro_csv = csv.reader(datos, delimiter=";")
    ficheiro_novo = open("/opt/bot/ficheiro_novo.csv", "w")
    contador = 0
    aleatorio = random.randrange(0, numero_lineas)
    for fila in ficheiro_csv:
        if contador == aleatorio:
            concello = fila[1]
            vacas = fila[2]
            habitantes = fila[3]
            usado = open("/opt/bot/usado.csv", "a")
            usado.write(fila[0] + ";" + fila[1] + ";" + fila[2] + ";" + fila[3] + "\n")
            usado.close()
        else:
            ficheiro_novo.write(fila[0] + ";" + fila[1] + ";" + fila[2] + ";" + fila[3] + "\n")
        contador += 1
    datos.close()
    ficheiro_novo.close()
    vacas_x_habitante = float(vacas) / float(habitantes)
    os.remove(ficheiro)
    os.rename("/opt/bot/ficheiro_novo.csv", ficheiro)

    if int(vacas) == int(habitantes):
        return "No Concello de " + concello + " hai un total de " + vacas + " vacas e " + habitantes + " habitantes. Tantas vacas como habitantes"
    elif int(vacas) == 0:
        return "No Concello de " + concello + " non hai ningunha vaca. Ten un total de " + habitantes + " habitantes."
    else:
        return "No Concello de " + concello + " hai un total de " + vacas + " vacas e " + habitantes + " habitantes. " + "{0:.2f}".format(vacas_x_habitante) + " vacas por habitante."

def publica(texto):
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    api.update_status(texto)

publica(obter_datos("/opt/bot/vacas_habi.csv"))
