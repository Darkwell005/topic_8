onset = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if (onset < 0) or (end < 0) or (onset == end):
    print("Некорректный диапазон")
else:
    onset, end = min(onset, end), max(onset, end)

    for i in range(onset, end + 1):

        for j in range(2, i):  # 2.

            if i % j == 0:
                break
        else:
            print(i)  # 3.
