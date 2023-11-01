# Написати функцію <bank> , яка працює за наступною логікою: користувач робить вклад у розмірі <a> одиниць
# строком на <years> років під <percents> відсотків (кожен рік сума вкладу збільшується на цей відсоток, ці
# гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). Параметр <percents>
# є необов'язковим і має значення по замовчуванню <10> (10%). Функція повинна принтануть суму, яка буде на рахунку,'
# а також її повернути (але округлену до копійок).)


def bank(cash, years, percents=10):
    for i in range(years):
        cash += cash * (percents / 100)
    return cash


deposit = float(input("Please enter cash: "))
invest_period = int(input("Please enter years: "))
result = bank(deposit, invest_period)
print(f"Сума на рахунку після {invest_period} років: {result}")