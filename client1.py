# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:55:01 2020

@author: Andy
"""

#import module socket
import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host,port))
print("Connected to the server")
msg = s.recv(1024)
msg = msg.decode()
print("Server Message : ", msg)

while 1:
    msg = s.recv(1024)
    msg = msg.decode()
    print("Server : ",msg)
    new_message = input(str("Anda : "))
    new_message = new_message.encode()
    s.send(new_message)
		
	