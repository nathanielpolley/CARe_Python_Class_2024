#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math
user_input_initial_count = input("Enter the initial cell count: ")
user_input_final_count= input("Enter the final cell count:")
user_input_time = input("Enter the time elapsed (in hours): ")
if user_input_initial_count and user_input_final_count and user_input_time.isdigit():
    cell_count=int(user_input_initial_count and user_input_final_count and user_input_time)
    print(f"initial_cell:{user_input_initial_count},final_cell:{user_input_final_count}, elapsed_time:{user_input_time}")

if int(user_input_final_count) > int(user_input_initial_count) :
   growth_rate = (math.log(int(user_input_final_count)) - math.log(int(user_input_initial_count))) / int(user_input_time)
   print(f"growth_rate: {growth_rate}")
else:
      print('Repeat the experiment')
