#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from random import randrange
from config import *


def dato():
    lista = []
    with open(DATAFILE, "r", newline="\n") as ficheiro:
        reader = csv.reader(ficheiro, delimiter=",")
        lista = list(reader)
        try:
            datos_concello = lista[randrange(len(lista))]
            lista.remove(datos_concello)
        except ValueError:
            print("Non quedan concellos por publicar")
            return

    with open(DATAFILE, "w", newline="\n") as ficheiro:
        writer = csv.writer(ficheiro, delimiter=",")
        for linha in lista:
            writer.writerow(linha)

    with open(USEDFILE,"a", newline="\n") as ficheiro:
        writer = csv.writer(ficheiro,delimiter=",")
        writer.writerow(datos_concello)

    concello = datos_concello[1]
    vacas = datos_concello[2]
    habitantes = datos_concello[3]
    vacas_x_habitante = (str(round(float(vacas) / float(habitantes),4))).replace(".",",")

    if int(vacas) == int(habitantes):
        return f"No Concello de {concello} hai un total de {vacas} vacas e {habitantes} habitantes. Tantas vacas como habitantes"
    elif int(vacas) == 0:
        return f"No Concello de {concello} non hai ningunha vaca. Ten un total de {habitantes} habitantes."
    else:
        print(f"No Concello de {concello} hai un total de {vacas} vacas e {habitantes} habitantes. {vacas_x_habitante} vacas por habitante.")
        return f"No Concello de {concello} hai un total de {vacas} vacas e {habitantes} habitantes. {vacas_x_habitante} vacas por habitante."


if __name__ == '__main__':
    print(dato())