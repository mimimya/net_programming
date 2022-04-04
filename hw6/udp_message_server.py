from socket import *
BUFF_SIZE = 1024
port = 7777

mBox = {}


s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    msg = data.decode().split(' ')
    commend = msg[0]
    id = msg[1]
    Message = ''
    for (i,k) in enumerate(msg):
        if i == 0:
            commend = k
        elif i == 1:
            id = k
        else:
            Message = Message+' '+k
    #Message = msg[2]
    #commend = 'receive'
    #id = '1'
    #Message = 'Hi'
    total = []
    if commend == 'send':
        if id in mBox:#key is str
            total = total+mBox[id] #Hi
            total.append(Message) # {A:[Hi, bye]}
            mBox.update([(id, total)])
            print(mBox)
        else:
            mBox[id] = [Message]
        s_sock.sendto(b"OK", addr)
    elif commend == 'receive':
        if id in mBox:
            if len(mBox[id]) > 0:
                s_sock.sendto(mBox[id].pop().encode(), addr)
            else:
                s_sock.sendto(b"No messages.",addr)
        else:
            s_sock.sendto(b"No messages.", addr)
    elif commend == 'quit' or commend == 'q':
        s_sock.close()