# Написати скрипт, який приймає від користувача два числа (int або float)
# і робить наступне: Кожне введене значення спочатку пробує перевести в int.
# У разі помилки - пробує перевести в float, а якщо і там ловить помилку -
# пропонує ввести значення ще раз (зручніше на даному етапі навчання для
# цього використати цикл while)
# Виводить результат ділення першого на друге. Якщо при цьому виникає помилка -
# оброблює її і виводить відповідне повідомлення

input_needed = True
while input_needed:
    text = ''
    input1 = input("Введіть перше число: ")
    input2 = input("Введіть друге число: ")
    try:
        number1 = int(input1)
        number2 = int(input2)
        print_text = "Обидва введені значення є int"
    except ValueError:
        try:
            number1 = float(input1)
            number2 = float(input2)
            text = "Одне з чисел float"
        except ValueError:
            text = "Помилка: Введені значення не є числами (int або float). Спробуйте ще раз."
    except ZeroDivisionError:
        text = "Помилка: Ділення на нуль неможливе."
    except Exception as e:
        text = f"Помилка: {e}"

    if not text:
        try:
            result = number1 / number2
            print(f"Результат ділення: {result}")
        except ZeroDivisionError:
            text = "Помилка: Ділення на нуль неможливе."
        except Exception as e:
            text = f"Помилка: {e}"

    print(text)
    if not text:
        input_needed = False



