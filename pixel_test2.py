import board
#print(dir(board))
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 100, brightness=.3)

pixels.fill((255, 255, 255))
#pixels.show()

time.sleep(3)
pixels.fill((0, 0, 0))
