# Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат
# (напр. інпут від юзера, результат математичної операції тощо). Також створiть четверту ф-цiю, яка
# всередині викликає 3 попереднi, обробляє їх результат та також повертає результат своєї роботи.
# Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.
from datetime import date


def get_birth_date():
    birth_date_list = input('Enter birth date formatted as DD.MM.YYYY: ').split('.')
    return date(int(birth_date_list[2]), int(birth_date_list[1]), int(birth_date_list[0]))


def get_age(birth_date: date):
    return (date.today() - birth_date).days / 365


def is_adult(age: float):
    return age > 18


def check_adult():
    birth_date = get_birth_date()
    age = get_age(birth_date)
    if is_adult(age):
        result = "Person is adult"
    else:
        result = "Person is not adult"
    return result

# get_age(date(1998,1,17))
print(check_adult())