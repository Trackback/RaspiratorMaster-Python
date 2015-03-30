from asyncio.locks import Condition
from distutils.command.config import config

__author__ = 'trackback'

from SocketClient import SocketClient
from Loger import Loger
from GUI import GUI
from GUI import Console
from threading import Thread

sock = SocketClient.SocketClient()
gui = GUI.GUI()
console = Console.Console()
class Core:
    def __init__(self):
        pass

    def boot(self):
        sock.connect("localhost", 9091)
        console.catch(self.sendCommand)



    def sendCommand(self, command):
        sock.say(command)