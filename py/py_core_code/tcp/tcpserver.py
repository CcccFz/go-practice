from socket import *
from time import ctime

HOST = ''
PORT = 9999
BUFSIZE = 1024
ADDR =(HOST, PORT)

serTcpSock = socket(AF_INET, SOCK_STREAM)
serTcpSock.bind(ADDR)
serTcpSock.listen(5)

while True:
    print('waiting for connection...')
    cliTcpSock, cliHost = serTcpSock.accept()
    print('...from connected:', cliHost)

    try:
        while True:
            data = cliTcpSock.recv(BUFSIZE).decode()
            if not data:
                break
            cliTcpSock.send(("[%s] %s" % (ctime(), data)).encode())
    except (ConnectionResetError, EOFError, KeyboardInterrupt):
        cliTcpSock.close()
        break

cliTcpSock.close()
serTcpSock.close()

