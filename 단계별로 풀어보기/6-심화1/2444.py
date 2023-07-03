num = int(input())

for i in range(num - 1):
    print(' ' * (num - i - 1) + '*' * (2 * i + 1))
print('*' * (2 * num - 1))
for i in range(num - 1):
    print(' ' * (i + 1) + '*' * (2 * (num - i - 1) - 1))
