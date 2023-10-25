x_list = set()
y_list = set()
inp = []
for _ in range(3):
    x, y = map(int, input().split())
    x_list.add(x)
    y_list.add(y)
    inp.append((x, y))

for x in x_list:
    for y in y_list:
        if (x, y) not in inp:
            print(x, y)
