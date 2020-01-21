from pyfirmata2 import ArduinoNano, util, Pin
import time




board = ArduinoNano("COM7")
iterator=util.Iterator(board)
iterator.start()
obj=Pin(board,2)

board.get_pin('a:2:o')
board.get_pin('a:3:o')
board.get_pin('a:4:i')
board.analog[2].write(1)
board.analog[3].write(0)
time.sleep(1)
board.release_pin('a:4:i')
board.release_pin('a:3:i')
board.get_pin('a:3:i')
board.get_pin('a:4:o')
board.analog[4].write(0)


