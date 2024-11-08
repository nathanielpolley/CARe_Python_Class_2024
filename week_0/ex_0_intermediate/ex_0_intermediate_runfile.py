import math

def calculate_growth_rate():
    try:
        # Prompt the user to input the initial count, final count, and time
        initial_count = float(input("Enter the initial cell count: "))
        final_count = float(input("Enter the final cell count: "))
        time = float(input("Enter the time elapsed (in hours): "))

        # Validate inputs
        if initial_count <= 0 or final_count <= 0:
            print("Cell counts must be positive numbers.")
            return
        if time <= 0:
            print("Time must be a positive number.")
            return

        # Calculate the growth rate using the formula
        growth_rate = (math.log(final_count) - math.log(initial_count)) / time

        # Display the growth rate
        print(f"The growth rate of the microbial culture is: {growth_rate:.4f} per hour")

    except ValueError:
        print("Invalid input. Please enter numerical values for cell counts and time.")

# Call the function to run the program
calculate_growth_rate()