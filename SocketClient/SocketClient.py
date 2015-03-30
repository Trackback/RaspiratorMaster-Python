__author__ = 'trackback'
import socket
from Loger import  Loger
debug = Loger.Loger()
tag = "Client"
MSGLEN = 1024


class SocketClient:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.conn = False

    def connect(self, host, port):
        self.conn = True
        self.sock.connect((host, port))

    def say(self, msg):
        if self.conn is True:
            debug.i(tag, "Sending: "+msg)
            self.sock.send(bytes(msg, "UTF-8"))
        else:
            debug.i(tag, "Connection is not establishment")

    def receive(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                debug.i(tag, 11)
                break
            data = data.decode("utf-8")
            debug.i(tag, data)

    def close(self):
        self.sock.close()