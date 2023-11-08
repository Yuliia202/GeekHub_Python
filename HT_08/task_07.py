# Напишіть функцію, яка приймає 2 списки. Результатом має бути новий список, в якому знаходяться
# елементи першого списку, яких немає в другому. Порядок елементів, що залишилися має відповідати
# порядку в першому (оригінальному) списку. Реалізуйте обчислення за допомогою генератора.
# Приклад: array_diff([1, 2], [1]) --> [2] array_diff([1, 2, 2, 2, 4, 3, 4], [2]) --> [1, 4, 3, 4]


def array_diff(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result


list1_input = input("Please input first values: ")
list1 = [int(x) for x in list1_input.replace(',', ' ').split()]

list2_input = input("Please input second values: ")
list2 = [int(x) for x in list2_input.replace(',', ' ').split()]

result = array_diff(list1, list2)
print(result)
