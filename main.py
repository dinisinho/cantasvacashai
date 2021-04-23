#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
from time import sleep

from obterdatos import dato
from chiador import chia

schedule.every().day.at("10:55").do(print(dato()))

if __name__ == '__main__':
	while True:
		schedule.run_pending()
		sleep(1)