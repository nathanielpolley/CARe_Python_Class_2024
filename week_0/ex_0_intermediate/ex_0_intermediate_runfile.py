import math
def get_float_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value <= 0:
                print('Value must be greater than 0.')
            else:
                return value
        except:
            print('Invalid input. Please enter a valid value.')
while True:
    initial_count = get_float_input('Enter initial count: ')
    final_count = get_float_input('Enter final count: ')
    if initial_count < final_count:
        time = get_float_input('Enter the time elapsed (in hours): ')
        growth_rate = round(math.log(final_count / initial_count) / time, 3)
        print(f'The calculated growth rate: {growth_rate}')
        break
    else:
        print('Final count should be higher than initial count')