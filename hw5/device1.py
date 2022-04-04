from socket import *
import random
port = 2500
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(2)


while True:
    conn, addr = sock.accept()
    temp = random.randint(0,40)
    humid = random.randint(0,50)
    lilum = random.randint(70,150)
    
    msg = conn.recv(BUFFSIZE).decode()
    if not msg:
        break
    if msg == 'Request':
        conn.send(('Device1: Temp={}, Humid={}, lilum={}'.format(temp, humid, lilum)).encode())
    elif msg == 'quit':
        break
    else: conn.send(b'Retry!')   
conn.close()
sock.close()