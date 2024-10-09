#YOUR CODE FOR EX_0 INTERMEDIATE HERE

import math
while True:
    try:
        initial_count = int(input("Please enter the initial count of the microbes: "))
        break
    except ValueError:
        print("Kindly enter a number only")

while True:
    try:
        final_count = int(input("Please enter the final count of the microbe: "))
        break
    except ValueError:
        print("Kindly enter a number only")

while True:
    try:
        time=int(input("Please enter the duration of growth in minutes: "))
        break
    except ValueError:
        print("Kindly enter a number only")

if final_count>initial_count:
    Growth_rate = (math.log(final_count)-math.log(initial_count))/time
    print("The growth rate is ", Growth_rate, "/min")
else:
    print("For growth rate, final count needs to be larger than initial")

