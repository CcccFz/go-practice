from twisted.internet import protocol, reactor
from time import ctime

PORT = 9999

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        print('...connected from:', self.transport.client)

    def dataReceived(self, data):
        self.transport.write(('[%s] %s' % (ctime(), data)).encode())

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()