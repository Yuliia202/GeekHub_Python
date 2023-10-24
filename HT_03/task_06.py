# Write a script to get the maximum and minimum value in a dictionary.

my_dict = {'1': 7, '2': 11, '3': 47, '4': 3, '5': 17}
number_values = [value for value in my_dict.values() if isinstance(value, (int, float))]
max_value = max(my_dict.values())
min_value = min(my_dict.values())
print(f"Max value: {max_value}")
print(f"Min value: {min_value}")