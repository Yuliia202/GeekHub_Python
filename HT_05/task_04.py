# Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
# Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
# -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)

def process_string(input_str):
    if 30 <= len(input_str) <= 50:
        letter_count = sum(1 for char in input_str if char.isalpha())
        digit_count = sum(1 for char in input_str if char.isdigit())
        print(f"Довжина рядка: {len(input_str)}, Кількість букв: {letter_count}, Кількість цифр: {digit_count}")
    elif len(input_str) < 30:
        total_sum = sum(int(char) for char in input_str if char.isdigit())
        letters_only = ''.join(char for char in input_str if char.isalpha())
        print(f"Сума всіх чисел: {total_sum}")
        print(f"Рядок без цифр лише з буквами: {letters_only}")
    elif len(input_str) > 50:
        print("Довжина рядка більше 50. Фантазія в дії!")


input_str = input("Введіть рядок: ")
process_string(input_str)
