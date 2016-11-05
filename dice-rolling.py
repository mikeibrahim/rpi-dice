#!/usr/bin/env python

#  Author: Mike Ibrahim  
#  Date: 11/05/2016
#  Version: 1.0

#  Repository: https://github.com/mikeibrahim/rpi-dice

#  dice-rolling.py
  
#  This is a dice game up to 7 using 7 LEDs
#  with the raspberry pi and GPIO ports

 
# Import Libraries needed 
import time
import RPi.GPIO as GPIO
import random
import sys


# Initialize settings for GPIO
GPIO.setwarnings(False)	# Turn warnings off
GPIO.setmode(GPIO.BCM)	# Use BCM Diagram layout

# Pins being used and their order (reversed from on.py)
#Pins=[4,5,6,13,19,17,22]
Pins=[22,17,19,13,6,5,4]

# Array of LED patterns for each number
Lights=[
	[0,0,0,0,0,0,0],	# 0
	[0,0,0,0,0,0,1],	# 1
	[0,0,0,0,0,1,1],	# 2
	[0,0,0,0,1,1,1],	# 3
	[0,0,0,1,1,1,1],	# 4
	[0,0,1,1,1,1,1],	# 5
	[0,1,1,1,1,1,1],	# 6
	[1,1,1,1,1,1,1]]	# 7


# Array of text lables for each number
Labels=[
	"Number Zero",
	"Number One",
	"Number Two",
	"Number Three",
	"Number Four",
	"Number Five",
	"Number Six",
	"Number Seven"]

# Set all pins to output mode 
for x in range(0, len(Pins)):
	GPIO.setup(Pins[x], GPIO.OUT)

# Function to turn on and off the LEDs for each pin from LED Pattern
# Parameter 1: OnOff - Array of Boolean Values in LED Pattern
def SwitchLights(OnOff):
	for x in range(0,len(OnOff)):
		GPIO.output(Pins[x], OnOff[x])
		
	return 0
	
# Function that will display the paramater number on the LEDs
# Parameter 1: num - random integer from the main program
def LED(num):
	SwitchLights(Lights[0])				# Turn off all LEDs	
	print Labels[num] + ": " + str(num)	# Print number to the screen
	SwitchLights(Lights[num])			# Turn on LEDs for the number

	return 0

# Function to display a fancy rolling event	
def Rolling():
	
	# Using sys library to print without buffering
	# flush() will write to the screen immediately
	sys.stdout.write("Rolling...")
	sys.stdout.flush()

	# Loop 3 times around
	for z in range (0,3):
		# Blink each GPIO on and off
		for x in range(0, len(Pins)):
			GPIO.output(Pins[x], True)
			sys.stdout.write(".")		# Put a dot for each blink
			sys.stdout.flush()
			time.sleep(.05)
			GPIO.output(Pins[x], False)
			
	sys.stdout.write("\n")				# Put new line after dots
	sys.stdout.flush()
	
	return 0
	
def main():
	# Set keys for rolling again
	y=1
	n=0
	key=y

	# Loop until n key is pressed
	while key != n:
		Rolling()
		LED(random.randint(0, len(Pins)))
		key=input("Roll again? (n=no, y=yes) ")

	# Switch off the all LEDs
	LED(0)
	return 0

if __name__ == '__main__':
	main()

