from socket import *
from time import *


BUFFSIZE = 1024
f = open('data.txt', 'w')
while True:
    received = ''
    m=''
    msg = input("Select device: ")
    if msg == '1':
        while True:
            if m =='quit':break
            s = socket(AF_INET, SOCK_STREAM)#[WinError 10053]
            s.connect(('localhost', 2500))  
            m = input("type 'Request': ")
            s.send(m.encode())
            received = s.recv(BUFFSIZE).decode()
            print(received)
            f.write(asctime()+': '+str(received)+'\n')    
            s.close()

    elif msg == '2':
        while True:
            m = input("type 'Request': ")
            if m =='quit':break
            s = socket(AF_INET, SOCK_STREAM)#[WinError 10053]
            s.connect(('localhost', 2555))  
            s.send(m.encode())
            received = s.recv(BUFFSIZE).decode()
            print(received)
            f.write(asctime()+': '+str(received)+'\n')    
            s.close() 
    elif msg == 'quit':break
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 2500))
s.send(b'quit')
s.close()
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 2555))
s.send(b'quit')
s.close()
        
f.close()
