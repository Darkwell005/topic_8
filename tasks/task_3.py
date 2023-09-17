n: int = int(input())

summa: int = 0
for i in range(1, n + 1):
    summa += i
    if summa > 100:
        print("Сумма всех чисел в диапазоне от 1 до", n, "больше 100")
        break
else:
    print(summa)
