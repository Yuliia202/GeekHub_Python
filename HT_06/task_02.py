# Написати функцію <bank> , яка працює за наступною логікою: користувач робить вклад у розмірі <a> одиниць
# строком на <years> років під <percents> відсотків (кожен рік сума вкладу збільшується на цей відсоток, ці
# гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). Параметр <percents>
# є необов'язковим і має значення по замовчуванню <10> (10%). Функція повинна принтануть суму, яка буде на рахунку,'
# а також її повернути (але округлену до копійок).)


def bank(cash, years, percents=10):
    if cash <= 0 or years <= 0 or percents < 0:
        return "Некоректні вхідні дані"

    for i in range(years):
        cash += cash * (percents / 100)
    return cash


try:
    deposit = float(input("Будь ласка, введіть суму вкладу: "))
    invest_period = int(input("Будь ласка, введіть кількість років: "))

    percents_input = input(
        "Будь ласка, введіть відсоток (натисніть Enter для застосування значення за замовчуванням 10%): ")
    if percents_input == "":
        percents = 10
    else:
        percents = int(percents_input)

    result = bank(deposit, invest_period, percents)
    if type(result) == float:
        print(f"Сума на рахунку після {invest_period} років: {result:.2f}")
    else:
        print(result)
except ValueError:
    print("Помилка: введені дані мають бути числами")