#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'ytDownloader.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
from subprocess import call

try:
    from pytube import YouTube
    from pytube import Playlist
    from pytube.cli import on_progress
    from colorama import Fore
except:
    call('pip3 install colorama pytube', shell=True)
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

if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja skida video i audio zapis sa Youtube.\n')
    URL = input('[+] Molimo vas unesiti Youtube link: ')

    try:
        VIDEO = YouTube(URL, on_progress_callback=on_progress)
        print(f'\n[+] Naziv klipa za skidanje: {VIDEO.title}')
        print(f'[+] Autor klipa: {VIDEO.author}')
        print(f'[+] Trajanje klipa: {round(VIDEO.length / 60, 2)}')
        print(f'[+] Broj pregleda: {VIDEO.views}')
        print(f'[+] Rejting: {VIDEO.rating}\n')
    except:
        exit('\n[-] Proverite da li ste pravilno uneli link!')

    IZBOR = int(input('''[+] Ponudjene opcije:

    [0] - Skinite video u 144p  (Verovatno bez zvuka)
    [1] - Skinite video u 240p  (Verovatno bez zvuka)
    [2] - Skinite video u 360p  (Verovatno zvuk radi)
    [3] - Skinite video u 480p  (Verovatno bez zvuka)
    [4] - Skinite video u 720p  (Verovatno bez zvuka)
    [5] - Skinite video u 1080p (Verovatno bez zvuka)
    [6] - Skinite audio u mp4 
    [7] - Skinite video sa zvukom
    [8] - Skinite playlistu u mp4 formatu
    [9] - Skinite playlistu u video formatu

    [+] Molimo vas izaberite jednu od ponudjenih opcija: '''))

    if IZBOR not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        exit('\n[-] Niste uneli pravilan izbor!')

    REZOLUCIJA = ['160', '133', '18', '135', '22', '137', '140']

    if IZBOR == 7:
        STREAM = VIDEO.streams.filter(progressive=True).first()
        print(f'\n[+] Molimo vas sacekajte dok se [ {VIDEO.title} ] skida ...\n')
        STREAM.download()
        print(f'\n\n[+] Uspesno ste skinuli fajl!')
        exit()

    if IZBOR == 8:

        try:
            PLAYLISTA = Playlist(URL)
            for audio in PLAYLISTA.videos:
                print(f'\n[+] Molimo vas sacekajte dok se [ {audio.title} ] skida ...')
                audio.streams.get_by_itag('140').download()
                print(f'[+] Uspesno ste skinuli fajl!')
        except:
            exit('\n[-] Proverite da li je link od videa koji se nalazi u playlisti!')
        exit()

    if IZBOR == 9:
        try:
            PLAYLISTA = Playlist(URL)
            for video in PLAYLISTA.videos:
                print(f'\n[+] Molimo vas sacekajte dok se [ {video.title} ] skida ...')
                video.streams.filter(progressive=True).first().download()
                print(f'[+] Uspesno ste skinuli fajl!')
        except:
            exit('\n[-] Proverite da li je link od videa koji se nalazi u playlisti!')
        exit()

    try:
        STREAM = VIDEO.streams.get_by_itag(REZOLUCIJA[IZBOR])
        print(f'\n[+] Molimo vas sacekajte dok se [ {VIDEO.title} ] skida ...\n')
        STREAM.download()
        print(f'\n\n[+] Uspesno ste skinuli fajl!')
    except:
        exit('\n[-] Rezolucija nije dostupna!')
