from socket import *

HOST = 'localhost'
PORT = 9999
BUFSIZE = 1024
ADDR = (HOST, PORT)

cliTcpSock = socket(AF_INET, SOCK_STREAM)
cliTcpSock.connect(ADDR)

try:
    while True:
        data = input('> ')
        if not data:
            break
        cliTcpSock.send(data.encode())

        data = cliTcpSock.recv(BUFSIZE).decode()
        if not data:
            break
        print(data)

except (EOFError, KeyboardInterrupt):
    cliTcpSock.close()