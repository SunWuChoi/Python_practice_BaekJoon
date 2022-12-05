x = int(input())
y = int(input())
q = 0
sign = 1
if y < 0:
    q = 5
    sign = -1

if x < 0:
    q += 2 * sign
elif x > 0:
    q += sign
print(q)