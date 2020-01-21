from pyfirmata2 import ArduinoNano, util
import time
board = ArduinoNano('COM3')
board.digital[9].write(1)

#
# board.get_pin('a:0:i')
# board.release_pin('a:0:i')












# board.get_pin('d:9:p').write(0.5)
# time.sleep(1)
# board.release_pin('d:9:p')
# time.sleep(1)
# x=board.get_pin('d:9:i').read()
# print(x)
# time.sleep(1)
# print(x)