# Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних
# букв та цифр, які зустрічаються в рядку більше ніж 1 раз. Рядок буде складатися лише з цифр
# та букв (великих і малих). Реалізуйте обчислення за допомогою генератора.
# Example (input string -> result):
#     "abcde" -> 0            # немає символів, що повторюються
#     "aabbcde" -> 2          # 'a' та 'b'
#     "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
#     "indivisibility" -> 1   # 'i' присутнє 6 разів
#     "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
#     "aA11" -> 2             # 'a' і '1'
#     "ABBA" -> 2             # 'A' і 'B' кожна двічі

def count_repeated(string):
    cleaned_string = ''.join(char for char in string if char.isalnum())
    cleaned_string = cleaned_string.lower()
    counts = {char: cleaned_string.count(char) for char in cleaned_string}
    repeated_count = sum(1 for count in counts.values() if count > 1)

    return repeated_count


print(count_repeated("abcde"))
print(count_repeated("aabbcde"))
print(count_repeated("aabBcde"))
print(count_repeated("indivisibility"))
print(count_repeated("Indivisibilities"))
print(count_repeated("aA11"))
print(count_repeated("ABBA"))
