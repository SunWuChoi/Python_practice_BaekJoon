l = [i for i in range(1, 31)]

for _ in range(28):
    l.remove(int(input()))

for a in l:
    print(a)