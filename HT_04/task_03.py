# Create a Python script that takes an age as input. If the age is less
# than 18 or greater than 120, raise a custom exception called InvalidAgeError.
# Handle the InvalidAgeError by displaying an appropriate error message.

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if 18 <= age <= 120:
        return
    raise InvalidAgeError("Invalid age. Age must be between 18 and 120.")


try:
    age = int(input('Please enter age: '))
    check_age(age)
    print("Valid age entered:", age)
except InvalidAgeError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter a valid integer for age.")




