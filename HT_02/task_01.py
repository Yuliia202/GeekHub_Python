# Write a script which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers.

values = input("Please write comma-seprated numbers : ")
generated_list = values.split(",")
generated_tuple = tuple(generated_list)
print('List : ', generated_list)
print('Tuple : ', generated_tuple)

