
def generate_prime(number):
	if isinstance(number,int):
		if number > 2:
		    for sample in range(number): # Loop through from (0) to (number)
		       
		       if sample > 1: # check if the sample is more than (1)
		           for x in range(2,sample): 
		               if (sample % x) == 0: # if a (sample) number is divisible by any other number apart from 1 and itelf
		                   break # break the loop
		           else:
		               print(sample) # Print the prime number
		else:
			print ("Insert a number greater than 1") # Display an error when a number less than 2 is passed in.
	else:
		print ("Please insert a number") # Display an error when a character is passed in as an argument.

generate_prime(1)