# Write a script which accepts two sequences of comma-separated colors from user.
# Then print out a set containing all the colors from color_list_1 which are not
# present in color_list_2.

color_list_1 = input('Please write colors:').split(',')
color_list_2 = input('Please write colors:').split(',')

print(set(color_list_1) - set(color_list_2))