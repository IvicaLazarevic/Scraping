#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'listaUFCturnira.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
from subprocess import call

try:
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from colorama import Fore
except:
    call('pip3 install colorama selenium bs4', shell=True)
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
UFC_WIKI = 'https://en.wikipedia.org/wiki/List_of_UFC_events'

def UFC():
    CHROME_OPCIJE = webdriver.ChromeOptions()
    CHROME_OPCIJE.add_argument('--headless')
    CHROME_OPCIJE.add_experimental_option('excludeSwitches', ['enable-logging'])
    DRAJVER = webdriver.Chrome(executable_path=CHROME_DRAJVER, options=CHROME_OPCIJE)

    try:
        DRAJVER.get(UFC_WIKI)
        soup = BeautifulSoup(DRAJVER.page_source, 'html.parser')
        UFC_TURNIRI = soup.find_all('a', class_='mw-parser-output')

        for ufc in UFC_TURNIRI:
            print(ufc)

    except(KeyboardInterrupt):
        exit('[-] Skripta prekinuta sa radom!')



if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja izlistava nazive svih UFC turnira!')
    UFC()

