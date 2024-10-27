#YOUR CODE FOR EX_0 INTERMEDIATE HERE

import math

initial_count = input("Enter initial count: ")
final_count = input("Enter final count: ")
time = input("Enter time elapsed: ")

if initial_count.isdigit() and final_count.isdigit() and time.isdigit():
    initial_count = int(initial_count)
    final_count = int(final_count)
    time = int(time)

    if (initial_count > 0) and (final_count > 0) and (time > 0) :
        if (final_count > initial_count) :
            x = math.log(final_count) - math.log(initial_count) / time
            print ("Growth rate:", x)
        else :
            print('Final count must be greater than initial count')
    else :
        print ('All values must be greater than 0')
else:
    print('Invalid input type(s). Please enter positive integer values')


