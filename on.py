#!/usr/bin/env python
#
#  Author: Mike Ibrahim  
#  Twitter: @stuff4rpi
#
#  Repository: https://github.com/mikeibrahim/rpi-dice
# 
#  on.py
#  
#  This is to test all the lights one by one 
#  to make sure they all work
#
 
# Import Libraries needed
import time
import RPi.GPIO as GPIO


# Initialize settings for GPIO
GPIO.setwarnings(False)	# Turn warnings off
GPIO.setmode(GPIO.BCM)	# Use BCM Diagram layout


# Pins being used and their order
Pins=[4,5,6,13,19,17,22]

# Loop though all of the pins
for x in range(0, len(Pins)):
	GPIO.setup(Pins[x], GPIO.OUT) # Set pin to output mode 
	GPIO.output(Pins[x], True)    # Turn on the pin
	time.sleep(.2)                # Pause so you can see a blink
	print "GPIO %d: %d" % (Pins[x], GPIO.input(Pins[x]))
	GPIO.output(Pins[x], False)   # Turn off the pin 
