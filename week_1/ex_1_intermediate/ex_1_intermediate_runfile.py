# Initialize an empty dictionary to store species and their sample counts
species_dict = {}

# Loop to allow the user to enter species names and their sample counts
while True:
    # Prompt the user to enter a species name or type 'exit' to quit
    species_name = input('Enter species name (or type "exit" to quit): ')

    # If the user types 'exit', break out of the loop
    if species_name.lower() == 'exit':
        break

    # Prompt the user to enter the number of samples for the species
    try:
        num_samples = int(input(f'Enter number of samples for {species_name}: '))
    except ValueError:
        # If the input is not a valid integer, show an error message and continue the loop
        print("Invalid input. Please enter a valid number for samples.")
        continue

    # Store the species name and the number of samples in the dictionary
    species_dict[species_name] = num_samples

# Initialize a variable to calculate the total number of samples
total_samples = 0
# Loop through the dictionary to sum up all the sample counts
for species, samples in species_dict.items():
    total_samples += samples

# Print the total number of samples collected
print(f'Number of total samples: {total_samples}')

# Initialize a list to store species with sample counts greater than 15
species_15 = []
# Loop through the dictionary to find species with more than 15 samples
for species, samples in species_dict.items():
    if samples > 15:
        species_15.append(species)

# Print the species that have sample counts greater than 15, if any
if species_15:
    print(f'Microbial species with sample counts greater than 15: {", ".join(species_15)}')
else:
    print('No microbial species have sample counts greater than 15.')


# Define a function to add a new species or increment its sample count
def add_new_species(new_species, species_dict):
    # If the species already exists in the dictionary, increment the sample count
    if new_species in species_dict:
        species_dict[new_species] += 1
    # Otherwise, add the species with a sample count of 1
    else:
        species_dict[new_species] = 1


# Loop to allow the user to add new species names or exit
while True:
    # Prompt the user to enter a new species name or type 'exit' to quit
    new_species = input('Enter a new species name (or type "exit" to quit): ')

    # If the user types 'exit', break out of the loop
    if new_species.lower() == 'exit':
        break

    # Call the function to add the new species or update its sample count
    add_new_species(new_species, species_dict)

# Create a string that lists all species and their sample counts
species_string = ', '.join(f'{key}: {value}' for key, value in species_dict.items())

# Print the updated species count
print(f'Updated species count: {species_string}')