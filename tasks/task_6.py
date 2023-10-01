onset: int = int(input("Введите начало диапазона: "))
end: int = int(input("Введите конец диапазона: "))

if (onset < 0) or (end < 0) or (onset == end):
    print("Некорректный диапазон")
else:
    # Отлично!
    onset, end = min(onset, end), max(onset, end)
    for i in range(onset, end + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

# В 3-м тесте программа слоамалась, исправьте пожалуйста,
# а также исправьте вывод результата.
# Число должны выводиться в одну строку через пробел.
