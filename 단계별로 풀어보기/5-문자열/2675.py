cases = int(input())
for _ in range(cases):
    num, s = input().split()
    num = int(num)
    for char in s:
        print(char*num, end='')
    print()