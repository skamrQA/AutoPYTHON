def bank(X, Y):
    total = X
    for i in range(Y):
        total = total * 1.1
    return total

X = int(input("Введите размер вклада в рублях: "))
Y = int(input("Введите срок вклада в годах: "))

result = bank(X, Y)
print(f"Сумма на вашем счету спустя {Y} лет будет: {result:.2f} рублей")