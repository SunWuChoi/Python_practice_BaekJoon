n, m = map(int, input().split())
*l, = range(1, n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    l[a-1], l[b-1] = l[b-1], l[a-1]
print(*l)
