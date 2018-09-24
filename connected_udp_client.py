from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 1234

        self.transport.connect(host, port)
        print("now we can only send to host %s port %d" % (host, port))
        self.transport.write(str.encode("hello world"))

reactor.listenUDP(1245, Helloer())
reactor.run()