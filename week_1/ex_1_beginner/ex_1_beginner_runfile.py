#YOUR CODE FOR EX_1 BEGINNER HERE
#User input the data for each day
d1=int(input("Enter microbial population count for day 1: "))
d2=int(input("Enter microbial population count for day 2: "))
d3=int(input("Enter microbial population count for day 3: "))
d4=int(input("Enter microbial population count for day 4: "))
d5=int(input("Enter microbial population count for day 5: "))

#Create a tuple with the values for each day
counts=(d1, d2, d3, d4, d5)

#First, calculate average by creating a loop that sums all the values from the tuple. Then, divided by its length to obtain the average and print it
sum_result=0
for suma in counts:
    sum_result += suma
average=sum_result/len(counts)
print("Average population count:",average)

#Find max with loop in which we compare each value of the tuple with the next one. If its higher than the original, is substituted and compared again to the next. This way the maximum number will be the final output
def find_max(counts):
    if not counts:
        return None
    max_num = counts[0]
    for num in counts:
        if num > max_num:
            max_num = num
    return max_num

maximum=find_max(counts)
print("Maximum population count:", maximum)

#Same for find min but changing symbol to minor to
def find_max(counts):
    if not counts:
        return None
    max_num = counts[0]
    for num in counts:
        if num < max_num:
            max_num = num
    return max_num

minimun=find_max(counts)
print("Minimum population count:", minimun)

#Find >200: define a function in which for the range of the length of the tuple, will find if its larger than 200. If not, it will continue to the next value. If it is >200, we detect the index of the corresponding day and sum 1 to the output (since day 1 is going to be index 0)
def more_200(counts):
    for i in range(len(counts)):
        overcount = counts[i]
        if overcount < 200:
            continue
        elif overcount > 200:
            day=counts.index(overcount)
            print(f"Day {day+1} excedes 200 counts")
            continue

#Apply the function to the tuple
x=more_200(counts)
print(x)