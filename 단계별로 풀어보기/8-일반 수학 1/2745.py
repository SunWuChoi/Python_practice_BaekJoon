inp_num, base = input().split()
base = int(base)

total = 0
size = len(inp_num)

for i in range(len(inp_num)):
    try:
        total += int(inp_num[i]) * base ** (size - i - 1)
    except:
        total += (ord(inp_num[i]) - 55) * base ** (size - i - 1)

print(total)
