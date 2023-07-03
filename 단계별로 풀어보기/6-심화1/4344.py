n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    print(f"{len([i for i in l[1:] if i > (sum(l[1:]) / l[0])]) / l[0] * 100:.3f}%")