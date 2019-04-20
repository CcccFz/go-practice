from socket import *
from time import ctime

HOST = ''
PORT = 9999
BUFSIZE = 1024
ADDR =(HOST, PORT)

serUdpSock = socket(AF_INET, SOCK_DGRAM)
serUdpSock.bind(ADDR)

try:
    while True:
        print('waiting for message...')
        data, cliAddr = serUdpSock.recvfrom(BUFSIZE)
        serUdpSock.sendto(("[%s] %s" % (ctime(), data.decode())).encode(), cliAddr)
        print('...received from and returned to ', cliAddr)

except (ConnectionResetError, EOFError, KeyboardInterrupt):
    serUdpSock.close()

