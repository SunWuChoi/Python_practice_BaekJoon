first, second, third = map(int, input().split())
dice = [0 for i in range(7)]  # dice[0] stores the biggest score

dice[first] += 1
dice[second] += 1
dice[third] += 1

for i in range(len(dice)):
    if dice[i] == 3:
        dice[0] = 10000 + i * 1000
    elif dice[i] == 2:
        dice[0] = 1000 + i * 100
    elif dice[i] == 1:
        if 100 * i > dice[0]:
            dice[0] = 100 * i
print(dice[0])
