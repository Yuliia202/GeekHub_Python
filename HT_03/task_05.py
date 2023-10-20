# Write a script to remove values duplicates from dictionary.
# Feel free to hardcode your dictionary.

my_dict = {'1': 7, '2': 11, '3': 47, '4': 3, '5': 17, '6': 17}

my_dict = {key: value for key, value in my_dict.items() if list(my_dict.values()).count(value) == 1}
print(f"Dictionary without values duplicates: {my_dict}")