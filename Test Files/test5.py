from pyfirmata2 import ArduinoNano, Board
import time
board = ArduinoNano('COM6')
board.digital[9].write(0)