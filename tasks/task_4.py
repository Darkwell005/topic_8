num: int = int(input("Введите число: "))
if num < 0:
    print("Число должно быть положительным")
for i in range(2, num):
    if num % i == 0:
        print("Число", num, "не является простым")
        i += 1
else:
    print("Число", num, "является простым")
