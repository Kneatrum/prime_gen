def generate_prime(number):
    for sample in range(number): # Loop through from (0) to (number)
       
       if sample > 1: # check if the sample is more than (1)
           for x in range(2,sample): 
               if (sample % x) == 0: # if a (sample) number is divisible by any other number apart from 1 and itelf
                   break # break the loop
           else:
               print(sample)
generate_prime(10)