
x = int(input("Сумма вклада: "))
p = int(input("Годовые проценты: "))
y = int(input("Итоговая сумма вклада: "))
i = y / (x + round(x / 100 * p))
print(float(round(i, 1)))

