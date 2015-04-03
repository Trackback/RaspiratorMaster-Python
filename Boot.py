__author__ = 'trackback'

from Loger import Loger
from Core import Core

tag = "Boot"
debug = Loger()
core = Core()

debug.i(tag, "Initing")
core.boot()

debug.i(tag, "Ready")