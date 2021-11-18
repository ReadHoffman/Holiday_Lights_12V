import time
from defs import *



def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
        
def run_rainbow(cycle_limit):
    cycle = 0
    while cycle<cycle_limit:
        rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
        cycle += 1

def toggle(wait,colors_list,cycle_limit):
    cycle = 0
    while cycle < cycle_limit:
        color_ct = len(colors_list)
        for i in range(num_pixels):
            pixels[i] = colors_list[(i+cycle) % color_ct]
        pixels.show()
        cycle +=1
        time.sleep(wait)

def reset(wait):
    pixels.fill(BLACK)
    pixels.show()
    time.sleep(wait) 
