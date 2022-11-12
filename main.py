#!/usr/bin/env python
# -*- coding: utf-8 -*-

import schedule
import time
import logging
from obterdatos import dato
from chiador import chia
from tooteador import tootea
from config import *

#Configuración de log:
log_level = logging.INFO

logging.basicConfig(
        level=log_level,
        datefmt='%d/%m/%Y %H:%M:%S',
        format='[%(asctime)s] <%(levelname)s> %(message)s'
    )

def main():
	publicacion = dato()
	if publicacion is not None:
		if TWITTER is True:
			try:
				chia(publicacion)
				logging.info(f"Chiouse en Twitter: {publicacion}")
			except Exception as e:
				logging.error(f"Produceuse un erro ao chiar. ERRO: {e}")

		if MASTODON is True:
			try:
				tootea(publicacion)
				logging.info(f"Tooteouse en Mastodon: {publicacion}")
			except Exception as e:
				logging.error(f"Produceuse un erro ao tootear. ERRO: {e}")

if __name__ == '__main__':
	logging.info("Programa iniciado")
	if TWITTER is True:
		logging.info("Twitter habilitado")
	if MASTODON is True:
		logging.info("Mastodon habilitado")
	logging.info(f"Os chíos publicaranse ás {hora}")
	schedule.every().day.at(hora).do(main)
	while True:
		schedule.run_pending()
		time.sleep(1)