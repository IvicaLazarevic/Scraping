#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'portlandCraigslist.py'
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

def portlandCraig(PRETRAGA):
    CRAIG_URL = f'https://portland.craigslist.org/search/sss?query={PRETRAGA}&sort=date'
    RES = requests.get(CRAIG_URL)
    SOUP = BeautifulSoup(RES.content, 'html.parser')
    for div in SOUP.find_all('div', {'class':'result-info'}):
        try:
            print(f'\n[+] Naziv oglasa: {div.find("a", {"class":"result-title hdrlnk"}).text}')
            print(f'[+] Cena: {div.find("span", {"class":"result-price"}).text}')
            print(f'[+] Naziv mesta: {div.find("span", {"class":"result-hood"}).text}')
            print(f'[+] Datum: {div.find("time", {"class":"result-date"}).text}')
            CSV_UPIS.writerow([div.find("a", {"class":"result-title hdrlnk"}).text, div.find("span", {"class":"result-price"}).text, div.find("span", {"class":"result-hood"}).text, div.find("time", {"class":"result-date"}).text])

        except:
            pass
    print('\n[+] Rezultate potrazite u fajlu pod nazivom Izvestaj.csv')

if __name__ == '__main__':
    print('\n[+] Skripta pretrazuje portland.craigslist.org.\n')
    PRETRAGA = input('[+] Sta zelite da pretrazite(na engleskom): ')
    FAJL = open('Izvestaj.csv', 'w', newline='', encoding='utf-8')
    CSV_UPIS = csv.writer(FAJL)
    CSV_UPIS.writerow(['Naziv oglasa', 'Cena', 'Naziv mesta', 'Datum'])
    portlandCraig(PRETRAGA)