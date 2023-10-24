# Write a Python program that demonstrates exception chaining.Create
# a custom exception class called CustomError and another called SpecificError.
# In your program (could contain any logic you want), raise a SpecificError, and
# then catch it in a try/except block, re-raise it as a CustomError with the original
# exception as the cause. Display both the custom error message and the original exception
# message.

class CustomError(Exception):
    pass


class SpecificError(Exception):
    pass


try:
    raise SpecificError("This is a specific error.")
except SpecificError as specific_error:
    print("Caught SpecificError:", specific_error)

    try:
        raise CustomError("Custom error occurred.") from specific_error
    except CustomError as custom_error:
        print("Caught CustomError:", custom_error)
        print("Original Exception Message:", custom_error.__cause__)
