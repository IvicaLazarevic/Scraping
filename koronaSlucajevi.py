#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'koronaSlucajevi.py'
__version__ = '0.1'
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

def srbija():
    SRBIJA = COVID_STATISTIKA['Countries']
    SRB = SRBIJA[148]['Country']
    print(f'\n[+] Statistika za drzavu {SRB} na datum {SRBIJA[148]["Date"]}')
    print(f'\n[+] Prijavljeni novi slucajevi: {SRBIJA[148]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno slucajeva: {SRBIJA[148]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {SRBIJA[148]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva: {SRBIJA[148]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {SRBIJA[148]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili: {SRBIJA[148]["TotalRecovered"]}')

def BiH():
    BiH = COVID_STATISTIKA['Countries']
    BIH = BiH[21]['Country']
    print(f'\n[+] Statistika za drzavu {BIH} na datum {BiH[21]["Date"]}')
    print(f'\n[+] Prijavljeni novi slucajevi: {BiH[21]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno slucajeva: {BiH[21]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {BiH[21]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva: {BiH[21]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {BiH[21]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili: {BiH[21]["TotalRecovered"]}')

def hrvatska():
    HRVATSKA = COVID_STATISTIKA['Countries']
    CRO = HRVATSKA[40]['Country']
    print(f'\n[+] Statistika za drzavu {CRO} na datum {HRVATSKA[40]["Date"]}')
    print(f'\n[+] Prijavljeni novi slucajevi: {HRVATSKA[40]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno slucajeva: {HRVATSKA[40]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {HRVATSKA[40]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva: {HRVATSKA[40]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {HRVATSKA[40]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili: {HRVATSKA[40]["TotalRecovered"]}')

def crnagora():
    CRNA_GORA = COVID_STATISTIKA['Countries']
    CG = CRNA_GORA[113]['Country']
    print(f'\n[+] Statistika za drzavu {CG} na datum {CRNA_GORA[113]["Date"]}')
    print(f'\n[+] Prijavljeni novi slucajevi: {CRNA_GORA[113]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno slucajeva: {CRNA_GORA[113]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {CRNA_GORA[113]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva: {CRNA_GORA[113]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {CRNA_GORA[113]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili: {CRNA_GORA[113]["TotalRecovered"]}')

def makedonija():
    MAKEDONIJA = COVID_STATISTIKA['Countries']
    MK = MAKEDONIJA[99]['Country']
    print(f'\n[+] Statistika za drzavu {MK} na datum {MAKEDONIJA[99]["Date"]}')
    print(f'\n[+] Prijavljeni novi slucajevi: {MAKEDONIJA[99]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno slucajeva: {MAKEDONIJA[99]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {MAKEDONIJA[99]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva: {MAKEDONIJA[99]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {MAKEDONIJA[99]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili: {MAKEDONIJA[99]["TotalRecovered"]}')

if __name__ == "__main__":
    globalno()
    srbija()
    BiH()
    hrvatska()
    crnagora()
    makedonija()

