from socket import *
import random

port =3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)


while True:
    msg = input('->')
    reTx = 0
    while reTx <=3:
        resp = str(reTx) + ' ' +msg
        sock.sendto(resp.encode(), ('localhost', port))
        sock.settimeout(2)
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:#ack을 시간 안에 못받았을 대
            reTx += 1
            continue
        else:
            break #시간 안에 받았을 때
    
    while True:
        sock.settimeout(None)
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:#50%확률로 손실
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break