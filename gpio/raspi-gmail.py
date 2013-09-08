#!/usr/bin/env python


import RPi.GPIO as GPIO, feedparser, time, getpass


def mailparser(username, password, label=''):
	return feedparser.parse("https://%s:%s@mail.google.com/gmail/feed/atom/%s" % (username, password, label))


def led_blink(led, interval=1, length=60):
	count = 0
	while count < length/float(2*interval):
		GPIO.output(led, True)
		time.sleep(interval)
		GPIO.output(led, False)
		time.sleep(interval)
	GPIO.cleanup()


DEBUG = 1

GPIO.setwarnings(False)

USERNAME = raw_input('Gmail Username: ')
PASSWORD = getpass.getpass()

MAIL_CHECK_FREQ = 60

GPIO.setmode(GPIO.BOARD)
GREEN_LED = 11
RED_LED = 13
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)


number_of_labels = int(raw_input("How many labels would you like to monitor?\n: "))
labels = dict()
print "Please list the labels if you said a number greater than 0. Otherwise your notifications will resume."
for index in range(number_of_labels):
	label = raw_input("%d: " % (index + 1))
	labels[label] = int(mailparser(USERNAME, PASSWORD, label)['feed']['fullcount'])

try:
	while True:
		mailtime = False
		for label, newmail_offset in labels.iteritems():
			mail = mailparser(USERNAME, PASSWORD, label)
			newmail_count = int(mail['feed']['fullcount']) - newmail_offset
			print "You have %d new email(s) labeled as %s." % (newmail_count, label)
			if newmail_count > 0:
				mailtime = True

		if mailtime:
			led_blink(GREEN_LED)
		else:
			time.sleep(MAIL_CHECK_FREQ)
except KeyboardInterrupt:
	GPIO.cleanup()
