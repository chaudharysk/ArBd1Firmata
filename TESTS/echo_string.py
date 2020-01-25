import time

import pyfirmata
from pyfirmata import Arduino, util


def main():
    board = Arduino("COM3")
    board.add_cmd_handler(pyfirmata.pyfirmata.STRING_DATA, on_string_received)

    iter = util.Iterator(board)
    iter.start()

    write_loop(board)


def write_loop(board):
    # msg_list = []
    # msg_list.append("X")
    # msg_list.append("A")
    # msg_list.append("Q")
    # msg_list.append("T")

    i = 0

    while True:

        message = util.str_to_two_byte_iter("©")

        board.send_sysex(pyfirmata.pyfirmata.STRING_DATA, message)

        i += 1

        # if i >= len(msg_list):
        #     i = 0

        time.sleep(0.5)


def on_string_received(*args, **kwargs):
    print(args)
    # print util.two_byte_iter_to_str(args)
    print(kwargs)


if __name__ == "__main__":
    main()