
# Задание 1
a = int(input("Введите количество км в первый день "))
b = int(input("Введите желаемый результат в км "))
km_day = a
count = 1

while (km_day <=b):
    print(f"{count}-й день - {round(km_day, 2)}")
    km_day = km_day+km_day*0.1
    count+=1

print(f"через {count} дней будет достигнут результат не менее {b} км")




# c = (a +a*0.1)
# d = (c + c*0.1)
# e = (d + d*0.1)

