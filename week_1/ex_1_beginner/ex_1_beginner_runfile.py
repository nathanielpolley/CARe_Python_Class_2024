# Initialize an empty list to store population counts
population_counts = []

# Loop through each of the 5 days to collect population count
for day in range(1, 6):
    while True:
        try:
            # Prompt the user to enter the microbial population count for the current day
            count = int(input(f'Enter the microbial population count for day {day}: '))
            # Append the count to the list of population counts
            population_counts.append(count)
            # Exit the loop if the input is valid
            break
        except ValueError:
            # Display an error message if the input is not a valid integer
            print('Please enter a valid number')

# Calculate the average population count by dividing the sum by the number of days
average = int(sum(population_counts) / len(population_counts))
# Find the maximum population count from the list
max_count = max(population_counts)
# Find the minimum population count from the list
min_count = min(population_counts)

# Print the average, maximum, and minimum population counts
print(f'Average population count: {average}\nMaximum population count: {max_count}\nMinimum population count: {min_count}')

# Find all days where the population count exceeds 200 and store those day numbers in a list
days_exceeding_200 = [day for day, count in enumerate(population_counts, start=1) if count > 200]

# Check if there are any days with a population count exceeding 200
if days_exceeding_200:
    # If there are, print the days where the population exceeds 200
    print("Days when the population exceeds 200:", ', '.join(map(str, days_exceeding_200)))
else:
    # If no days exceed 200, print a message indicating that
    print("No days when the population exceeds 200.")