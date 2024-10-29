population_counts = [100, 200, 150, 300, 50]
average_population = sum(population_counts) / len(population_counts)
max_population = max(population_counts)
min_population = min(population_counts)

print(f" average population count: {average_population:.2f}")
print(f" maximum population count: {max_population}")
print(f" minimum population count: {min_population}")

exceeding_days = []
for day in range(len(population_counts)):
    if population_counts[day] > 200:
        exceeding_days.append(day + 1)

if exceeding_days:
    print(f"population exceeded 200 on days: {','.join(map(str, exceeding_days))}")
else:
    print("population never exceeded 200 on any day.")
