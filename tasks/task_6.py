onset = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
if (onset or end) < 0:
    print("Некорректный диапазон")
elif onset == end:
    print("Некорректный диапазон")
else:
    for i in range(onset, end + 1):
        pass



