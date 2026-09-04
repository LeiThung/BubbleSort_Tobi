from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms
from random import randrange

pixels_count = 32
pixels = NeoPixel(Pin(15), pixels_count)
pixels_count_half = int(pixels_count/2)

a = [[randrange(256) for c in range(3)] for i in range(pixels_count)]

while True:
    ## Set a color for each of the RGB-LEDs
    for i in range(pixels_count - 1):
        if (a[i][0] > a[i + 1][0]):
            a[i], a[i + 1] = a[i + 1], a[i]

    for i in range(pixels_count):
        pixels[i] = a[i]
    pixels.write()
    sleep_ms(50)