original = input()
num = original
count = 0
while True:
    count += 1
    if len(num) == 1:
        num = "0" + num

    num = str(int(num[1] + str(int(num[0]) + int(num[1]))[-1]))

    if num == original:
        print(count)
        break