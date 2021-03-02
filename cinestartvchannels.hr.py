#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'cinestartvchannels.hr.py'
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

def cineTv():
    URL = 'https://cinestartvchannels.hr/film-serija/'
    RES = requests.get(URL)
    SOUP = BeautifulSoup(RES.content, 'html.parser')
    for item in SOUP.findAll('div', {'class':'wrapper container-fluid'}):
        for film in item.findAll('div', {'class':'body col-xs-12 col-lg-10'}):

            # AKCIJA

            for akcija in film.findAll('a', {'class':'single-movie-serie akc'}):
                AKCIJA.append(akcija.text)

            for akcanimirani in film.findAll('a', {'class':'single-movie-serie akc ani'}):
                AKCIJA.append(akcanimirani.text)
                ANIMIRANI.append(akcanimirani.text)

            for akchoror in film.findAll('a', {'class':'single-movie-serie akc hor'}):
                AKCIJA.append(akchoror.text)
                HOROR.append(akchoror.text)

            for akcijakrimi in film.findAll('a', {'class':'single-movie-serie akc kri'}):
                AKCIJA.append(akcijakrimi.text)
                KRIMINALISTICKI.append(akcijakrimi.text)

            for akckrimmisterija in film.findAll('a', {'class':'single-movie-serie akc kri misterij'}):
                AKCIJA.append(akckrimmisterija.text)
                KRIMINALISTICKI.append(akckrimmisterija.text)
                MISTERIJA.append(akckrimmisterija.text)

            for akckrimiscifi in film.findAll('a', {'class':'single-movie-serie akc kri sf'}):
                AKCIJA.append(akckrimiscifi.text)
                KRIMINALISTICKI.append(akckrimiscifi.text)
                SCIFI.append(akckrimiscifi.text)

            for akckrimitriler in film.findAll('a', {'class':'single-movie-serie akc kri tri'}):
                AKCIJA.append(akckrimitriler.text)
                KRIMINALISTICKI.append(akckrimitriler.text)
                TRILER.append(akckrimitriler.text)

            for akckomedija in film.findAll('a', {'class':'single-movie-serie akc kom'}):
                AKCIJA.append(akckomedija.text)
                KOMEDIJA.append(akckomedija.text)

            for akckomporodicni in film.findAll('a', {'class':'single-movie-serie akc kom obi'}):
                AKCIJA.append(akckomporodicni.text)
                KOMEDIJA.append(akckomporodicni.text)
                PORODICNI.append(akckomporodicni.text)

            for akcavantura in film.findAll('a', {'class':'single-movie-serie akc ava'}):
                AKCIJA.append(akcavantura.text)
                AVANTURA.append(akcavantura.text)

            for akcavantdrama in film.findAll('a', {'class':'single-movie-serie akc ava dra'}):
                AKCIJA.append(akcavantdrama.text)
                AVANTURA.append(akcavantdrama.text)
                DRAMA.append(akcavantdrama.text)

            for akcavanthoror in film.findAll('a', {'class':'single-movie-serie akc ava hor'}):
                AKCIJA.append(akcavanthoror.text)
                AVANTURA.append(akcavanthoror.text)
                HOROR.append(akcavanthoror.text)

            for akcijaavanturakrimi in film.findAll('a', {'class':'single-movie-serie akc ava tri'}):
                AKCIJA.append(akcijaavanturakrimi.text)
                KRIMINALISTICKI.append(akcijaavanturakrimi.text)
                AVANTURA.append(akcijaavanturakrimi.text)

            for akcavanturascifi in film.findAll('a', {'class':'single-movie-serie akc ava sf'}):
                AKCIJA.append(akcavanturascifi.text)
                AVANTURA.append(akcavanturascifi.text)
                SCIFI.append(akcavanturascifi.text)

            for akcdramkrimi in film.findAll('a', {'class':'single-movie-serie akc dra kri'}):
                AKCIJA.append(akcdramkrimi.text)
                DRAMA.append(akcdramkrimi.text)
                KRIMINALISTICKI.append(akcdramkrimi.text)

            for akcdramscifi in film.findAll('a', {'class':'single-movie-serie akc dra sf'}):
                AKCIJA.append(akcdramscifi.text)
                DRAMA.append(akcdramscifi.text)
                SCIFI.append(akcdramscifi.text)

            for akcscifitriler in film.findAll('a', {'class':'single-movie-serie akc sf tri'}):
                AKCIJA.append(akcscifitriler.text)
                SCIFI.append(akcscifitriler.text)
                TRILER.append(akcscifitriler.text)

            for akcavantura in film.findAll('a', {'class':'single-movie-serie akc ava'}):
                AKCIJA.append(akcavantura.text)
                AVANTURA.append(akcavantura.text)

            for akcbiografija in film.findAll('a', {'class':'single-movie-serie akc bio'}):
                AKCIJA.append(akcbiografija.text)
                BIOGRAFIJA.append(akcbiografija.text)

            for akcdrama in film.findAll('a', {'class':'single-movie-serie akc dra'}):
                AKCIJA.append(akcdrama.text)
                DRAMA.append(akcdrama.text)

            for akctriler in film.findAll('a', {'class':'single-movie-serie akc tri'}):
                AKCIJA.append(akctriler.text)
                TRILER.append(akctriler.text)

            for akcvestern in film.findAll('a', {'class':'single-movie-serie akc ves'}):
                AKCIJA.append(akcvestern.text)
                VESTERN.append(akcvestern.text)

            for akcscifi in film.findAll('a', {'class':'single-movie-serie akc sf'}):
                AKCIJA.append(akcscifi.text)
                SCIFI.append(akcscifi.text)

            # ANIMIRANI

            for animirani in film.findAll('a', {'class':'single-movie-serie ani'}):
                ANIMIRANI.append(animirani.text)

            for aniavantura in film.findAll('a', {'class':'single-movie-serie ani ava'}):
                ANIMIRANI.append(aniavantura.text)
                AVANTURA.append(aniavantura.text)

            for aniavantkomedija in film.findAll('a', {'class':'single-movie-serie ani ava kom'}):
                ANIMIRANI.append(aniavantkomedija.text)
                AVANTURA.append(aniavantkomedija.text)
                KOMEDIJA.append(aniavantkomedija.text)

            for aniavantkomporodicni in film.findAll('a', {'class':'single-movie-serie ani ava kom obi'}):
                ANIMIRANI.append(aniavantkomporodicni.text)
                AVANTURA.append(aniavantkomporodicni.text)
                KOMEDIJA.append(aniavantkomporodicni.text)
                PORODICNI.append(aniavantkomporodicni.text)

            for aniavantporodicni in film.findAll('a', {'class':'single-movie-serie ani ava obi'}):
                ANIMIRANI.append(aniavantporodicni.text)
                AVANTURA.append(aniavantporodicni.text)
                PORODICNI.append(aniavantporodicni.text)

            for anikomporodicni in film.findAll('a', {'class':'single-movie-serie ani kom obi'}):
                ANIMIRANI.append(anikomporodicni.text)
                KOMEDIJA.append(anikomporodicni.text)
                PORODICNI.append(anikomporodicni.text)

            for aniporodicni in film.findAll('a', {'class':'single-movie-serie ani obi'}):
                ANIMIRANI.append(aniporodicni.text)
                PORODICNI.append(aniporodicni.text)

            for aniscifi in film.findAll('a', {'class':'single-movie-serie ani sf'}):
                ANIMIRANI.append(aniscifi.text)
                SCIFI.append(aniscifi.text)

            for anihidden in film.findAll('a', {'class':'single-movie-serie ani hidden'}):
                ANIMIRANI.append(anihidden.text)

            # AVANTURA

            for avantura in film.findAll('a', {'class':'single-movie-serie ava'}):
                AVANTURA.append(avantura.text)

            for avantbiodramakrimi in film.findAll('a', {'class':'single-movie-serie ava bio dra kri'}):
                AVANTURA.append(avantbiodramakrimi.text)
                BIOGRAFIJA.append(avantbiodramakrimi.text)
                DRAMA.append(avantbiodramakrimi.text)
                KRIMINALISTICKI.append(avantbiodramakrimi.text)

            for avantdrama in film.findAll('a', {'class':'single-movie-serie ava dra'}):
                AVANTURA.append(avantdrama.text)
                DRAMA.append(avantdrama.text)

            for avanturadramakom in film.findAll('a', {'class':'single-movie-serie ava dra kom'}):
                AVANTURA.append(avanturadramakom.text)
                DRAMA.append(avanturadramakom.text)
                KOMEDIJA.append(avanturadramakom.text)

            for avantkomedija in film.findAll('a', {'class':'single-movie-serie ava kom'}):
                AVANTURA.append(avantkomedija.text)
                KOMEDIJA.append(avantkomedija.text)

            for avantscifi in film.findAll('a', {'class':'single-movie-serie ava sf'}):
                AVANTURA.append(avantscifi.text)
                SCIFI.append(avantscifi.text)

            for avantkomporodicni in film.findAll('a', {'class':'single-movie-serie ava kom obi'}):
                AVANTURA.append(avantkomporodicni.text)
                KOMEDIJA.append(avantkomporodicni.text)
                PORODICNI.append(avantkomporodicni.text)

            for avanthorormisterija in film.findAll('a', {'class':'single-movie-serie ava hor misterij'}):
                AVANTURA.append(avanthorormisterija.text)
                HOROR.append(avanthorormisterija.text)
                MISTERIJA.append(avanthorormisterija.text)

            for avantmisterporodicni in film.findAll('a', {'class':'single-movie-serie ava misterij obi'}):
                AVANTURA.append(avantmisterporodicni.text)
                MISTERIJA.append(avantmisterporodicni.text)
                PORODICNI.append(avantmisterporodicni.text)

            for avantkomporodscifi in film.findAll('a', {'class':'single-movie-serie ava kom obi sf'}):
                AVANTURA.append(avantkomporodscifi.text)
                KOMEDIJA.append(avantkomporodscifi.text)
                PORODICNI.append(avantkomporodscifi.text)
                SCIFI.append(avantkomporodscifi.text)

            for avantdramaporodicni in film.findAll('a', {'class':'single-movie-serie ava dra obi'}):
                AVANTURA.append(avantdramaporodicni.text)
                DRAMA.append(avantdramaporodicni.text)
                PORODICNI.append(avantdramaporodicni.text)

            for avantporodicni in film.findAll('a', {'class':'single-movie-serie ava obi'}):
                AVANTURA.append(avantporodicni.text)
                PORODICNI.append(avantporodicni.text)

            for avantporodscifi in film.findAll('a', {'class':'single-movie-serie ava obi sf'}):
                AVANTURA.append(avantporodscifi.text)
                PORODICNI.append(avantporodscifi.text)
                SCIFI.append(avantporodscifi.text)

            # BIOGRAFSKI

            for biografija in film.findAll('a', {'class':'single-movie-serie bio'}):
                BIOGRAFIJA.append(biografija.text)

            for biodrama in film.findAll('a', {'class':'single-movie-serie bio dra'}):
                BIOGRAFIJA.append(biodrama.text)
                DRAMA.append((biodrama.text))

            for biodokument in film.findAll('a', {'class':'single-movie-serie bio dok'}):
                BIOGRAFIJA.append(biodokument.text)
                DOKUMENTARAC.append(biodokument.text)

            for biodramkrimi in film.findAll('a', {'class':'single-movie-serie bio dra kri'}):
                BIOGRAFIJA.append(biodramkrimi.text)
                DRAMA.append(biodramkrimi.text)
                KRIMINALISTICKI.append(biodramkrimi.text)

            for biodramkrimitriler in film.findAll('a', {'class':'single-movie-serie bio dra kri tri'}):
                BIOGRAFIJA.append(biodramkrimitriler.text)
                DRAMA.append(biodramkrimitriler.text)
                KRIMINALISTICKI.append(biodramkrimitriler.text)
                TRILER.append(biodramkrimitriler.text)

            for biodramaromantika in film.findAll('a', {'class':'single-movie-serie bio dra rom'}):
                BIOGRAFIJA.append(biodramaromantika.text)
                DRAMA.append(biodramaromantika.text)
                ROMANSA.append(biodramaromantika.text)

            for biodramatriler in film.findAll('a', {'class':'single-movie-serie bio dra tri'}):
                BIOGRAFIJA.append(biodramatriler.text)
                DRAMA.append(biodramatriler.text)
                TRILER.append(biodramatriler.text)

            for biodramasportski in film.findAll('a', {'class':'single-movie-serie bio dra spo'}):
                BIOGRAFIJA.append(biodramasportski.text)
                DRAMA.append(biodramasportski.text)

            for biokomedija in film.findAll('a', {'class':'single-movie-serie bio kom'}):
                BIOGRAFIJA.append(biokomedija.text)
                KOMEDIJA.append(biokomedija.text)

            for biokomkrimi in film.findAll('a', {'class':'single-movie-serie bio kom kri'}):
                BIOGRAFIJA.append(biokomkrimi.text)
                KOMEDIJA.append(biokomkrimi.text)
                KRIMINALISTICKI.append(biokomkrimi.text)

            for biokrimi in film.findAll('a', {'class':'single-movie-seria bio kri'}):
                BIOGRAFIJA.append(biokrimi.text)
                KRIMINALISTICKI.append(biokrimi.text)

            # DRAMA

            for drama in film.findAll('a', {'class':'single-movie-serie dra'}):
                DRAMA.append(drama.text)

            for dramahorscifi in film.findAll('a', {'class':'single-movie-serie dra hor sf'}):
                DRAMA.append(dramahorscifi.text)
                HOROR.append(dramahorscifi.text)
                SCIFI.append(dramahorscifi.text)

            for dramahormisterija in film.findAll('a', {'class':'single-movie-serie dra hor misterij'}):
                DRAMA.append(dramahormisterija.text)
                HOROR.append(dramahormisterija.text)
                MISTERIJA.append(dramahormisterija.text)

            for dramahorscifitriler in film.findAll('a', {'class':'single-movie-serie dra hor sf tri'}):
                DRAMA.append(dramahorscifitriler.text)
                HOROR.append(dramahorscifitriler.text)
                SCIFI.append(dramahorscifitriler.text)
                TRILER.append(dramahorscifitriler.text)

            for dramahortriler in film.findAll('a', {'class':'single-movie-serie dra hor tri'}):
                DRAMA.append(dramahortriler.text)
                HOROR.append(dramahortriler.text)
                TRILER.append(dramahortriler.text)

            for dramakri in film.findAll('a', {'class':'single-movie-serie dra kri'}):
                DRAMA.append(dramakri.text)
                KRIMINALISTICKI.append(dramakri.text)

            for drakritriler in film.findAll('a', {'class':'single-movie-serie dra kri tri'}):
                DRAMA.append(drakritriler.text)
                KRIMINALISTICKI.append(drakritriler.text)
                TRILER.append(drakritriler.text)

            for dramakomedija in film.findAll('a', {'class':'single-movie-serie dra kom'}):
                DRAMA.append(dramakomedija.text)
                KOMEDIJA.append(dramakomedija.text)

            for dramakomporodicni in film.findAll('a', {'class':'single-movie-serie dra kom obi'}):
                DRAMA.append(dramakomporodicni.text)
                KOMEDIJA.append(dramakomporodicni.text)
                PORODICNI.append(dramakomporodicni.text)

            for dramakomromanticni in film.findAll('a', {'class':'single-movie-serie dra kom rom'}):
                DRAMA.append(dramakomromanticni.text)
                KOMEDIJA.append(dramakomromanticni.text)
                ROMANSA.append(dramakomromanticni.text)

            for dramakomscifi in film.findAll('a', {'class':'single-movie-serie dra kom sf'}):
                DRAMA.append(dramakomscifi.text)
                KOMEDIJA.append(dramakomscifi.text)
                SCIFI.append(dramakomscifi.text)

            for dramakomtriler in film.findAll('a', {'class':'single-movie-serie dra kom tri'}):
                DRAMA.append(dramakomtriler.text)
                KOMEDIJA.append(dramakomtriler.text)
                TRILER.append(dramakomtriler.text)

            for dramamisterporodicni in film.findAll('a', {'class':'single-movie-serie dra misterij obi'}):
                DRAMA.append(dramamisterporodicni.text)
                MISTERIJA.append(dramamisterporodicni.text)
                PORODICNI.append(dramamisterporodicni.text)

            for dramamisterscifi in film.findAll('a', {'class':'single-movie-serie dra misterij sf'}):
                DRAMA.append(dramamisterscifi.text)
                MISTERIJA.append(dramamisterscifi.text)
                SCIFI.append(dramamisterscifi.text)

            for dramamistertriler in film.findAll('a', {'class':'single-movie-serie dra misterij tri'}):
                DRAMA.append(dramamistertriler.text)
                MISTERIJA.append(dramamistertriler.text)
                TRILER.append(dramamistertriler.text)

            for dramromantika in film.findAll('a', {'class':'single-movie-serie dra rom'}):
                DRAMA.append(dramromantika.text)
                ROMANSA.append(dramromantika.text)

            for dramascifi in film.findAll('a', {'class':'single-movie-serie dra sf'}):
                DRAMA.append(dramascifi.text)
                SCIFI.append((dramascifi.text))

            for dramascifitriler in film.findAll('a', {'class':'single-movie-serie dra sf tri'}):
                DRAMA.append(dramascifitriler.text)
                SCIFI.append(dramascifitriler.text)
                TRILER.append(dramascifitriler.text)

            for dramatriler in film.findAll('a', {'class':'single-movie-serie dra tri'}):
                DRAMA.append(dramatriler.text)
                TRILER.append(dramatriler.text)

            # DOKUMENTARNI

            for dokumentarac in film.findAll('a', {'class':'single-movie-serie dok'}):
                DOKUMENTARAC.append(dokumentarac.text)

            # HOROR

            for horor in film.findAll('a', {'class':'single-movie-serie hor'}):
                HOROR.append(horor.text)

            for horkriromansa in film.findAll('a', {'class':'single-movie-serie hor kri rom'}):
                HOROR.append(horkriromansa.text)
                KRIMINALISTICKI.append(horkriromansa.text)
                ROMANSA.append(horkriromansa.text)

            for horkomedija in film.findAll('a', {'class':'single-movie-serie hor kom'}):
                HOROR.append(horkomedija.text)
                KOMEDIJA.append(horkomedija.text)

            for horkomscifi in film.findAll('a', {'class':'single-movie-serie hor kom sf'}):
                HOROR.append(horkomscifi.text)
                KOMEDIJA.append(horkomscifi.text)
                SCIFI.append(horkomscifi)

            for horormisterija in film.findAll('a', {'class':'single-movie-serie hor misterij'}):
                HOROR.append(horormisterija.text)
                MISTERIJA.append(horormisterija.text)

            for horortriler in film.findAll('a', {'class':'single-movie-serie hor tri'}):
                HOROR.append(horortriler.text)
                TRILER.append((horortriler.text))

            for hormisterijascifi in film.findAll('a', {'class':'single-movie-serie hor misterij sf'}):
                HOROR.append(hormisterijascifi.text)
                MISTERIJA.append(hormisterijascifi.text)
                SCIFI.append(hormisterijascifi.text)

            for hororscifi in film.findAll('a', {'class':'single-movie-serie hor sf'}):
                HOROR.append(hororscifi.text)
                SCIFI.append(hororscifi.text)

            # KRIMINALISTICKI

            for kriminalisticki in film.findAll('a', {'class':'single-movie-serie kri'}):
                KRIMINALISTICKI.append(kriminalisticki.text)

            for krimitriler in film.findAll('a', {'class':'single-movie-serie kri tri'}):
                KRIMINALISTICKI.append(krimitriler.text)
                TRILER.append(krimitriler.text)

            # KOMEDIJE

            for komedija in film.findAll('a', {'class':'single-movie-serie kom'}):
                KOMEDIJA.append(komedija.text)

            for komromansa in film.findAll('a', {'class':'single-movie-serie kom rom'}):
                KOMEDIJA.append(komromansa.text)
                ROMANSA.append(komromansa.text)

            for kommisterija in film.findAll('a', {'class':'single-movie-serie kom misterij'}):
                KOMEDIJA.append(kommisterija.text)
                MISTERIJA.append(kommisterija.text)

            for komkriporodicni in film.findAll('a', {'class':'single-movie-serie kom kri obi'}):
                KOMEDIJA.append(komkriporodicni.text)
                KRIMINALISTICKI.append(komkriporodicni.text)
                PORODICNI.append(komkriporodicni.text)

            for komporodicni in film.findAll('a', {'class':'single-movie-serie kom obi'}):
                KOMEDIJA.append(komporodicni.text)
                PORODICNI.append(komporodicni.text)

            for komscifi in film.findAll('a', {'class':'single-movie-serie kom sf'}):
                KOMEDIJA.append(komscifi.text)
                SCIFI.append(komscifi.text)

            for komtriler in film.findAll('a', {'class':'single-movie-serie kom tri'}):
                KOMEDIJA.append(komtriler.text)
                TRILER.append(komtriler.text)

            # PORODICNI

            for porodicni in film.findAll('a', {'class':'single-movie-serie obi'}):
                PORODICNI.append(porodicni.text)

            # SCI-FI

            for scifi in film.findAll('a', {'class':'single-movie-serie sf'}):
                SCIFI.append(scifi.text)

            for scifitriler in film.findAll('a', {'class':'single-movie-serie sf tri'}):
                SCIFI.append(scifitriler.text)
                TRILER.append(scifitriler.text)

            # TRILER

            for triler in film.findAll('a', {'class':'single-movie-serie tri'}):
                TRILER.append(triler.text)


if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja radi scraping sajta cinestartvchannels.hr\n')

    KOMEDIJA = []
    KRIMINALISTICKI = []
    HOROR = []
    TRILER = []
    DRAMA = []
    BIOGRAFIJA = []
    AKCIJA = []
    AVANTURA = []
    SCIFI = []
    ANIMIRANI = []
    ROMANSA = []
    VESTERN = []
    DOKUMENTARAC = []
    PORODICNI = []
    MISTERIJA = []

    print('[!] Molimo vas sacekajte dok skripta ne pokupi nazive filmova sa sajta...')
    cineTv()

    IZBOR = input(f'''\n[+] Sledece opcije su vam na izboru:
    
    [01] - Akcioni filmovi [{len(AKCIJA)}]
    [02] - Animirani filmovi [{len(ANIMIRANI)}]
    [03] - Avanturisticki filmovi [{len(AVANTURA)}]
    [04] - Biografski filmovi [{len(BIOGRAFIJA)}]
    [05] - Dokumentarni filmovi [{len(DOKUMENTARAC)}]
    [06] - Drame [{len(DRAMA)}]
    [07] - Horor filmovi [{len(HOROR)}]
    [08] - Komedije [{len(KOMEDIJA)}]
    [09] - Krimi filmovi [{len(KRIMINALISTICKI)}]
    [10] - Misterije [{len(MISTERIJA)}]
    [11] - Porodicni filmovi [{len(PORODICNI)}]
    [12] - Romanticni filmovi [{len(ROMANSA)}]
    [13] - SciFI filmovi [{len(SCIFI)}]
    [14] - Trileri [{len(TRILER)}]
    [15] - Vestern filmovi [{len(VESTERN)}]
    [00] - Izlazak iz skripte  
      
    [+] Molimo vas unesiti opciju koju zelite: ''')

    if IZBOR not in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']:
        exit('\n[-] Molimo vas pravilno unesite opciju!')

    if IZBOR == '00':
        exit('\n[-] Hvala vam sto ste koristili skriptu!')

    if IZBOR == '01':
        print('\n[+] Izlistavamo zanr AKCIJA:\n')
        for film in AKCIJA:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '02':
        print('\n[+] Izlistavamo zanr ANIMIRANI:\n')
        for film in ANIMIRANI:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '03':
        print('\n[+] Izlistavamo zanr AVANTURA:\n')
        for film in AVANTURA:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '04':
        print('\n[+] Izlistavamo zanr BIOGRAFIJA:\n')
        for film in BIOGRAFIJA:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '05':
        print('\n[+] Izlistavamo zanr DOKUMENTARNI:\n')
        for film in DOKUMENTARAC:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '06':
        print('\n[+] Izlistavamo zanr DRAMA:\n')
        for film in DRAMA:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '07':
        print('\n[+] Izlistavamo zanr HOROR:\n')
        for film in HOROR:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '08':
        print('\n[+] Izlistavamo zanr KOMEDIJA:\n')
        for film in KOMEDIJA:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '09':
        print('\n[+] Izlistavamo zanr KRIMINALISTICKI:\n')
        for film in KRIMINALISTICKI:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '10':
        print('\n[+] Izlistavamo zanr MISTERIJA:\n')
        for film in MISTERIJA:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '11':
        print('\n[+] Izlistavamo zanr PORODICNI:\n')
        for film in PORODICNI:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '12':
        print('\n[+] Izlistavamo zanr ROMANSA:\n')
        for film in ROMANSA:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '13':
        print('\n[+] Izlistavamo zanr SCI-FI:\n')
        for film in SCIFI:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '14':
        print('\n[+] Izlistavamo zanr TRILER:\n')
        for film in TRILER:
            print(f'[+] Naziv filma: {film}')

    if IZBOR == '15':
        print('\n[+] Izlistavamo zanr VESTERN:\n')
        for film in VESTERN:
            print(f'[+] Naziv filma: {film}')