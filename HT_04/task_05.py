# Create a Python program that repeatedly prompts the user for a number
# until a valid integer is provided. Use a try/except block to handle any
# ValueError exceptions, and keep asking for input until a valid integer is
# entered. Display the final valid integer.

while True:
    try:
        user_value = input('Please enter a number: ')
        valid_integer = int(user_value)
        print(f'You entered a valid integer: {valid_integer}')
        break
    except ValueError:
        print('Invalid input. Please enter a valid integer.')