#YOUR CODE FOR EX_0 INTERMEDIATE HERE
# Input from the user
import math

time = input("Enter time in hours: ")

# Conditional statement for ensuring time is a valid number
if time.isdigit():
    itime = int(time)
if not time.isdigit():
    print("Error: text not accepted, only numbers")
elif int(time) <= 0:
    print("invalid time (should be more than 0h)")
else:
    initial_count = input("Enter initial count: ")

# Conditional statement to ensure initial count is valid
if initial_count.isdigit():
    icount = int(initial_count)
if not initial_count.isdigit():
    print("Error: text not accepted, only numbers")
elif int(initial_count) <= 0:
    print("invalid initial count (should be more than 0)")
else:
    final_count = input("Enter final count: ")

# Conditional statement to ensure final count is valid and perform the calculus
if final_count.isdigit():
    fcount = int(final_count)
if not final_count.isdigit():
    print("Error: text not accepted, only numbers")
elif int(final_count) < int(initial_count):
    print("invalid final count (should be greater than initial count)")
else:
    calculus = (math.log(fcount) - math.log(icount)) / itime
    print(f"Growth rate per hour is: {calculus}")