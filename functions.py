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

def plinko_color(wait,colors_list,cycle_limit,speed,plinko_size,background_color):
    pixels.fill(background_color)
    pixels.show()
    color_ct = len(colors_list)
    cycle = 0
    while cycle < cycle_limit:
        plinko_chip = 0
        #iterate thru all pixels
        plinko_already_stacked = 0
        zone_max_length = max([ max-min+1 for min,max in ZONES])
        while plinko_already_stacked < zone_max_length + plinko_size:
            #toggle through color list
            color = colors_list[plinko_chip % color_ct]

            #iterate thru available pixels not already stacked
            lead_pixel = 0
            while lead_pixel < zone_max_length:
                for zone in ZONES:
                    zone_max_pixel = zone[1]
                    zone_min_pixel = zone[0]
                    zone_lead_pixel = lead_pixel + zone_min_pixel
                    if zone_lead_pixel < zone_max_pixel - plinko_already_stacked:
                        for background_pixel in range(zone_min_pixel,zone_lead_pixel):
                            pixels[background_pixel] = background_color
                        for plinko_stack_pixel in range(zone_lead_pixel-plinko_size+1,zone_lead_pixel+1):
                            if plinko_stack_pixel >= 0 and plinko_stack_pixel < zone_max_pixel: 
                                pixels[plinko_stack_pixel] = color
                        pixels.show()
                    time.sleep(speed)
                lead_pixel += 1
                
            plinko_chip += 1
            plinko_already_stacked = plinko_size*plinko_chip
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
