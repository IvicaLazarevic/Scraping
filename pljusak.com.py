#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'pljusak.com.py'
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

def pljusak():
    URL = 'https://pljusak.com/meteo.php?stanica=karaburma'
    RES = requests.get(URL)
    SOUP = BeautifulSoup(RES.content, 'html.parser')
    print(f'[+] Vrednosti za grad: {SOUP.find_all("td", {"class":"naslov_met"})[0].text}')
    print(f'[+] Temperatura: {SOUP.find_all("td", {"class":"broj_met"})[0].text}')
    print(f'[+] Vetar(m/s): {SOUP.find_all("td", {"class": "broj_met"})[1].text}')
    print(f'[+] Pritisak(hPa): {SOUP.find_all("td", {"class": "broj_met"})[2].text}')
    print(f'[+] Vlaznost(%): {SOUP.find_all("td", {"class": "broj_met"})[3].text}')
    print(f'[+] Padavine(mm): {SOUP.find_all("td", {"class": "broj_met"})[4].text}')


if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja radi scrap sajta pljusak.com\n')
    pljusak()