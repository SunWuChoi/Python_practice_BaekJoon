n, x = map(int, input().split())
print(*[i for i in input().split() if int(i) < int(x)])
