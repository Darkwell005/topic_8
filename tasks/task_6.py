onset = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if (onset or end) < 0:
    print("Некорректный диапазон")
elif onset == end:
    print("Некорректный диапазон")
for i in range(onset, end + 1):
    for j in range(2, int(i ** 0.5)):
        if i % j == 0:
            print(j)
            break
