import time
import signal
import sys

from PyMata.pymata import PyMata

board=PyMata("COM6")
board.digital_write(9,1)