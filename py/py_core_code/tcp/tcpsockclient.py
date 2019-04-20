from socket import *

HOST = 'localhost'
PORT = 9998
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    cliTcpSock = socket(AF_INET, SOCK_STREAM)
    cliTcpSock.connect(ADDR)

    data = input('> ')
    if not data:
        break
    cliTcpSock.send(('%s\r\n' % data).encode())

    data = cliTcpSock.recv(BUFSIZE).decode()
    if not data:
        break
    print(data.strip())

    cliTcpSock.close()