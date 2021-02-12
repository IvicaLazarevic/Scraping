#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'sasomange.rs.py'
__version__ = '0.2'
__site__ = 'pythonbytes.rs'

import sys
import csv
from subprocess import call

try:
    import requests
    from bs4 import BeautifulSoup
    from colorama import Fore
except:
    call('pip3 install colorama requests bs4', shell=True)
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

def sasomangeScrap():
    URL = 'https://sasomange.rs/'
    RES = requests.get(URL)
    SOUP = BeautifulSoup(RES.content, 'html.parser')

    for kategorije in SOUP.find_all('ul', {'class':'web-categories'}):
        for kategorija in kategorije.find_all('li'):
            print(f'[+] Naziv kategorije: {kategorija.find("p", {"class":"category-name"}).text}')


if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja iscitava oglase sa sajta sasomange.rs\n')
    sasomangeScrap()