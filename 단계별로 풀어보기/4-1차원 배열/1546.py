n = int(input())
l = list(map(int, input().split()))
print(sum(l) / n / max(l) * 100)