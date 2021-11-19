import time
from defs import *
import random



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
        
        
def slide_and_stop(wait,colors_list,cycle_limit,speed):
    pixels.fill(BLACK)
    pixels.show()
    color_ct = len(colors_list)
    cycle = 0
    while cycle < cycle_limit:
        for j in range(num_pixels):
            color = colors_list[j % color_ct]
            for i in range(num_pixels-j*5):
                pixels[i] = color
                pixels.show()
                time.sleep(speed)
        cycle += 1

def plinko_color(wait,colors_list,cycle_limit,speed,plinko_size):
    pixels.fill(BLACK)
    pixels.show()
    color_ct = len(colors_list)
    cycle = 0
    while cycle < cycle_limit:
        j = 0
        while j < num_pixels:
            plinko_length = plinko_size*j
            color = colors_list[j % color_ct]
            i=0
            while i < num_pixels-plinko_length:
                for k in range(i):
                    pixels[k] = BLACK
                for m in range(i-plinko_size,i):
                    if m < 0: continue
                    pixels[m] = color
                pixels.show()
                time.sleep(speed)
                i += 1 
            j += 1
        cycle += 1

def random_points(wait,colors_list,cycle_limit):
    cycle = 0
    while cycle < cycle_limit:
        pixel_list = list(range(num_pixels))
        random.shuffle(pixel_list)
        color_ct = len(colors_list)
        for i in pixel_list:
            color = colors_list[i % color_ct]
            pixels[i] = color
            pixels.show()
            time.sleep(wait)
        time.sleep(3)
        pixels.fill(BLACK)
        pixels.show()
        cycle += 1
        

def reset(wait):
    pixels.fill(BLACK)
    pixels.show()
    time.sleep(wait) 
