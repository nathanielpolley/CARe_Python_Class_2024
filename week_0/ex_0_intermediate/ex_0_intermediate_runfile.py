#YOUR CODE FOR EX_0 INTERMEDIATE HERE

initial_count = float(input("Enter initial count: "))
final_count = float(input("Enter final count: "))
time = float(input("Enter time elapsed: "))

growth_rate = (final_count - initial_count) / time

if initial_count <= 0 or final_count <= 0 or time <= 0 :
    print ('invalid numbers')
else:
    print("Growth rate:", growth_rate)



