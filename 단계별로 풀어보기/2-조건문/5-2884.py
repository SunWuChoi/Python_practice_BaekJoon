hour, min = map(int, input().split())

if min < 45:
    hour -= 1
    if hour == -1:
        hour = 23
    min += 15
else:
    min -= 45

print(f"{hour} {min}")