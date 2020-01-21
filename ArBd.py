from pyfirmata2 import ArduinoNano, util
import time


class ArBd1:
    def __init__(self, COM):
        self.board = ArduinoNano(COM)
        self.iterator=util.Iterator(self.board)
        self.iterator.start()
        # RGB PINS
        self.board.get_pin('d:9:p')
        self.board.get_pin('d:10:p')
        self.board.get_pin('d:11:p')
        # BUZZER PIN
        self.board.get_pin('d:6:p')
        # Navigation Switches
        self.board.get_pin('a:1:o')
        # Potentiometer
        self.board.get_pin('a:6:o')
        # LDR
        self.board.get_pin('a:7:o')
        # Charlieplexed LEDs
        self.board.get_pin('a:2:o')
        self.board.get_pin('a:3:o')
        self.board.get_pin('a:4:o')




        pass

    # Enter one or zero to yurn off and turn on Rgb led
    def rgbDigital(self, r, g, b):
        self.board.digital[9].write(g)
        self.board.digital[10].write(b)
        self.board.digital[11].write(r)

    # takes value from 0 to 255
    def rgbAnalog(self, r, g, b):
        self.board.digital[9].write(g / 255)
        self.board.digital[10].write(b / 255)
        self.board.digital[11].write(r / 255)



    def buzzerAnalog(self,value):
        self.board.digital[6].write(value)
    def buzzerDigital(self,value):
        self.board.get_pin('d:6:o').write(value)

    def navigationSwitches(self):
        time.sleep(1)
        prevValue=self.board.analog[1].read()
        value = self.board.analog[1].read()
        print(prevValue)
        while(1):
            time.sleep(0.1)
            value = self.board.analog[1].read()
            if (value<prevValue+0.02 and value > prevValue-0.02):
                pass

            elif value >= 0 and value < 0.01:
                print("Up Pressed")
            elif value >= 0.79 and value < 0.81:
                print("Down Pressed")
            elif value >= 0.47 and value < 0.52:
                print("Left Pressed")
            elif value >= 0.745 and value < 0.755:
                print("Right Pressed")
            elif value >= 0.655 and value < 0.675:
                print("Center Pressed")
            prevValue=value
    def potentiometer(self):
        while (1):
            time.sleep(0.1)
            value = self.board.analog[6].read()
            print(value)

    def ldr(self):
        while(1):
            time.sleep(0.1)
            value = self.board.analog[7].read()
            print(value)

    def charlieplexing(self):
        pass

















# obj = ArBd1("COM7")
# obj.rgbDigital(1,1,1)
# obj.rgbDigital(0,0,0)
# obj.potentiometer()
#obj.ldr()




