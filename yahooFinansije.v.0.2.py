#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'yahooFinansije.py'
__version__ = '0.2'
__site__ = 'pythonbytes.rs'

import sys
from time import sleep as pauza
from subprocess import call

try:
    from selenium import webdriver
    from colorama import Fore
except:
    call('pip3 install colorama selenium', shell=True)
    exit()


def logo():
    print(Fore.RED+"\n       __           __        ____      __        ")
    print(Fore.RED+"  ____/ /___ ______/ /_______/ __ \____/ /__  _____ ")
    print(Fore.RED+" / __  / __ `/ ___/ //_/ ___/ / / / __  / _ \/ ___/ ")
    print(Fore.RED+"/ /_/ / /_/ / /  / ,< / /__/ /_/ / /_/ /  __/ /     ")
    print(Fore.RED+"\__,_/\__,_/_/  /_/|_|\___/\____/\__,_/\___/_/      ")
    print(Fore.RED+"                                                \n")
    print(Fore.RED+'                               Naziv: '+ __scriptName__)
    print(Fore.RED+'                               Verzija: '+ __version__)
    print(Fore.RED+'                               Koder: '+ __coder__)
    print(Fore.RED+ '                               Sajt: ' + __site__+Fore.WHITE)

if sys.platform == 'linux' or sys.platform == 'linux2' or sys.platform == 'darwin':
    call('clear', shell=True)
    logo()
else:
    call('cls', shell=True)
    logo()

CHROME_DRAJVER = 'C:\chromedriver.exe'
YAHOO_URL = 'https://finance.yahoo.com/quote/INFY/news?p=INFY'

def yahooFinansije():
    CHROME_OPCIJE = webdriver.ChromeOptions()
    CHROME_OPCIJE.add_argument('headless')
    CHROME_OPCIJE.add_experimental_option('excludeSwitches', ['enable-logging'])
    DRAJVER = webdriver.Chrome(executable_path=CHROME_DRAJVER, options=CHROME_OPCIJE)

    DRAJVER.get(YAHOO_URL)

    for i in range(5):
        DRAJVER.execute_script('window.scrollBy(0, 500)')
        pauza(1)

    VESTI = DRAJVER.find_elements_by_xpath('//*[@id="latestQuoteNewsStream-0-Stream"]/ul/li')

    for vest in VESTI:
        print(f'[+] Naslov vesti: {vest.find_element_by_xpath(".//h3/a").text}')


if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja prikazuje vesti sa Yahoo Finance.\n')
    yahooFinansije()

