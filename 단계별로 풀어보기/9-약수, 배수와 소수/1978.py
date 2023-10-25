import math


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


case = int(input())
num_list = list(map(int, input().split()))
counter = 0
for num in num_list:
    if isPrime(num):
        counter += 1
print(counter)
