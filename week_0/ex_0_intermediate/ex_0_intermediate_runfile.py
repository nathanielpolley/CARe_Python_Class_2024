#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math
user_input_initial_count = input("Enter the initial cell count: ")
user_input_final_count= input("Enter the final cell count:")
user_input_time = input("Enter the time elapsed (in hours): ")
if user_input_initial_count.isdigit() and user_input_final_count.isdigit() and user_input_time.isdigit():
    initial_count = int(user_input_initial_count)
    final_count = int(user_input_final_count)
    time_elapsed = int(user_input_time)
    if final_count>initial_count:
         growth_rate = (math.log(int(final_count)) - math.log(int(initial_count))) / int(time_elapsed)
         print(f"growth_rate: {growth_rate} per hour")
    else:
        print('Error in the experiment')
else:
  print('ERROR')

