import math


def calculate_growth_rate(initial_count, final_count, time):
    if initial_count <= 0 or final_count <= 0 or time <= 0:
        raise ValueError("Counts and time must be greater than zero.")

    growth_rate = (math.log(final_count) - math.log(initial_count)) / time
    return growth_rate


def main():
    try:
        initial_count = float(input("Enter the initial cell count: "))
        final_count = float(input("Enter the final cell count: "))
        time = float(input("Enter the time elapsed (in appropriate units): "))

        growth_rate = calculate_growth_rate(initial_count, final_count, time)
        print(f"The growth rate of the microbial culture is: {growth_rate:.4f} per unit time")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
