# Написати скрипт, який приймає від користувача два числа (int або float)
# і робить наступне: Кожне введене значення спочатку пробує перевести в int.
# У разі помилки - пробує перевести в float, а якщо і там ловить помилку -
# пропонує ввести значення ще раз (зручніше на даному етапі навчання для
# цього використати цикл while)
# Виводить результат ділення першого на друге. Якщо при цьому виникає помилка -
# оброблює її і виводить відповідне повідомлення

while True:
    try:
        input1 = input("Введіть перше число: ")
        number1 = int(input1)

        input2 = input("Введіть друге число: ")
        number2 = int(input2)

        break
    except ValueError:
        try:
            number1 = float(input1)
            number2 = float(input2)
            break
        except ValueError:
            print("Помилка: Введені значення не є числами (int або float). Спробуйте ще раз.")

try:
    result = number1 / number2
    print(f"Результат ділення: {result}")
except ZeroDivisionError:
    print("Помилка: Ділення на нуль неможливе.")
except Exception as e:
    print(f"Помилка: {e}")
