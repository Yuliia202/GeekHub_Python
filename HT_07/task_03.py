# На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
#    а) створити список із парами ім('я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції)'' '
# '- як валідні, так і ні;)
#    б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і
# надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK
#    P.S. Не забудьте використати блок try/except ;)

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

    return "OK"


# Створіть список пар ім'я/пароль для перевірки.
credentials_list = [
    ("vasya", "wasd"),
    ("vasya", "vasyapupkin2000"),
    ("user123", "short"),
    ("user1", "passwordwith1number"),
    ("user2", "password$with*special")
]

for login, password in credentials_list:
    try:
        login = input("Please enter your name: ")
        password = input("Please enter your password: ")
        result = validate_credentials(login, password)
        print(f"Name: {login}")
        print(f"Password: {password}")
        print(f"Status: {result}")
        print("-----")
    except ValidationException as e:
        print(f"Name: {login}")
        print(f"Password: {password}")
        print(f"Status: {e}")
        print("-----")