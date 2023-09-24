n: int = int(input())

num: int = n
while True:
    for x in range(1, n + 1):
        if num % x != 0:
            break
    else:
        print(num)
        break

    num += n

    factorial: int = 1
    n_copy: int = n
    while n_copy > 1:
        factorial *= n_copy
        n_copy -= 1

    if num > factorial:
        break
