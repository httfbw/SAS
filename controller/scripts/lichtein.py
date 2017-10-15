# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 74      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


def colorWipe(strip, color, wait_ms=50):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)
	for j in range(strip.numPixels()):
		strip.setPixelColor(j, Color(0, 0, 0))
		strip.show()
		time.sleep(wait_ms/1000.0)

def blinken(strip, color):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
	strip.show()
	time.sleep(0.5)
	for j in range(strip.numPixels()):
		strip.setPixelColor(j, Color(0, 0, 0))
	strip.show()
	time.sleep(0.5)

def brightness(strip, i):
	for j in range(strip.numPixels()):
		strip.setPixelColor(j, Color(i, i, i))

def setAll(strip):
	for i in range(0, 255):
		brightness(strip, i)
		time.sleep(0.01)
		strip.show()
	for l in range(255, 0, -1):
		brightness(strip, l)
		time.sleep(0.01)
		strip.show()


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	x=0
	while x<10:
		setAll(strip)
		x+1
