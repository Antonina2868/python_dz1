# Задание 5. Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если слово длинное,
# выводить только первые 10 букв в слове.
# Пример:
# Введите слова через пробел: раз два три
# 1. раз
# 2. два
# 3. три
# Введите слова через пробел: раз перерефрижерированность
# 1. раз
# 2. перерефриж

# li = input("Введите несколько слов через пробел: ")
li = ("Доброе утро многоуважаемые люди")
li_1 = li.split(' ')
count = 0
for elem in li_1:
    count+=1
    if(len(elem)>10):
        elem = elem[:11]
    print(f"{count}. {elem}")
