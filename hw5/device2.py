from socket import *
import random
port = 2555
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)


while True:
    conn, addr = sock.accept()
    heartbeat = random.randint(40,140)
    steps = random.randint(2000,6000)
    cal = random.randint(1000,4000)
    
    msg = conn.recv(BUFFSIZE).decode()
    if not msg:
        break
    if msg == 'Request':
        conn.send(('Device2: Heartbeat={}, Steps={}, Cal={}'.format(heartbeat, steps, cal)).encode())
    elif msg == 'quit':
        break    
conn.close()
sock.close()
