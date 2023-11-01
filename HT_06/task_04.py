# Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме
# список простих чисел всередині цього діапазона. Не забудьте про перевірку на валідність введених даних
# та у випадку невідповідності - виведіть повідомлення.

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_list(start, end):
    if start < 2 or end < 2:
        print("Start and end must to be no less 2")
        return []

    if start > end:
        print("Start must to be less or = end")
        return []

    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes


start = int(input("Please enter start number: "))
end = int(input("Please enter end number: "))
print(prime_list(start, end))
