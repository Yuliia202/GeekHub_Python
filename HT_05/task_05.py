# Ну і традиційно - калькулятор. Повинна бути 1 ф-цiя, яка б приймала 3 аргументи
# - один з яких операцiя, яку зробити! Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2;
# можна всі разом - типу 1 + 2). Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте
# протестувати з різними значеннями на предмет помилок!

def calculator(number1: float, operation: str, number2: float):
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        result = number1 / number2
    elif operation == "%":
        result = number1 % number2
    elif operation == "//":
        result = number1 // number2
    elif operation == "**":
        result = number1 ** number2
    else:
        return "Incorrect operator"
    return result


try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /, %, //, or **): ")
    print(calculator(number1, operation, number2))

except ValueError:
    print("Incorrect input. Please enter valid numbers.")
