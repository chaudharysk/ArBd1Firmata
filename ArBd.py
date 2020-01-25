from pyfirmata2 import ArduinoNano, util
import time


class ArBd1:
    def __init__(self, COM):
        self.temp=None
        self.humidity=None
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

    # Enter one or zero to turn off and turn on Rgb led
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

    def charlieplexing(self,A2='Z',A3='Z',A4='L',A5='H'):
        # Z is for high impedence or Input
        # H = HIGH PIN
        # L = LOW PIN
        LED=0
        cmd=0x01 # Command for Charlieplexing
        if (A2=='Z' and A3=='Z' and A4=='L' and A5=='H'):
            LED=1
        elif (A2=='Z' and A3=='L' and A4=='Z' and A5=='H'):
            LED =2
        elif (A2=='L' and A3=='Z' and A4=='Z' and A5=='H'):
            LED=3
        elif (A2=='Z' and A3=='L' and A4=='H' and A5=='Z'):
            LED=4
        elif (A2=='L' and A3=='Z' and A4=='H' and A5=='Z'):
            LED=5
        elif (A2=='Z' and A3=='Z' and A4=='H' and A5=='L'):
            LED=6
        elif (A2=='L' and A3=='H' and A4=='Z' and A5=='Z'):
            LED=7
        elif (A2=='Z' and A3=='H' and A4=='Z' and A5=='0'):
            LED=8
        elif (A2=='Z' and A3=='H' and A4=='L' and A5=='Z'):
            LED=9
        elif (A2=='H' and A3=='Z' and A4=='Z' and A5=='L'):
            LED=10
        elif (A2=='1' and A3=='Z' and A4=='0' and A5=='Z'):
            LED = 11
        elif (A2=='H' and A3=='L' and A4=='Z' and A5=='Z'):
            LED = 12
        data=[LED]
        self.board.send_sysex(cmd,data)
    def charlieplexingPov(self):
       while 1:
           for x in range(1, 13):
               self.board.send_sysex(0x01, [x])


    def dht11(self): # Function to fetch temp and humidity value
        def getDht(*args, **kwargs):
            #print(args)
            # print util.two_byte_iter_to_str(args)
            #print(kwargs)
            self.humidity=args[0]
            self.temp=args[1]


        self.board.add_cmd_handler(0x02,getDht)
        self.board.send_sysex(0x02, [])
        time.sleep(1)
    def tempAndHumidity(self):
        self.dht11()
        return [self.temp,self.humidity]

# board=ArBd1('COM3')
# print(board.tempAndHumidity())

        
    

















# obj = ArBd1("COM7")
# obj.rgbDigital(1,1,1)
# obj.rgbDigital(0,0,0)
# obj.potentiometer()
#obj.ldr()




