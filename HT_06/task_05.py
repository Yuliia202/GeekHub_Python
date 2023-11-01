# Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі,
# що не перевищують його.

def fibonacci(number):
    a, b = 0, 1
    while a <= number:
        print(a, end=" ")
        a, b = b, a + b


value = int(input("Введіть максимальне значення для чисел Фібоначчі: "))
fibonacci(value)
