onset = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if (onset < 0) or (end < 0) or (onset == end):
    print("Некорректный диапазон")
else:

    # 1.Если начало диапазона больше конца:
    # необходимо изменить порядок и идти от меньшего числа к большему;

    for i in range(onset, end + 1):

        for j in range(2, ...):  # 2.

            if i % j == 0:
                break
        else:
            print(...)  # 3.
