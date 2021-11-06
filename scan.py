#Copyright ©Kenzawa/Bahwa
#Please if you respect me then don't recode
#Thx From author

import certifi
import urllib3
import argparse
import time
from colorama import Fore
import sys
from urllib3.exceptions import MaxRetryError

from urllib3.util.timeout import Timeout

b = '\033[34;1m'
g = Fore.LIGHTGREEN_EX
c = Fore.LIGHTCYAN_EX
r = Fore.LIGHTRED_EX
w = Fore.LIGHTWHITE_EX

logo = f"""{b}
       _  __    _____ _           _                        
      | |/ /___|  ___(_)_ __   __| | ___ _ __   
      | ' // __| |_  | | '_ \ / _` |/ _ \ '__| 
      | . \ (__|  _| | | | | | (_| |  __/ |    
      |_|\_\___|_|   |_|_| |_|\__,_|\___|_|   
{r}                                                                
==================Information=====================
||Tools     : KcFinder MasScan                  ||
||Author    : Kenzawa/Babwa                     ||
||help      : CLI Python3                       ||
||github    : https://github.com/pengode-handal ||
==================Information=====================
"""
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='Put URL')
parser.add_argument('-l', '--list', help='File Contain URL')
parser.add_argument('-s', '--save', help='If Result Wan\'t To Be Saved')
parser.add_argument('-v', '--version', action='version', version='0.2.1')

args = parser.parse_args()

def getUrl(url):
    urls = []
    with open(url, "r") as ufile:
        allurl = ufile.readlines()
        for i in range(len(allurl)):
            urls.append(allurl[i].strip('\n'))
        return urls
adaa = []
def scan(url):
    try:
        http = urllib3.PoolManager(ca_certs=certifi.where())
        target = url
        #mengecek prokotol
        target = target.replace('https://', '')
        target = target.replace('http://', '')
        tar_list = target.split('/')
        for tar in tar_list:
            if tar == '':
                tar_list.remove(tar)
        target = '/'.join(tar_list)
        url = 'http://' + target

        wl = getUrl('list')
        count = 0
        garis = open('list','r').read().splitlines()
        
        for i in wl:
            count = count + 1
            www = url+i 
            if count >= len(garis):
              print("\n"+target + " Is Done")
            sys.stdout.write(f'\r{w}Progress: {count}/{len(garis)}')
            time.sleep(0.01)
            try:
                get = http.request('GET', www)
            except:
                www = 'https://'+target+i 
                get = http.request('GET', www)
            if get.status == 404 or 'Not Found' in get.data.decode('utf-8') or 'not found' in get.data.decode('utf-8'):
                pass
            elif get.status == 302:
                time.sleep(0.2)
                adaa.append(g+'\n[*] '+c+url+r+' ==> Redirected - '+www)
            elif get.status == 200:
                time.sleep(0.2)
                adaa.append(b+'\n[+] '+url+c+' ==> Found!! - '+www)
                
                if args.save:
                    logger(pika=www, nma=args.save)
                else:
                    pass
            elif get.status == 403:
                pass
            elif get.status == 500:
                pass
            else:
                pass
        
    except MaxRetryError:
        print("\nConnection Error")
        exit()



def logger(pika, nma):
    file = open(str(nma) + ".txt", "a")
    file.write(str(pika))
    file.write("\n")    
    file.close()

print(logo)

if args.url:
    start = time.time()
    print(w+"=====================Progress=====================")
    scan(args.url)
    print(w+"\n##########{}RESULT{}{}###########".format(b, c, w))
    for ada in adaa:
      print(ada)
    stop = time.time()
    print('\nFinished in {} second'.format(int(stop - start)))
elif args.list:
    urll = getUrl(args.list)
    start = time.time()
    print(w+"=====================Progress=====================")
    for link in urll:
            scan(link)
    print(w+"\n##########{}RESULT{}{}###########".format(b, c, w))
    for ada in adaa:
      print(ada)
    stop = time.time()
    print('\nFinished in {} second'.format(int(stop - start)))
