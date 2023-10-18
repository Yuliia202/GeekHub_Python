#Write a script to check whether a value from user input is contained in a group
# of values.    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
# [1, 2, 'u', 'a', 4, True] --> 5 --> False

user_input = input()
value_to_check = input("Enter a value to check: ")
if value_to_check in user_input:
    print("True")
else:
    print("False")
