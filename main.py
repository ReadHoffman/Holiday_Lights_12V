# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
from functions import *
from defs import *



if __name__ == '__main__':
    run_rainbow(2)
    reset(1)
    toggle(1,[RED,GREEN],10)
    reset(1)
