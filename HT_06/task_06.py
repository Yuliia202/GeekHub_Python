# Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
# Тобто функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня -
# пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
#    Наприклад:
#    fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#    fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]

def cyclic_shift(lst, shift):
    if not lst:
        return lst

    n = len(lst)
    shift = shift % n

    if shift == 0:
        return lst

    return lst[-shift:] + lst[:-shift] if shift > 0 else lst[-shift:] + lst[:-shift]


list1 = input("Please enter a list (comma-separated values): ")
list1 = [int(x.strip()) for x in list1.split(",")]
shift1 = int(input("Please enter the shift value: "))
result1 = cyclic_shift(list1, shift1)
print(result1)


