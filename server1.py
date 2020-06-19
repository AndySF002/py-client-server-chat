# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:55:22 2020

@author: Andy
"""
#import module socket
import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))
s.listen(5)
print("menunggu koneksi dari client...")
conn,addr = s.accept()
print("Client telah terkoneksi..")
conn.send("Welcome to the Server...".encode())

while 1:
    msg = input(str("Anda : "))
    msg = msg.encode()
    conn.send(msg)
    print("Pesan Terkirim ...")
    recv_msg = conn.recv(1024)
    print("client :", recv_msg.decode())
    	
