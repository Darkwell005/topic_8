negative_count = 0
negative_sum = 0
positive_sum = 0
while True:
    num = int(input())
    if num < 0:
        negative_count += 1
        negative_sum += num

    if negative_count == 3:
        break
    elif num > 0:
        positive_sum += num
print(negative_sum)
print(positive_sum)
