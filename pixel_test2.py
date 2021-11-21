import board
#print(dir(board))
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 100, brightness=1)

# pixels.fill((255, 255, 255))
pixels[99] = (255, 255, 255)
#pixels.show()

time.sleep(10)
pixels.fill((0, 0, 0))
