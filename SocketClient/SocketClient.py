__author__ = 'trackback'

import asyncore, socket
from Loger import Loger
debug = Loger.Loger()
tag = "Client"


class SocketClient(asyncore.dispatcher):
    def __init__(self):
        pass

    def start(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.out_buffer = "123"

    def handle_close(self):
        self.close()

    def handle_read(self):
        debug.i(tag, 'Received' + self.recv(1024).decode("UTF-8"))
        #self.close()

    def say(self, data):
        #self.out_buffer = data
        self.send(bytes(data, "UTF-8"))

    def loop(self):
        asyncore.loop()