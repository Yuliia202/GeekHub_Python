# Написати функцію, яка приймає на вхід список(через кому), підраховує кількість
# однакових елементів у ньомy і виводить результат.Елементами списку можуть бути дані
# будь - яких типів.
# Наприклад:
# 1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] - ---> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"

def count_elements(my_list):
    element_count = {}
    for item in my_list:
        if isinstance(item, (list, bool)):
            item_str = str(item)
        else:
            item_str = item

        if item_str in element_count:
            element_count[item_str] += 1
        else:
            element_count[item_str] = 1

    result = []
    for item, count in element_count.items():
        result.append(f"{item} -> {count}")

    return ', '.join(result)


input_list = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]
print(count_elements(input_list))
