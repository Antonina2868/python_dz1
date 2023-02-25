# 3. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Далее необходимо собрать аналитику о товарах. Реализовать словарь,в котором каждый ключ —
# характеристика товара, напр.название,а значение—список значений-характеристик, напр.список названий товаров.
# Пример:
# {
# “названия”: [“компьютер”, “принтер”, “сканер”],
# “цены”: [20000, 6000, 2000],
# “количества”: [5, 2, 7],
# “ед”: [“шт.”]
# }
products = []
quest = "Y"
while quest.lower() == "y":
    n = int(input("Введите номер товара: "))
    prod_name = input("Введите название товара: ")
    prod_price = int(input("Введите стоимость товара: "))
    prod_quantity = int(input("Введите количество товара: "))
    prod_measure = input("Введите единицу измерения товара: ")

    products.append((n, {
        "название": prod_name,
        "цена": prod_price,
        "количество": prod_quantity,
        "ед": prod_measure,
    }))
    quest = input("Добавить товар?(Y/N)")

print(products)

