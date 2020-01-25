import time

import pyfirmata
from pyfirmata import Arduino, util

humidity=()
k=0
def main():
    board = Arduino("COM3")
    board.add_cmd_handler(0x02, on_string_received)
    iter = util.Iterator(board)
    iter.start()

    board.send_sysex(0x02, [])
    time.sleep(1)
    # board.send_sysex(pyfirmata.pyfirmata.STRING_DATA, [2])
    # time.sleep(1)
    # board.send_sysex(pyfirmata.pyfirmata.STRING_DATA, [3])
    # time.sleep(1)
    #print(humidity)
    print(k)


def on_string_received(*args, **kwargs):
    print(type(args))
    k=args[0]
    #print(args[0])
    # print util.two_byte_iter_to_str(args)
    #print(kwargs)
    #humidity=args
    # temp=args[1]





if __name__ == "__main__":
    main()
