# Write a script to concatenate all elements in a list into a string and print it.
# List must be include both strings and integers and must be hardcoded.

values_list = [1, 2, 'u', 'a', 4, True]
values_string = "".join(map(str, values_list))
print('String of concatenated values: ', values_string)