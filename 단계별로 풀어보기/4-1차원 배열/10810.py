size, num = map(int, input().split())

l = [0 for i in range(size)]

for _ in range(num):
    i, j, k = map(int, input().split())
    for index in range(i - 1, j):
        l[index] = k

print(*l)