__author__ = 'trackback'

from Loger import Loger

debug = Loger.Loger()
tag = "Console"

class Console:
    def __init__(self):
        pass

    def catch(self, callback=None):
        if callback is not None:
            self.callback = callback
        else:
            debug.w(tag, "No callback specified")

        data = input()
        if self.callback is not None:
            self.callback(data)