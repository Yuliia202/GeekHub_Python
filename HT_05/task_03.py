# Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями. Створiть просту умовну
# конструкцiю (звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися
# рiвнiсть змiнних "x" та "y" та у випадку нервіності - виводити ще і різницю.
# Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
# x > y;       вiдповiдь - "х бiльше нiж у на z"
# x < y;       вiдповiдь - "у бiльше нiж х на z"
# x == y.      вiдповiдь - "х дорiвнює z"

def user_value(x, y):
    if x > y:
        result = f'х бiльше нiж у на {x - y}'
    elif x < y:
        result = f"у бiльше нiж х на {y - x}"
    else:
        result = f"х дорiвнює y"
    return result


x = int(input("Please enter number 1: "))
y = int(input("Please enter value 2: "))
print(user_value(x, y))