
Sample_Species = {} #empty dictionary
#first function that updates the dictionary with existing sampled species data
def sampledspecies(keys, values):
    Sample_Species[keys] = values

#iterate over to collect the initial data from the user
number_of_species = int(input("Enter the total number of species in digits:"))
i = 0
while i < number_of_species:
    key_input = str(input("Enter the name of the species:").upper())
    value_input = int(input("Enter the number of samples sampled in numbers:"))
    sampledspecies(key_input, value_input)
    i+= 1

#function to add new inputs from user
def new_samples(species):
    if species in Sample_Species:
        Sample_Species[species] = Sample_Species[species]+1
    else:
        Sample_Species[species] = 1

#this block of code ensures the program runs as long as the user types enter
while str(input("Type 'Enter' to continue: ").upper()) =='ENTER':
    entry = str(input("Enter the species name: ").upper())
    new_samples(entry)

#list to append species with more than 15 samples
surplus_num_species=[]
for key in Sample_Species:
    if Sample_Species[key] >= 15:
        surplus_num_species.append(key)

print("Total number of samples across all species is:", sum(Sample_Species.values()))
print("\n")
print("Species with more than 15 samples are: ",','.join(surplus_num_species))
print("\n")
print(Sample_Species)


