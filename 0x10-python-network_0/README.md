# Python Networking Cheat Sheet

This cheat sheet provides a quick reference for common networking tasks in Python.

## Table of Contents

- [Socket Programming](#socket-programming)
- [HTTP Requests](#http-requests)
- [UDP and TCP](#udp-and-tcp)
- [DNS Lookup](#dns-lookup)
- [Ping](#ping)

---

## Socket Programming


### TCP Server

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    # Handle client_socket
    client_socket.close()



# TCP Client
python

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))
client_socket.send(b"Hello, server!")
data = client_socket.recv(1024)
client_socket.close()



# UDP Server
python

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 8888))

while True:
    data, client_address = server_socket.recvfrom(1024)
    # Handle data and client_address



# UDP Client
python

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b"Hello, server!", ('localhost', 8888))


## HTTP Requests

# Using requests Library
- Install the requests library: pip install requests

python

import requests

response = requests.get('https://www.example.com')
print(response.text)


## UDP and TCP

# UDP Client and Server
- UDP Server and Client examples are provided in the "Socket Programming" section above.

# TCP Client and Server
- TCP Server and Client examples are provided in the "Socket Programming" section above.


# DNS Lookup


import socket

ip_address = socket.gethostbyname('www.example.com')
print(f'IP Address: {ip_address}')


# Ping
python

import os

hostname = "www.example.com"
response = os.system("ping -c 1 " + hostname)

if response == 0:
    print(f'{hostname} is up')
else:
    print(f'{hostname} is down')
