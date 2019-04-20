from socket import *

HOST = 'localhost'
PORT = 9999
BUFSIZE = 1024
ADDR = (HOST, PORT)

cliUdpSock = socket(AF_INET, SOCK_DGRAM)

try:
    while True:
        data = input('> ')
        if not data:
            break
        cliUdpSock.sendto(data.encode(), ADDR)

        data = cliUdpSock.recvfrom(BUFSIZE)[0]
        if not data:
            break
        print(data.decode())

except (EOFError, KeyboardInterrupt):
    cliUdpSock.close()