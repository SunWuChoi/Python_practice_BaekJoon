num = int(input())
stringOfNums = input()
total = 0
for i in range(num):
    total += int(stringOfNums[i])
print(total)