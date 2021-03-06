# Zip Code generator
# Takes 2 strings: "79-900" and "80-155" and returns a list of codes between them.

def postal_codes(str1, str2):
    var1 = str1.split('-')
    var2 = str2.split('-')
    start1 = int(var1[0])  # 79
    meta1 = int(var1[1])  # 900
    start2 = int(var2[0])  # 80
    meta2 = int(var2[1])  # 155

    for x in range(start1, start2 + 1):
        for y in range(1000):
            if (x == start1 and y < meta1) or (x == start2 and y > meta2):
                continue
            else:
                print(f'{x}-{y:03}')  # print('{}-{:03d}'.format(x, y))


postal_codes('79-900', '80-155')


# The list contains elements with values 1-n.
# Write a function that checks which elements are missing.

def find_missing_numbers(input_num, max_num):
    list_of_numbers = set()
    for x in range(1, max_num+1):
        list_of_numbers.add(x)

    missing = list_of_numbers.difference(input_num)
    print(f'All elements: {list(list_of_numbers)}')
    print(f'Input list: {input_num}')
    print(f'Missing numbers: {list(missing)}')


input_list = [2, 8, 6, 1, 11, 19, 15]   # You can also use input function to enter values by terminal.
find_missing_numbers(input_list, 20)


# Generate a list of numbers from 2 to 5.5 with increments of 0.5.
# The resulting data must be of Decimal type.

from decimal import Decimal as dm


def generate_numbers(start=dm(2), stop=dm(5.5), step=dm(0.5)):
    list_of_numbers = [start]
    while list_of_numbers[-1] < stop:
        start += step
        list_of_numbers.append(start)
    print(list_of_numbers)
    # print(type(list_of_numbers[0]))


generate_numbers()


