#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'rottenTomatoes100.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
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

def rotten100():
    ROTTEN_100_URL = 'https://www.rottentomatoes.com/top/bestofrt/'
    RES = requests.get(ROTTEN_100_URL)
    SOUP = BeautifulSoup(RES.content, 'html.parser')
    for table in SOUP.find_all('table', {'class':'table'}):
        for row in table.find_all('tr')[1:]:
            print(f'[+] Redni broj filma: {row.find("td", {"class":"bold"}).text}')
            print(f'[+] Ime filma: {row.find("a", {"class":"unstyled articleLink"}).text.strip()}')
            print(f'[+] Broj kritika: {row.find("td", {"class":"right hidden-xs"}).text}')
            print(f'[+] Ocena: {row.find("span", {"class":"tMeterScore"}).text}\n')

if __name__ == '__main__':
    print('\n[+] Top 100 filmova svih vremena prema rottentomatoes.com.\n')
    rotten100()