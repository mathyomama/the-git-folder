import RPi.GPIO as gpio
from time import sleep


gpio.setmode(gpio.board)

gpio.setup(11, gpio.OUT)

while True:
	gpio.output(11, True)
	sleep(2)
	gpio.output(11, False)
	sleep(2)


