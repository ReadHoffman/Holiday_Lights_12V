# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
from functions import *
from defs import *
import time



if __name__ == '__main__':
    try:
        while True:
            hour = time.localtime().tm_hour
            if  (hour>=11 and hour <22) or (hour>5 and hour <8):
                pass
            else:
                time.sleep(60)
                continue
            random_points(.1,[WHITE],1)
            reset(1)
            random_points(.1,[RED,GREEN],1)
            reset(1)
            plinko_color(1,[RED,GREEN],.5,.02,5)
            reset(1)
            slide_and_stop(1,[WHITE,GREEN],1,.02)
            reset(1)
            run_rainbow(2)
            reset(1)
            toggle(1,[RED,GREEN],4)
            reset(1)
    except KeyboardInterrupt:
        print(print('\nShows over folks!'))
        pass
    
pixels.deinit()
