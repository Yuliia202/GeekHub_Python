# Користувачем вводиться початковий і кінцевий рік. Створити цикл, який
# виведе всі високосні роки в цьому проміжку (границі включно). P.S. Рік
# є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400.

start_year = int(input('Введіть початковий рік:'))
finish_year = int(input('Введіть кінцевий рік:'))
for i in range(start_year, finish_year+1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(i)