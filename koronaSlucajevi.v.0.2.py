#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'koronaSlucajevi.py'
__version__ = '0.2'
__site__ = 'pythonbytes.rs'

import sys
from subprocess import call

try:
    import requests
    from colorama import Fore
except:
    call('pip3 install colorama requests', shell=True)
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

COVID_STATISTIKA = requests.get('https://api.covid19api.com/summary').json()

def globalno():
    print('\n[+] Statiskika na globalnom nivou:')
    print(f'\n[+] Prijavljeni novi slucajevi na globalnom nivou: {COVID_STATISTIKA["Global"]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno na globalnom nivou: {COVID_STATISTIKA["Global"]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {COVID_STATISTIKA["Global"]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva na globalnom nivou: {COVID_STATISTIKA["Global"]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {COVID_STATISTIKA["Global"]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili na globalnom nivou: {COVID_STATISTIKA["Global"]["TotalRecovered"]}')

def drzava(broj):
    DRZAVA = COVID_STATISTIKA['Countries']
    drz = DRZAVA[broj]['Country']
    print(f'\n[+] Statistika za drzavu {drz} na datum {DRZAVA[broj]["Date"]}')
    print(f'\n[+] Prijavljeni novi slucajevi: {DRZAVA[broj]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno slucajeva: {DRZAVA[broj]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {DRZAVA[broj]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva: {DRZAVA[broj]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {DRZAVA[broj]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili: {DRZAVA[broj]["TotalRecovered"]}')

if __name__ == "__main__":
    izbor = int(input('''\n[+] Izaberite opciju koju zelite:
    
    [0] - Statistika na globalnom nivou.
    [1] - Statistika za Srbiju.
    [2] - Statistika za Bosnu i Hercegovinu.
    [3] - Statistika za Hrvatsku.
    [4] - Statistika za Crnu Goru.
    [5] - Statistika za Severnu Makedoniju.
    [6] - Statistika za Albaniju.
    
    Unesite opciju koju zelite: '''))

    if izbor not in [0, 1, 2, 3, 4, 5, 6]:
        exit('\n[-] Molimo vas unesite pravilno opciju koju zelite!')

    if izbor == 0:
        globalno()

    if izbor == 1:
        drzava(148)

    if izbor == 2:
        drzava(21)

    if izbor == 3:
        drzava(40)

    if izbor == 4:
        drzava(113)

    if izbor == 5:
        drzava(99)

    if izbor == 6:
        drzava(1)