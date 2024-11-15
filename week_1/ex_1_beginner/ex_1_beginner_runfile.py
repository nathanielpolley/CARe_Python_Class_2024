#YOUR CODE FOR EX_1 BEGINNER HERE
microbial_population_counts=[100, 200, 150, 300, 50]
from statistics import mean

def average_population(microbial_population_counts):
    return mean(microbial_population_counts)
avg_population = average_population(microbial_population_counts)
print(f"The average population is: {avg_population}")

max_count = min_count = microbial_population_counts[0]

for count in microbial_population_counts:
    if count > max_count:
        max_count = count
    if count < min_count:
        min_count = count

print(f"Maximum population count: {max_count}")
print(f"Minimum population count: {min_count}")


for day, count in enumerate(microbial_population_counts, start=1):
    if count > 200:
        print(f"Day {day}: {count}")
