# -*- coding: utf-8 -*-

import schedule
import time
import logging
from obterdatos import dato
from chiador import chia
from config import *

#Configuración de log:
log_level = logging.INFO

logging.basicConfig(
        level=log_level,
        datefmt='%d/%m/%Y %H:%M:%S',
        format='[%(asctime)s] <%(levelname)s> %(message)s'
    )

def main():
	tweet = dato()
	if tweet is not None:
		try:
			chia(tweet)
			logging.info(f"Chiouse: {tweet}")
		except Exception as e:
			logging.error(f"Produceuse un erro ao chiar. ERRO: {e}")

if __name__ == '__main__':
	logging.info("Programa iniciado")
	schedule.every().day.at(hora).do(main)
	while True:
		schedule.run_pending()
		time.sleep(1)