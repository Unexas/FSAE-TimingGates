import WebServer
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

start_pin = 17
stop_pin = 22
reset_pin = 5

GPIO.setup(start_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(stop_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(reset_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

counter = True

while True:
	while (counter == True):
		if(GPIO.input(start_pin) == True):
			print ("first gate sensor ready")
			time.sleep(1)
		else:
			print: ("check first gate alignment")
			time.sleep(1)
		if(GPIO.input(stop_pin) == True):
			print ("first gate sensor ready")
			time.sleep(1)
		else:
			print: ("check first gate alignment")
			time.sleep(1)
		if(GPIO.input(start_pin) == True and GPIO.input(stop_pin) == True):
			counter = False
			print("both gates are set, trial ready to begin")

			if(GPIO.input(reset_pin) == True):
				counter = True
				print("gates have been reset")
				time.sleep(1)
			gate1trigger = False
			gate2trigger = False
			while(gate1trigger == False and gate2trigger == False):
				if(GPIO.input(start_pin) == False):
					start = time.time()
					print ("first gate triggered")
					gate1trigger = True

					if(GPIO.input(reset_pin == True)):
						counter = True
						print("gates have been reset")
						time.sleep(1)
			while(gate1trigger == True and gate2trigger == False):
				if(GPIO.input(stop_pin) == False):
					stop = time.time()
					print ("second gate triggered")
					t = stop - start
					print ("Time: %.3fs" % (t))
					time.sleep(15)
					gate2trigger = True
					counter = True