m = [list(input()) for _ in range(5)]
c = 0

while True:
    for i in range(5):
        if len(m[i]) != 0:
            print(m[i].pop(0), end="")

    if not any(m):
        break
