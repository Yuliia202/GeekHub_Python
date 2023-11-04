# Створіть функцію для валідації пари ім'я/пароль за наступними правилами: - ім'я повинно бути не меншим
# за 3 символа і не більшим за 50; - пароль повинен бути не меншим за 8 символів
# і повинен мати хоча б одну цифру; - якесь власне додаткове правило:)
# Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.

class ValidationException(Exception):
    pass


def validate_credentials(login, password):
    if len(login) < 3 or len(login) > 50:
        raise ValidationException("Name must have 3-50 symbols.")
    if len(password) < 8:
        raise ValidationException("Password must have at least 8 symbols.")

    has_number = False
    has_special_symbol = False

    for char in password:
        if char.isdigit():
            has_number = True
        if char in '!@#$%^&*':
            has_special_symbol = True

    if not has_number:
        raise ValidationException("Password must have at least 1 number.")
    if not has_special_symbol:
        raise ValidationException("Password must have at least 1 special symbol.")

    return True


try:
    username = input("Please input name: ")
    password = input("Please input password: ")
    if validate_credentials(username, password):
        print("Validation successful. You can use this password.")
except ValidationException as e:
    print(f"Validation error: {e}")