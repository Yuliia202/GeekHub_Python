# Write a script that combines three dictionaries by updating the first one.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5, 'e': 6}

dict1.update(dict2)
dict1.update(dict3)

print(dict1)