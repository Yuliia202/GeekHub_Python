# Write a script that will run through a list of tuples and replace the last
# value for each tuple. The list of tuples can be hardcoded. The "replacement"
# value is entered by user. The number of elements in the tuples must be different.

tuple_list = [(1, 7, True), ("abc", 7), (0,), ()]
replacing_values = input(f"Input value for replacing: ")
for i in range(len(tuple_list)):
    if len(tuple_list[i]) > 0:
        tuple_list[i] = tuple_list[i][:len(tuple_list[i]) - 1] + (replacing_values, )
print(f'List with replaced elements: {tuple_list}')