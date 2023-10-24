# Write a script to remove values duplicates from dictionary.
# Feel free to hardcode your dictionary.

my_dict = {'1': 7, '2': 11, '3': 47, '4': 3, '5': 17, '6': 17}

print(f'Original dictionary: {my_dict}')
unique_dict = {}
for key, value in my_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value
print(f"Dictionary without duplicated values: {unique_dict}")