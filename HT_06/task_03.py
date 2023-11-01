# Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True,
# якщо це число просте і False - якщо ні.

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


number = int(input("Please enter value: "))
result = is_prime(number)
if result:
    print(f"{number} є простим числом.")
else:
    print(f"{number} не є простим числом.")