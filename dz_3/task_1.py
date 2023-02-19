# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень
# """
#
# """
# year_month = input("Ведите номер месяца: ")
# # year_month = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# for i in year_month:
#     if year_month == 12:
#         print("зима")
    # elif year_month == 1:
    #     print("зима")
    # elif year_month == 2:
    #     print("зима")

user_month = int(input("Ведите номер месяца: "))
seasons = {"winter": [12, 1, 2], "spring": [3, 4, 5], "summer": [6, 7, 8], "autumn": [9, 10, 11]}

for season in seasons:
    for month in seasons[season]:
        if user_month == month:
            print(season)