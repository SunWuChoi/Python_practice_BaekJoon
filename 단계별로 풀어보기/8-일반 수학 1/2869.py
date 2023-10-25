A, B, V = map(int, input().split())
days = int((V - A) / (A - B) + ((V - A) % (A - B) > 0)) + 1
print(days)
