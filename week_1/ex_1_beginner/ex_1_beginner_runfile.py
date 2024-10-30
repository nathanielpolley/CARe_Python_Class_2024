#YOUR CODE FOR EX_1 BEGINNER HERE


population_counts = []

for i in range(5):
    count = int(input(f"Enter population count for day {i + 1}: "))
    population_counts.append(count)

average_population = sum(population_counts) / len(population_counts)
max_population = max(population_counts)
min_population = min(population_counts)

print("Average Population:", average_population)
print("Maximum Population:", max_population)
print("Minimum Population:", min_population)

x = 200
print(f"Days with population count exceeding {x}:")
for day, count in enumerate(population_counts, start=1):
    if count > x:
        print("The day corresponds to Day", day, "and the value is", count)
    else :
        print ("No population exceeding 200")
