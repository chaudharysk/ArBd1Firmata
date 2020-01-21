import time
import signal
import sys

from PyMata.pymata import PyMata

board=PyMata("COM3")
board.digital_write(1,0)