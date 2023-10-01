#Import necessary libraries

import time  # Use the time library to import sleep and time functions.
import RPi.GPIO as GPIO     # Import the RPi.GPIO library for GPIO control.

# Set the GPIO mode to use BCM pin numbering.
GPIO.setmode(GPIO.BCM)  


# Define the GPIO pin numbers for the ultrasonic sensor-trig pin and echo pin, and the LED.
LED_pin = 12
trig_pin=4
echo_pin=17


# Set up the GPIO pins as either input or output.
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(LED_pin, GPIO.OUT)


# Function to calculate distance using the ultrasonic sensor.
def calc_distance():

    # Produce a short pulse on the trigger pin.
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)


# Measure the time echo pin takes from low to high and back to low.
    while GPIO.input(echo_pin) == 0:
        pulse_start_time = time.time()
    while GPIO.input(echo_pin) == 1:
        pulse_end_time = time.time()


# Determine the pulse duration and convert it into centimetres.
    total_pulse_duration = pulse_end_time - pulse_start_time
    distance= total_pulse_duration * 34300 / 2      #Speed of sound in cm/s
    
    return distance


#Main code
try:
    while True:
        dist_cm = calc_distance()       #Call the calc_distance function to get the distance in cms.
        
        if dist_cm < 10:                 # Check if the distance is less than 10 cm (object is in range).
          
            GPIO.output(LED_pin, GPIO.HIGH)      #LED will be on.
            print("Object is in range")
        else:            # Else the distance is more than 10 cm (object is out of range).
            
            GPIO.output(LED_pin, GPIO.LOW)       #LED will be off.
            print("Object is out of range")
        
        time.sleep(0.15)   # Sleep for 0.15 second before taking the next distance.


# Handle a keyboard interrupt to clear the GPIO pins (Ctrl+C).
except KeyboardInterrupt:
    GPIO.cleanup()
