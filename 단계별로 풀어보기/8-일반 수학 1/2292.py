target = int(input())
i = 1
jump = 0
while target > i:
    jump += 1
    i += 6*jump
jump += 1
print(jump)