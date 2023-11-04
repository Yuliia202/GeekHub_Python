# Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення
# у вигляді кортежа: периметр квадрата, площа квадрата та його діагональ.

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * 2 ** (1 / 2)
    return perimeter, area, diagonal


value = float(input("Please enter value: "))
result = square(value)
perimeter, area, diagonal = result

print(f"Perimeter: {perimeter}, Area: {area}, Diagonal: {diagonal}")

