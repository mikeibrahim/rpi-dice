#!/usr/bin/env python
#
#  Author: Mike Ibrahim  
#  Date: 10/01/2016
#  Version: 1.0
#
#  Repository: https://github.com/mikeibrahim/rpi-dice
#
#  dice-binary.py
#
#  Game of Dice up to 7 using 3 LEDs in binary
#

# Import Libraries needed
import time
import RPi.GPIO as GPIO
import random

# Initialize settings for GPIO
GPIO.setwarnings(False)		# Disable warnings
GPIO.setmode(GPIO.BCM)		# Use the BCM layout for the pin numbering

# Pins being used and their order
#Pins=[4,5,6]
Pins=[6,5,4]  #reverse pins for binary (right to left)


# Set all the Pins for output mode
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)


# Function to turn on and off the LEDs for each pin from LED Pattern
# Parameter 1: OnOff - Array of Boolean Values in LED Pattern
def SwitchLights(OnOff):		
	for x in range(0,3):
		GPIO.output(Pins[x], OnOff[x])
		
	return 0
	
# Function to convert all the integer numbers to thier binary form
# Then send the binary form to the SwitchLights function
# Parameter 1: num - random integer from the main program
def LED(num):
	
	# First turn off all the lights 
	SwitchLights([False, False, False])

	# Check which number matches the parameter
	# For each number convert to binary
	if num==0:
		print "LED Zero: " + str(num)
		SwitchLights([False, False, False])
		

	if num==1:
		print "LED One: " + str(num)
		SwitchLights([False, False, True])
		
	if num==2:
		print "LED Two: " + str(num)
		SwitchLights([False, True, False])

	if num==3:
		print "LED Three: " + str(num)
		SwitchLights([False, True, True])
		
	if num==4:
		print "LED Four: " + str(num)
		SwitchLights([True, False, False])

	if num==5:
		print "LED Five: " + str(num)
		SwitchLights([True, False, True])
		
	if num==6:
		print "LED Six: " + str(num)
		SwitchLights([True, True, False])
		
	if num==7:
		print "LED Seven: " + str(num)
		SwitchLights([True, True, True])
		

	return 0
	

# Function main program
def main():
	# Initialize key=1 to do the first roll
	key=1
	
	# Keep rolling dice until key=0
	while key!=0:
		# Pass a random number between 0-7 to the LED function
		LED(random.randint(0, 7))
		
		# Ask the user to roll again
		key=input("Roll again? (0: no  1: yes) ")

	return 0

if __name__ == '__main__':
	main()

