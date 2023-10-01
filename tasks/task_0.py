negative_count: int = 0
negative_sum: int = 0
positive_sum: int = 0
while True:
    num: int = int(input())

    if num < 0:
        negative_count += 1
        negative_sum += num
    elif num > 0:
        positive_sum += num

    if negative_count == 3:
        break

print('Сумма положительных чисел:', positive_sum)
print('Сумма отрицательных чисел:', negative_sum)

# ---------------- №2 ----------------
negative_count: int = 0
negative_sum: int = 0
positive_sum: int = 0
while negative_count < 3:

    num: int = int(input())

    if num < 0:
        negative_count += 1
        negative_sum += num
    elif num > 0:
        positive_sum += num

print('Сумма положительных чисел:', positive_sum)
print('Сумма отрицательных чисел:', negative_sum)
