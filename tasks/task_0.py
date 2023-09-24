i = 0
summa = 0
while True:
    num = int(input())
    if num < 0:
        i += 1
    if i == 3:
        break
    summa += num
    print(summa)
