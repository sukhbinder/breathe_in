import sys
import threading
import time

import keyboard

TEXT = ["BREATHE IN", "HOLD", "BREATHE OUT"]
JJ = [0, 4, 11]


def my_code():
    """
    The actual function to do the breathe patterns.

    It rings a ``ding`` to alert user for hold breathe in and out

    """
    i = 0
    j = 0
    while True:
        print(" "*50, "\r", end="")
        if i in [0, 4, 11, 19]:
            print("\t\t\t{} {}".format(TEXT[j], i - JJ[j]), "\a", end="")
        else:
            print("\t\t\t{} {}".format(TEXT[j], i - JJ[j]), end="")
        time.sleep(1)
        i = i+1
        if i > 4:
            j = 1
        if i > 11:
            j = 2
        if i >= 19:
            i = 0
            j = 0


def main():
    my_thread = threading.Thread(target=my_code, daemon=True).start()
    print("Press ESC  to quit")
    keyboard.wait("esc")
    sys.exit()
