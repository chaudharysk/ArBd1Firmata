# from pyfirmata2 import ArduinoNano,pyfirmata2
# board=ArduinoNano('COM6')
# board.send_sysex(5,[45])
# #print(board.getDataValue())
# board.send_sysex(0x10,[])
# print(board.getDataValue())
# print(board.get_firmata_version())

from ArBd import ArBd1
board =ArBd1('COM6')
board.rgbDigital(1,1,1)