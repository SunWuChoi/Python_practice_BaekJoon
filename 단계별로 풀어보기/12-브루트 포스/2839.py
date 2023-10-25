weight = int(input())

if weight % 5 == 0:
    print(weight // 5)
else:
    bag = 0
    while weight > 0:
        weight -= 3
        bag += 1
        if weight % 5 == 0:
            print(weight // 5 + bag)
            break
        elif weight == 1 or weight == 2:
            print(-1)
            break
        elif weight == 0:
            print(bag)
            break
