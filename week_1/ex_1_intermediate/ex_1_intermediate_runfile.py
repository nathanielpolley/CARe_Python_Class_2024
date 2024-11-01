species_dict = {}
while True:
    species_name = input('Enter species name (or type "exit" to quit): ')
    if species_name.lower() == 'exit':
        break
    try:
        num_samples = int(input(f'Enter number of samples for {species_name}: '))
    except ValueError:
        print("Invalid input. Please enter a valid number for samples.")
        continue
    species_dict[species_name] = num_samples
total_samples = 0
for species, samples in species_dict.items():
    total_samples += samples
print(f'Number of total samples: {total_samples}')
species_15 = []
for species, samples in species_dict.items():
    if samples > 15:
        species_15.append(species)
if species_15:
    print(f'Microbial species with sample counts greater than 15: {', '.join(species_15)}')
else:
    print('No microbial species have sample counts greater than 15.')
def add_new_species(new_species, species_dict):
    if new_species in species_dict:
        species_dict[new_species] += 1
    else:
        species_dict[new_species] = 1
while True:
    new_species = input('Enter a new species name (or type "exit" to quit): ')
    add_new_species(new_species, species_dict)
    if new_species.lower() == 'exit':
        break
species_string = ', '.join(f'{key}: {value}' for key, value in species_dict.items())
print(f'Updated species count: {species_string}')