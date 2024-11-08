#YOUR CODE FOR EX_1 BEGINNER HERE
population_counts = [100, 200, 150, 300, 50]
maximum = population_counts[0]
minimum = population_counts[0]
average = 0
days = []
for i in population_counts:
    average = average + i
    if i >= maximum:
        maximum = i
    if i <= minimum:
        minimum = i
    if i > 200:
        print(f"The day when the populations exceed 200 : {population_counts.index(i)}")

average = average/len(population_counts)
print(f'The average is : {average}')
print(f'The maximum is : {maximum}')
print(f'The minimum is : {minimum}')