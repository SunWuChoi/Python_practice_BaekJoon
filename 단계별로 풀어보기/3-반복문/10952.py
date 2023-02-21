flag = True
while flag:
    first, second = map(int, input().split())
    if first == 0 and second == 0:
        flag = False
    else:
        print(first+second)