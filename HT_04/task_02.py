# Create a custom exception class called NegativeValueError. Write a
# Python program that takes an integer as input and raises the NegativeValueError
# if the input is negative. Handle this custom exception with a try/except block
# and display an error message.
class NegativeValueError(Exception):
    pass


def positive_integer(value):
    if value < 0:
        raise NegativeValueError("Negative error. Please enter positive number")


try:
    user_input = int(input('Please enter integer: '))
    positive_integer(user_input)
    print("You entered a positive integer:", user_input)
except NegativeValueError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter a valid integer.")
