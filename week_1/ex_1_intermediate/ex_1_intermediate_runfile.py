microbial_species={"Bacteria":20,"Archaea":15,"Fungi":10}
total_samples=0
for species,count in microbial_species.items():
     total_samples+=count
     print(f"Added {count} samples from {species}")
print(f"Total number of samples collected:{total_samples}")

microbial_species["Virus"] = 1
microbial_species["algea"]=1
print(microbial_species)
while True:
    new_species=input("Enter a new species name(or quit to stop):")
    if new_species.lower()=='quit':
        break
    if new_species in microbial_species:
        print(f"{new_species} already exist in the dictionary.")
        continue
    while True:
        try:
            sample_count=int(input(f"Enter the sample count for {new_species}:"))
            if sample_count< 0:
                print("Please enter a non-negative number.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
    microbial_species[new_species]=sample_count
    print(f"Added {new_species} with {sample_count} samples.")

print("Microbial species in the end")
for species,count in microbial_species.items():
    print(f"{species}:{count}")
#YOUR CODE FOR EX_1 INTERMEDIATE HERE
