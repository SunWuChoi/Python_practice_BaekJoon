n = int(input())

for _ in range(n):
    inp = input().split("X")
    score = 0
    for a in inp:
        if (a := len(a)) > 0:
            score += (a * (a+1)) // 2
    print(score)