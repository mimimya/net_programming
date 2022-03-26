from socket import *




while True:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 9876))
    text = input("수식 입력 (q 종료) : ")
    if (text == 'q'): break
    s.send(text.encode())
    try:
        msg = s.recv(1024)
    except:
        print("다시 시도해주세요")
        s.close()
        continue
    else:
        if not msg :
            break
        print(msg.decode())
    s.close()