#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'vremenskaPrognoza.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
import json
from urllib import request
from subprocess import call

try:
    from colorama import Fore
except:
    call('pip3 install colorama', shell=True)
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

MESTO = input('\n[+] Unesite naziv mesta: ')

API_KLJUC = '72e3282487104dde2ab3a919942ac41f'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={MESTO}&lang=sr&units=metric&appid={API_KLJUC}'

ODGOVOR = request.urlopen(URL)
PODACI = json.load(ODGOVOR)

print(f'\n[+] Vremenska prognoza za mesto: {PODACI["name"]}')
print(f'[+] Drzava: {PODACI["sys"]["country"]}')

print(f'\n[+] Trenutno vreme: {PODACI["weather"][0]["description"]}')
print(f'[+] Temperatura: {PODACI["main"]["temp"]}°C')
print(f'[+] Subjektivni osecaj: {PODACI["main"]["feels_like"]}°C')
print(f'[+] Minimalna temperatura: {PODACI["main"]["temp_min"]}°C')
print(f'[+] Maksimalna temperatura: {PODACI["main"]["temp_max"]}°C')
print(f'[+] Atmosferski pritisak: {PODACI["main"]["pressure"]}hPa(mb)')
print(f'[+] Vlaznost vazduha: {PODACI["main"]["humidity"]}%')
print(f'[+] Vidljivost: {PODACI["visibility"]}')
print(f'[+] Brzina vetra: {PODACI["wind"]["speed"]}m/s')
print(f'[+] Oblacnost: {PODACI["clouds"]["all"]}%')

