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
    try:
        raise CustomError('Custom error occurred.')
    except CustomError as e:
        print(f'Caught CustomError: {e}')
        raise SpecificError (e)
except SpecificError as  e:
    print(f'Original Exception Message: {e}')


