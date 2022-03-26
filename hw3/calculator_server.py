from operator import indexOf
from socket import *

#https://saynot.tistory.com/entry/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%88%98%EC%8B%9D%EC%9D%98-%ED%9B%84%EC%9C%84-%ED%91%9C%EA%B8%B0%EB%B2%95-%EB%B3%80%ED%99%98-%EA%B3%84%EC%82%B0-python
def infixTopostfix(tokenList): #중위 표현식을 후위 표현식으로 변환
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = []
    postfixList = []

    for token in tokenList:
        if type(token) is float:
            postfixList.append(token)
                    
        elif token == ')':
            if token == ')' and len(opStack)>1:
                while opStack[-1] != '(':
                    postfixList.append(opStack.pop(-1))
                opStack.pop(-1)
        else:# 3 */, 2 + -,  1 (
            if len(opStack)>0: 
                if prec[opStack[-1]] >= prec[token] and token != '(':
                    postfixList.append(opStack.pop(-1))
                    opStack.append(token)
                elif prec[opStack[-1]] <= prec[token] and token == '(':
                    opStack.append(token)
                else:
                    opStack.append(token)
            elif len(opStack) == 0:
                opStack.append(token)

    while not len(opStack) == 0:
        postfixList.append(opStack.pop(-1))

    return postfixList


def postfixEval(tokenList): #후위 표현식 계산
    opStack = []
    for token in tokenList:
        if type(token) is float:
            opStack.append(token)
        elif token == '*':
            tmp1 = opStack.pop(-1)
            tmp2 = opStack.pop(-1)
            opStack.append(tmp2*tmp1)
        elif token == '/':
            tmp1 = opStack.pop(-1)
            tmp2 = opStack.pop(-1)
            opStack.append(tmp2/tmp1)
        elif token == '+':
            tmp1 = opStack.pop(-1)
            tmp2 = opStack.pop(-1)
            opStack.append(tmp2+tmp1)
        elif token == '-':
            tmp1 = opStack.pop(-1)
            tmp2 = opStack.pop(-1)
            opStack.append(tmp2-tmp1)
    return opStack.pop(-1)

s= socket(AF_INET, SOCK_STREAM)
s.bind(('', 9876))
s.listen(1)

while True:
    client, addr = s.accept()
    fomul = client.recv(1024)
    if not fomul:
        break
    try: fomul = fomul.decode()
    except:
        client.send(b"Try again")
    else:
        print("Received : %s"% fomul)
        #문자열을 토큰화 
        tokens=[]
        num = '0'
        for i in fomul:
            if i in ['+','-','*','/','(',')']:
                tokens.append(float(num))
                tokens.append(i)
                num='0'
            elif i == ' ':
                None
            else:
                num = num+str(i)
        if num != '0':
            tokens.append(float(num)) # 마지막 피연산자

        print("tokens : ", tokens)
        postfix = infixTopostfix(tokens) #중위 표현식 > 후위 표현식
        print("postfix : ", postfix)
        res = postfixEval(postfix) #후위 표현식 계산
        print(res)
        #결과 송신
        client.send(("%.1f"%float(res)).encode())
        client.close()
s.close()