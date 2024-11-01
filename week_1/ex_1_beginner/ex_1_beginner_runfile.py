population_counts = [100, 200, 150, 300, 50]
average = int(sum(population_counts) / len(population_counts))
max = max(population_counts)
min = min(population_counts)
print(f'Average population count: {average}\nMaximum population count: {max}\nMinimum population count: {min}')
for days, count in enumerate(population_counts, start=1):
    if count > 200:
        print(f'Days number when the population exceeds 200: {days}')