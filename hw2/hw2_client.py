from socket import*

sock = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())
#본인의 이름을 문자열로 전송
sock.send(b'Sunjoo Park')
#본인의 학번을 수신 후 출력
msg = sock.recv(1024)
print(int.from_bytes(msg,'big'))
sock.close()