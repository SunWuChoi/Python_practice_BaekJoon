from collections import deque

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    cabbage_list = []
    for _ in range(k):  # populating the cabbage in the grid
        a, b = map(int, input().split())
        cabbage_list.append([a, b])

    worm = 0
    while cabbage_list:
        curr_c = cabbage_list[0]
        worm += 1
        cabbage_list.remove(curr_c)
        to_check = deque([(curr_c[0], curr_c[1])])
        while to_check:
            c = to_check.popleft()
            for adj_c in [[c[0] + 1, c[1]], [c[0] - 1, c[1]], [c[0], c[1] + 1], [c[0], c[1] - 1]]:
                if adj_c in cabbage_list:
                    to_check.append(adj_c)
                    cabbage_list.remove(adj_c)

    print(worm)

