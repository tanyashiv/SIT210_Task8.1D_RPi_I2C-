# Import necessary libraries
import smbus
import time

# Define I2C device address and resolution mode
comp_Address =  0x23
res_mode = 0x20

# Initialize the I2C bus
bus = smbus.SMBus(1)

# Function to read light intensity value
def light_val():
     # Read a block of data from the I2C device
    l = bus.read_i2c_block_data(comp_Address, res_mode)
    return Convert_data(l) # Convert the data to a light intensity value

# Function to convert data to light intensity value
def Convert_data(data):
    return ((data[1] + (256 * data[0]))/ 1.2)  # Combine two bytes of data to get the light intensity value

# Continuous loop for reading and processing light intensity
while True:
     Intensity = light_val()  # Get the current light intensity value
     time.sleep(1)   # Pause for 1 second
     
     # Determine the intensity level and print the corresponding message
     if(Intensity > 2600):
         print("Intensity of light: Too Bright")
     elif(Intensity > 1600 and Intensity < 2600):
         print("Intensity of light: Bright")
     elif(Intensity > 1100 and Intensity < 1600):
         print("Intensity of light: Medium")
     elif(Intensity > 600 and Intensity < 1100):
         print("Intensity of light: Dark")
     elif(Intensity < 600):
         print("Intensity of light: Too Dark")
