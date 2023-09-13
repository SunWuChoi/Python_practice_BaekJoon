s = set()

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0:
        if y > 0:
            s.add("pinf")
        else:
            s.add("minf")
    elif y == 0:
        if x > 0:
            s.add("p0")
        else:
            s.add("m0")
    else:
        if x > 0:
            s.add("p" + str(y / x))
        else:
            s.add("m" + str(y / x))

print(len(s))
