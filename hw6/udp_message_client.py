from socket import *

BUFF_SIZE = 1024
port = 7777

c_sock = socket(AF_INET,SOCK_DGRAM)
c_sock.connect(('localhost', port))

while True:
    data = input("Enter the message(\"send mboxId message\" or \"receive mboxId\"):")
    c_sock.send(data.encode())
    if data == 'quit' or data =='q':
        c_sock.close()
    msg = c_sock.recv(BUFF_SIZE).decode()
    print(msg)
  