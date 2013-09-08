import RPi.GPIO as gpio
from time import sleep


gpio.setmode(gpio.BOARD)

gpio.setup(11, gpio.OUT)

n = 0
while n < 3:
	gpio.output(11, True)
	sleep(2)
	gpio.output(11, False)
	sleep(2)
	n += 1

gpio.cleanup()
