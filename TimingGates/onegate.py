import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sensor = 17                                                             #assigns the one gate to pin input
reset = 5                                                               #assigns the reset to a pin input

GPIO.setup(sensor, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)               #assigns the sensor start value to 0
GPIO.setup(reset, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)                #assigns the reset start value to 0


while True:                                                             #constantly loops the program
        gatetrigger1 = False                                            #assigns the first split counter to false
        gatetrigger2 = False                                            #assigns the second split counter to false
        gatetrigger3 = False                                            #assigns the third split counter to false
        gatetrigger4 = False                                            #assigns the fourth split counter to false
        counter = True                                                  #assigns the loop counter to true
        resetcounter = False                                            #assigns the reset counter to false
        counter1 = False                                                #assigns the split counter1
        counter2 = False                                                #assigns the split counter2
        counter3 = False                                                #assigns the split counter3

        while (counter == True):                                                        #while the counter is true it will check to see if the sensor is aligned
                if (GPIO.input(sensor) == True):                                        #if the sensor is aligned start checking for a break in the signal
                        counter = False
                        print ("the sensor is ready")
                        while (gatetrigger1 == False and resetcounter == False):        #if the gate hasnt been tripped yet and theres no reset check the sensor
                                if (GPIO.input(reset) == True):                         #if the reset is pressed return the program to check the gate alignment
                                        resetcounter = True                             #assigns the reset to true to get out of the while loop
                                        print ("gate reset")
                                        time.sleep(2)

                                if (GPIO.input(sensor) == False):                       #the sensor has been tripped
                                        start1 = time.time()                            #start the timer
                                        print ("timer started")
                                        time.sleep(2)                                   #pauses the program to account for interferance while the car is still getting off the start$
                                        gatetrigger1 = True                             #assigns the gatetrigger1 to true to get to the next while loop


                        while (gatetrigger1 == True and resetcounter == False):         #the sensor has been tripped once
                                if (GPIO.input(reset) == True):                         #if the reset is pressed return the program to check the gate alignment
                                        resetcounter = True                             #assigns the reset to true to get out of the while loop
                                        print ("gate reset")
                                        time.sleep(2)

                                if (GPIO.input(sensor) == False):                       #the sensor has been tripped again
                                        stop1 = time.time()                             #stops the timer after the sensor is tripped
                                        t1 = stop1 - start1                             #calculates the time of the first split
                                        start2 = time.time()                            #starts the second split timer
                                        print ("Split 1: %.3fs" % (t1))                 #prints the first split time
					time.sleep(2)
                                        counter1 = True                                 #sets the counter1 true for the next loop
                                        gatetrigger1 = False                            #sets the gatetrigger1 to false to get out of the while loop

                        while (gatetrigger2 == False and counter1 == True):             #the sensor has been tripped twice
                                if (GPIO.input(reset) == True):                         #if the reset is pressed return the program to check the gate alignment
                                        counter1 = False                                #assigns the counter1 to true to get out of the while loop
                                        print ("gate reset")
                                        time.sleep(2)

                                if (GPIO.input(sensor) == False):                       #the sensor has been tripped again
                                        stop2 = time.time()                             #stop the split two timer
                                        t2 = stop2 - start2 + t1                        #find the split two time and add it to split one for the total time
                                        start3 = time.time()                            #start the timer for the third split
                                        print ("Split 2: %.3fs" % (t2))                 #prints the second split
                                        file.write("Split 2: %.3fs\n" % (t2))           #write the second split to the text file
                                        time.sleep(2)
                                        counter2 = True                                 #assigns the counter2 to true for the next loop
                                        gatetrigger2 = True                             #assigns the gatetrigger2 to true to get out of the while loop

                        while (gatetrigger3 == False and counter2 == True):             #the sensor has been tripped three times
                                if (GPIO.input(reset) == True):                         #if the reset is pressed return the program to check the gate alignment
                                        counter2 = False                                #assigns the counter2 to false to get out of the while loop
                                        print ("gate reset")
                                        time.sleep(2)

                                if (GPIO.input(sensor) == False):                       #the sensor has been tripped again
                                        stop3 = time.time()                             #stop the split three timer
                                        t3 = stop3 - start3 + t2                        #find the split three time and add it to the split two for the total time
                                        start4 = time.time()                            #start the timer for the final time
                                        print ("Split 3: %.3fs" % (t3))                 #print the split three time
                                        file.write("Split 3: %.3fs\n" % (t3))           #write the split three time to the text file
                                        time.sleep(2)
                                        counter3 = True                                 #assigns the counter3 to true for the next loop
                                        gatetrigger3 = True                             #assigns gatetrigger3 to true to get out of the while loop

                        while (gatetrigger4 == False and counter3 == True):             #the sensor has been tripped four times
                                if (GPIO.input(reset) == True):                         #if the reset is pressed return the program to check the gate alignent
                                        counter3 = False                                #assigns the counter3 to false to get out of the while loop
                                        print ("gate reset")
                                        time.sleep(2)

                                if (GPIO.input(sensor) == False):                       #the sensor has been tripped the final time
                                        stop4 = time.time()                             #stop the final timer
                                        t4 = stop4 - start4 + t3                        #find the final split timer and add it to the split three for the total time
                                        print ("Final Time: %.3fs" % (t4))              #print the final time
                                        file.write("Final Time: %.3fs\n\n" % (t4))      #write the final time to the text file
                                        file.close                                      #close the file
                                        time.sleep(5)
                                        gatetrigger4 = True                             #assign the gatetrigger4 to true to get out of the while loop
   else:        	                                                                #if the sensor is not aligned let the user know
                        print ("check sensor alignment")
                        time.sleep(1)

GPIO.cleaup()

		
