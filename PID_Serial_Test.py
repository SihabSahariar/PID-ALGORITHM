# Developed By Sihab Sahariar


# Importing libraries
import time
import serial

# Defining variables 
encoder_pos = 0.0 # our encoder position from our range input
actual_pos  = 0.0 # our actual position taking into account en
desired_pos = 210 # desired position
error = 0.0 
previous_error = 0.0
total_error = 0.0 

#Gains for PID controller
kp = 1.0   # Proportional Gain
ki = 0.0   # Integral Gain
kd = 0.0   # Derivative Gain


try:
	serial = serial.Serial('/dev/tty0', 9600)
except:
	print ("Failed to connect")

def PID_Controller_Data():
	data = serial.readline()
	data = data.split(',')
	encoder_pos = data[0]
	error = data[1]
	lst = [encoder_pos,error]
	return lst 

if __name__ == '__main__':
	while(True):  
		# Call this function and scrap data from serial 
		data  = PID_Controller_Data()
		encoder_pos = data[0]
		error = data[1]
		
	    	# PID controller
	    	actual_pos = encoder_pos          # depending on tics/rev (70 pulse per rev)::do math
		previous_error = error            # This is for derivative calculations
		error = desired_pos - actual_pos  # This is the error between desired and real
		total_error += error              # This is for integral gain ki (sum of error over time)

		# Now the actual Controller
		# Multiply kp by proportional error, kd by derivative error and ki by error sum
		motor_voltage_input = (kp*error) + (kd*(error - previous_error)) + (ki*total_error);

		# Now that we have a proposed input (voltage), now send it back 
		print(motor_voltage_input);
		# Using a small delay to receive & send data with minimum errors
		time.sleep(1)

