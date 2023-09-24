onset = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if (onset < 0) or (end < 0) or (onset == end):
    print("Некорректный диапазон")
elif onset < end:
    for i in range(onset, end + 1):
        for j in range(2, int(i ** 0.5)):
            if i % j == 0:
                print()
                break
elif end > onset:
    for i in range(end, onset + 1):
        for j in range(2, int(i ** 0.5)):
            if i % j == 0:
                print()
                break
# Также не забывайте про:
# "Если начало диапазона больше конца:
# необходимо изменить порядок и идти от меньшего числа к большему;"
