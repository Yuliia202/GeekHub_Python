# Write a script which accepts a <number> from user and generates dictionary
# in range <number> where key is <number> and value is <number>*<number>
# e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}

inputted_values = int(input(f"Please input limit value: "))
dict_1 = {val: val ** 2 for val in range(inputted_values + 1)}
print(f"Dictionary in range {inputted_values}: {dict_1}")
