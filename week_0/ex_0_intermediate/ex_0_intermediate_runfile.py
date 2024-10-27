#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math
initial_count = int(input("Enter your initial count: "))
final_count = int(input("Enter your final count: "))
time = int(input("Enter your time: "))
if time <= 0:
    time = int(input("Time invalid, enter a new time bigger than 0: "))

print((math.log(final_count) - math.log(initial_count)) / time)