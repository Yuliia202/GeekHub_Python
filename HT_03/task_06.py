# Write a script to get the maximum and minimum value in a dictionary.

my_dict = {1: 7, 2: 11, 3: 47, 4: 3, 5: 17,
           6: "bdv", 7: "fdfbf", 8: "z",
           11: [5], 13: [7, 8, 0],
           9: ["bfb", "gdd", "kd"], 14: ["f"],
           12: {9, 8, 7, 6, 5, 4}, 16: {0, 2},
           17: {"dfh", "ryn"}, 18: {"a", "dfkbgjektgnke"},
           10: (2, 8, 5, 9), 15: (7,),
           19: ("fdvsb",), 20: ("uu", "atefwevw")}
number_values = [value for value in my_dict.values() if isinstance(value, (int, float))]
string_values = [value for value in my_dict.values() if isinstance(value, str)]
list_number_values = [value for value in my_dict.values() if isinstance(value, list)
                      and all(isinstance(sub_item, (int, float)) for sub_item in value)]
list_string_values = [value for value in my_dict.values() if isinstance(value, list)
                      and all(isinstance(sub_item, str) for sub_item in value)]
set_number_values = [value for value in my_dict.values() if isinstance(value, set)
                      and all(isinstance(sub_item, (int, float)) for sub_item in value)]
set_string_values = [value for value in my_dict.values() if isinstance(value, set)
                      and all(isinstance(sub_item, str) for sub_item in value)]
tuple_number_values = [value for value in my_dict.values() if isinstance(value, tuple)
                      and all(isinstance(sub_item, (int, float)) for sub_item in value)]
tuple_string_values = [value for value in my_dict.values() if isinstance(value, tuple)
                      and all(isinstance(sub_item, str) for sub_item in value)]
print(f"Max number value: {max(number_values)}")
print(f"Min number value: {min(number_values)}")
print(f"Max string value: {max(string_values)}")
print(f"Min string value: {min(string_values)}")
print(f"Max list value (with number elements): {max(list_number_values)}")
print(f"Min list value (with number elements): {min(list_number_values)}")
print(f"Max list value (with string elements): {max(list_string_values)}")
print(f"Min list value (with string elements): {min(list_string_values)}")
print(f"Max set value (with number elements): {max(set_number_values)}")
print(f"Min set value (with number elements): {min(set_number_values)}")
print(f"Max set value (with string elements): {max(set_string_values)}")
print(f"Min set value (with string elements): {min(set_string_values)}")
print(f"Max tuple value (with number elements): {max(tuple_number_values)}")
print(f"Min tuple value (with number elements): {min(tuple_number_values)}")
print(f"Max tuple value (with string elements): {max(tuple_string_values)}")
print(f"Min tuple value (with string elements): {min(tuple_string_values)}")
