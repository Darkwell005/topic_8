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

print(negative_sum)
