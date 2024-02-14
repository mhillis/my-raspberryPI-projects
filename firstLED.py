import RPi.GPIO as GPIO #Import Raspberry Pi GPIO library

from time import sleep # import the sleep function from the time module

GPIO.setwarnings(False) #ignores warning for now

GPIO.setmode(GPIO.BOARD) # use physical pin numbering
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # set pin 7 to be an output pin and set intitial value to low (off)

while True: # Run foreever
	GPIO.output(7, GPIO.HIGH) #turn on
	sleep(1) # sleep for 1 second
	GPIO.output(7, GPIO.LOW) # turn off
	sleep(1)
