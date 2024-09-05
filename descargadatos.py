#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import logging
import requests
from config import *

ano_habitantes = "2023"
ano_vacas = "2023"
baseURLHabitantes = f"https://www.ige.gal/igebdt/igeapi/json/datos/589/0:0,1:${ano_habitantes},9913"
baseURLVacas = f"https://www.ige.gal/igebdt/igeapi/json/datos/62/0:6,1:${ano_vacas},9915"

def descargaDatos():
    codsconcellos = ""
    lista_total = []
    with open(CONCELLOSFILE, "r", newline="\n") as ficheiro:
        reader = csv.reader(ficheiro, delimiter=";")
        lista = list(reader)
    for concello in lista:
        nome_concello = concello[1]
        cod_concello = concello[0]
        urlPoboacion = f"{baseURLHabitantes}:{cod_concello}"
        urlVacas = f"{baseURLVacas}:{cod_concello}"
        resposta_poboacion = requests.get(urlPoboacion)
        datos_habitantes = resposta_poboacion.json()['datos']
        for habitantes in datos_habitantes:
            resposta_vacas = requests.get(urlVacas)
            datos_vacas = resposta_vacas.json()['datos']
            for vacas in datos_vacas:
                lista = [cod_concello, nome_concello, vacas[5], habitantes[5]]
                print(lista)
                lista_total.append(lista)
    return lista_total

def gardaDatos(lista):
    with open(DATAFILE, "w", newline="\n") as ficheiro:
        writer = csv.writer(ficheiro, delimiter=";")
        for linha in lista:
            writer.writerow(linha)

if __name__ == '__main__':
    gardaDatos(descargaDatos())