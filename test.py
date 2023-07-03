size = int(input())

lst = [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]

while size > 3:
    bigger_lst = [[' ' for i in range(len(lst) * 3)] for j in range(len(lst) * 3)]
    for row in range(len(lst)):
        for col in range(len(lst)):
            if lst[row][col] == '*':
                bigger_lst[row * 3 + 0][col * 3 + 0] = '*'
                bigger_lst[row * 3 + 0][col * 3 + 1] = '*'
                bigger_lst[row * 3 + 0][col * 3 + 2] = '*'
                bigger_lst[row * 3 + 1][col * 3 + 0] = '*'
                bigger_lst[row * 3 + 1][col * 3 + 2] = '*'
                bigger_lst[row * 3 + 2][col * 3 + 0] = '*'
                bigger_lst[row * 3 + 2][col * 3 + 1] = '*'
                bigger_lst[row * 3 + 2][col * 3 + 2] = '*'
    lst = bigger_lst
    size //= 3

for line in lst:
    print(''.join(line))
