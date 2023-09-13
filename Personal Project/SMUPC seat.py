row, col, num = map(int, input().split())
l = []
for i in range(row):
    l.append(input())

seat = "0" * num
count = 0

for row in l:
    for i in range(col - num + 1):
        if row[i:i+num] == seat:
            count += 1

print(count)
