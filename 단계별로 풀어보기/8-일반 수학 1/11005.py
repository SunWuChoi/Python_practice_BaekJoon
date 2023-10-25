inp_num, base = map(int, input().split())

p = 0
while (inp_num // base ** p) >= base:
    p += 1

size = p + 1

for i in range(size):
    c = inp_num // (base ** (size - 1 - i))
    inp_num = inp_num % (base ** (size - 1 - i))
    if c < 10:
        print(c, end="")
    else:
        print(chr(c + 55), end="")
