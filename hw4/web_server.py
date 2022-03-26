from socket import *
import parse
s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n') #req[0]HTTP Request 의 첫 번째 줄

    filename = parse.parse("GET /{} HTTP/1.1", req[0])
   
    if filename[0] == 'index.html':
        f=open('C:/Users/tjswn/Documents/net_program/hw4/index.html', 'r', encoding = 'utf-8')
        sending = f.read().encode()
    elif filename[0] == 'iot.png':
        f=open('C:/Users/tjswn/Documents/net_program/hw4/iot.png', 'rb')
        sending = f.read()
    elif filename[0] == 'favicon.ico':
        f=open('C:/Users/tjswn/Documents/net_program/hw4/favicon.ico', 'rb')
        sending = f.read()
    else :
        sending= (('HTTP/1.1 404 Not Found\r\n'+'\r\n'+'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'+'<BODY>Not Found</BODY></HTML>').encode())

    c.send(sending)
    c.close()