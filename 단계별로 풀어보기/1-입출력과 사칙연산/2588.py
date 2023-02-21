X = int(input())
Y = input()
total = 0
for digit in range(len(Y)):
    num = int(Y[len(Y) - 1 - digit])
    print(X * num)
    mult_num = X * num * 10 ** digit
    total += mult_num
print(total)
