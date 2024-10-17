#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math
initial_count = float(input("Enter the initial cell count: "))
final_count= float(input("Enter the final cell count:"))
time = float(input("Enter the time elapsed (in hours): "))
growth_rate = (math.log(final_count) - math.log(initial_count)) / time
print(f"growth_rate: {growth_rate}")
