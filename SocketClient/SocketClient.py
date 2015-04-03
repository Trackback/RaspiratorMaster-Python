__author__ = 'trackback'

import asynchat
import asyncore
import socket
import threading
from Loger import Loger
debug = Loger()
tag = "Client"


class SocketClient(asynchat.async_chat):
    def __init__(self):
        pass

    def start(self, host, port):
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))

        self.set_terminator('\n')
        self.buffer = []

    def collect_incoming_data(self, data):
        #pass
        self.buffer.append(data)

    def found_terminator(self):
        #pass
        msg = ''.join(self.buffer)
        debug.i(tag, 'Received:' + msg)
        self.buffer = []

    def handle_read(self):
        data = self.recv(1024)
        if data is None:
            return
        data = data.decode("UTF-8")
        debug.i("", data)

    def loop(self):
        comm = threading.Thread(target=asyncore.loop)
        comm.daemon = True
        comm.start()

        while True:
            msg = input('> ')
            self.push(bytes(msg, "UTF-8"))