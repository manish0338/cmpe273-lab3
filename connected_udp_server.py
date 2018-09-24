from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def datagramReceived(self, data, address):
        print("received %r from %s" % (data, address))

    def connectionRefused(self):
        print("No one listening")

reactor.listenUDP(1234, Helloer())
reactor.run()