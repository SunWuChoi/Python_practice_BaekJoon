import sys

input = sys.stdin.readline

n, k = map(int, input().split())
p = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]

for _ in range(n):
    po, v = map(int, input().split())
    p[po - 1].append(v)

t = []


def best_calculator(l, k):
    for i in range(k):
        max_val = 0
        max_index = -1

        for i in range(len(l)):
            if l[i] > max_val:
                max_val = l[i]
                max_index = i
        if max_val > 0: l[max_index] -= 1

    return max(l)


for i in range(11): t.append(best_calculator(p[i], k))
print(sum(t))