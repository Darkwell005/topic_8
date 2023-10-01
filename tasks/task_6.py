onset: int = int(input("Введите начало диапазона: "))
end: int = int(input("Введите конец диапазона: "))

if (onset < 0) or (end < 0) or (onset == end):
    print("Некорректный диапазон")
else:
    onset, end = min(onset, end), max(onset, end)

    print('Простые числа в заданном диапазоне:')
    for i in range(onset, end + 1):
        # if i != 0 and i != 1:
        # if i > 1:
        if i >= 2:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i, end=' ')
