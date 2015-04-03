__author__ = 'trackback'

from SocketClient import SocketClient


sock = SocketClient()

class Core:
    def __init__(self):
        pass

    def boot(self):
        sock.start("localhost", 9091)
        sock.loop()

    def sendCommand(self, command):
        sock.say(command)
