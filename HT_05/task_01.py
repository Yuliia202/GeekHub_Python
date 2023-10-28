# Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12)
# та яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь).
# У випадку некоректного введеного значення - виводити відповідне повідомлення.

def all_season(month):
    if month == 12 or month == 1 or month == 2:
        return "Зима"
    elif month == 3 or month == 4 or month == 5:
        return "Весна"
    elif month == 6 or month == 7 or month == 8:
        return "Літо"
    elif month == 9 or month == 10 or month == 11:
        return "Осінь"
    else:
        return "Ви ввели некоректне значення"

season = int(input("Введіть номер місяця: "))
result = all_season(season)
print(result)





