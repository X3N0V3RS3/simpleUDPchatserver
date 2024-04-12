#coding: utf-8
#Script Written by X3N0V3RS3
import socket,sys,time,os,subprocess,threading


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
s.bind(("192.168.1.99", 100))

iplist = []
chatlist = []
while True:
    data,addr = s.recvfrom(999999)
    ip = addr[0]
    port = addr[1]
    address = (ip, port)
    iplist.append(address)
    chatlist.append(data)
    set(iplist)
    #print(iplist)
    print(data,address)
    #servertxtcoded = (f"{data}{addr}")
    servertextcoded = (f"{chatlist}").strip()
    s.sendto(servertextcoded.encode("ascii"), (ip,port))
    
    
