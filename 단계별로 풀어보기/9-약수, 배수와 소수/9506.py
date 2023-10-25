while True:
    num = int(input())
    if num == -1:
        break
    divisor = []
    for i in range(1, num):
        if num % i == 0:
            divisor.append(i)
    if sum(divisor) == num:
        print(num, " = ", " + ".join(str(i) for i in divisor), sep="")
    else:
        print(f"{num} is NOT perfect.")
