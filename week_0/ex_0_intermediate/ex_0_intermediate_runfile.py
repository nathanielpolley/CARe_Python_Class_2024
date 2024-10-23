#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math
user_input_initial_count = input("Enter the initial cell count: ")
if user_input_initial_count.isdigit():
    cell_count=int(user_input_initial_count)
    print(f"Entered number1:{cell_count}")
user_input_final_count= (input("Enter the final cell count:"))
if user_input_final_count.isdigit():
    cell_count2=int(user_input_final_count)
    print(f"Entered Number2:{cell_count2}")
user_input_time = (input("Enter the time elapsed (in hours): "))
if user_input_time.isdigit():
    number=int(user_input_time)
    print(f"Entered Number3:{number}")

if cell_count2 > cell_count:
   growth_rate = (math.log(cell_count2) - math.log(cell_count)) / number
   print(f"growth_rate: {growth_rate}")
else:
      print('Repeat the experiment')
