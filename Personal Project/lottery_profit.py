import random


def generate_lottery():
    number_list = [i for i in range(1, 46)]
    l = []
    for i in range(6):
        l.append(number_list.pop(random.randint(1, 44 - i)))
    l.sort()
    return l


prize_num = [[16, 18, 20, 23, 32, 43],
             [18, 20, 23, 27, 32, 43],
             [16, 20, 23, 27, 32, 43],
             [16, 18, 23, 27, 32, 43],
             [16, 18, 20, 27, 32, 43],
             [16, 18, 20, 23, 27, 43],
             [16, 18, 20, 23, 27, 32]]

prize_list = []
try_list = []
money = []
i = 0
while True:
    curr_gen = generate_lottery()
    i += 1

    if curr_gen in prize_num:
        if curr_gen == prize_num[0]:
            money.append(2175006375)
        else:
            money.append(46774331)

        prize_list.append(curr_gen)
        try_list.append(i)
        print(i, curr_gen)
        i = 0
        if len(prize_list) == 10:
            break
print(try_list)
print(sum(try_list)/len(try_list))
print(money)
print(sum(money)/len(money))

print(sum(money)/len(money) - sum(try_list)/len(try_list) * 1000)
