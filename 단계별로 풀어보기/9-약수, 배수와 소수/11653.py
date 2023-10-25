num = int(input())
i = 2
while num != 1:
    if num % i == 0:
        num //= i
        print(i)
        i = 2
        if num == 1:
            break
    else:
        i += 1
