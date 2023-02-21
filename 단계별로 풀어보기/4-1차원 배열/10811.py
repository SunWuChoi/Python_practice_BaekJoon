size, m = map(int, input().split())
*l, = range(1, size + 1)

for _ in range(m):
    start, end = map(int, input().split())
    l[start - 1: end] = list(reversed(l[start - 1: end]))

print(*l)
