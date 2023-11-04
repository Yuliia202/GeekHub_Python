# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій -
# необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
#     якщо введено коректну пару ім'я/пароль - вертається True;
#     якщо введено неправильну пару ім'я/пароль:
#         якщо silent == True - функція вертає False
#         якщо silent == False -породжується виключення LoginException (його також треба створити =))

class LoginException(Exception):
    pass

def check_values(user_name, password, silent=False):
    users = [
        ("user1", "password1"),
        ("user2", "password2"),
        ("user3", "password3"),
        ("user4", "password4"),
        ("user5", "password5")
    ]
    for user, passw in users:
        if user == user_name and passw == password:
            return True

    if silent:
        return False
    else:
        raise LoginException("Невірна пара ім'я/пароль")

try:
    username = input("Введіть ім'я: ")
    password = input("Введіть пароль: ")
    result = check_values(username, password)
    if result:
        print("Успішний вхід!")
    else:
        print("Невірна пара ім'я/пароль")
except LoginException as e:
    print(f"Помилка входу: {e}")



