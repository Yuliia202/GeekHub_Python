# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції. Тобто щоб її можна було
# використати у вигляді: for i in my_range(1, 10, 2):
# print(i) 1 3 5 7 9 P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
# https://docs.python.org/3/library/stdtypes.html
# range P.P.P.S Не забудьте обробляти невалідні ситуації (аналог range(1, -10, 5)).
# Подивіться як веде себе стандартний range в таких випадках.


def my_range(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        raise TypeError(f"my_range expected at most 3 arguments, got {len(args)}")

    if step == 0:
        raise ValueError("my_range() arg 3 must not be zero")

    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step


for i in my_range(1, 10, 2):
    print(i)
