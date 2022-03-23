from socket import *

s= socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello '+addr[0].encode())
    msg = client.recv(1024)
    print(msg.decode())
 
    client.send((20191547).to_bytes(8,'big'))
    client.close()