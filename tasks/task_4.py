num: int = int(input("Введите число: "))

if num < 0:
    print("Число должно быть положительным")
else:
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            print("Число", num, "не является простым")
            break
    else:
        print("Число", num, "является простым")
