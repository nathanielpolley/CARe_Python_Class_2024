microbial_samples = {
    "Bacteria": 20,
    "Archaea": 15,
    "Fungi": 10 }

total_samples = sum( microbial_samples.values())
print(f" Total number of samples / {total_samples}")

species_above_15 =[ species for species, count in microbial_samples.items() if count > 15]
print(f"species with more than 15 samples: {species_above_15}")

def add_species( species_dict, new_species):
    """
    Add a new species to the dictionary.
    If the new species exists increement its count by 1
    If not, add it with an initial count of 1
    """

    if new_species in species_dict:
        species_dict[new_species] += 1
    else:
        species_dict[new_species] = 1

while True:
    new_species = input(" Enter a new microbial species to add or type stop to finish:")
    if new_species.lower() == 'stop':
        break
    add_species(microbial_samples, new_species)
print("Updated microbial species dictionary:")
for species, count in microbial_samples.items():
    print(f"{species}: {count}")

#