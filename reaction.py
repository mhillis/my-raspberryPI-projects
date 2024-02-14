import RPi.GPIO as GPIO #import raspberry pi GPIO library
import time #import time module
import random #import random module
from datetime import datetime #import the datetime function from the  datetime module

GPIO.setwarnings(False) # ignores warning for now

GPIO.setmode(GPIO.BOARD) #use physical pin numbering
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # set pin 7 to be an output pin and set the initial value to LOW(off)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set pin to 16 to be the input(in thise case push button) set initially value to off
random.seed()

while True:
	time.sleep(random.random()*10) #random sleep time from 1-10 seconds(i think)
	start = datetime.now() # timer begins
	GPIO.output(7,GPIO.HIGH) #turn led on
	while not GPIO.input(16):
		pass
	print("Your reaction time: ",
		(datetime.now() - start).total_seconds())
	print("Get ready to try again.")
	GPIO.output(7, GPIO.LOW)
