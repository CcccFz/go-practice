from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 9998
ADDR = (HOST, PORT)

class MyStreamHandler(SRH):
    def handle(self):
        print('...from connected:', self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline().decode())).encode())

tcpServ = TCP(ADDR, MyStreamHandler)
print('waiting for connection...')
tcpServ.serve_forever()

