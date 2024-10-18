#Initiation of list
growth_rate = []

#Initiation of a while loop taking input for 5 days and appending into the list created
n=0
while n < 5:
    try:
        x=int(input("Enter the microbial population count for the day:"))
        growth_rate.append(x)
        n = n+1
    except ValueError:
        print("Kindly enter the count in number only")

#Printing the average, maximum, minimum population from the list
print("\n")
print("The average microbial population count is", abs(sum(growth_rate)/len(growth_rate)))
print("The maximum microbial population count is",max(growth_rate))
print("The minimum microbial population count is",min(growth_rate))

print("\n") #Just a line to separate in the output

#Looping over the list to find days that have over 200 population count
for i in growth_rate:
    if i > 200:
        print("The microbial growth count is over 200 days on day", growth_rate.index(i)+1)