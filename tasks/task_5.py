n = int(input())
num = 1
for n in range(1, n + 1):
    while num > 0:
        if num % n == 0:
            num += 1
            print(num)

