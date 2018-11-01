import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

switch = 13                                                   #assigns the switch to a pin input

GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)     #assigns the start value of the switch to 0


if (GPIO.input(switch) == True):                              #if the switch is high start the two gate program
        import tigerracing

else:                                                         #if the switch is low start the one gate program
        import onegate


GPIO.cleanup()

