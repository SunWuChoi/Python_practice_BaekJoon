num, kth = map(int, input().split())


def kth_finder(num, kth):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
            if count == kth:
                return i
    return 0

print(kth_finder(num, kth))