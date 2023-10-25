num = int(input())
start_num = 0
if num - len(str(num)) * 9 >= 0:
    start_num = num - len(str(num)) * 9
for i in range(start_num, num):
    total = i
    for small_i in str(i):
        total += int(small_i)
    if total == num:
        print(i)
        break
else:
    print(0)
