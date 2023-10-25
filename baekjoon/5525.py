n = int(input())
m = int(input())
s = input()
I = "I" + ("OI" * n)
count = 0
li = len(I)

for i in range(len(s)):
    if s[i: i + li] == I:
        count += 1

print(count)
