import math


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


start = int(input())
end = int(input())

l = []
for i in range(start, end + 1):
    if isPrime(i):
        l.append(i)
if l:
    print(sum(l))
    print(l[0])
else:
    print(-1)
