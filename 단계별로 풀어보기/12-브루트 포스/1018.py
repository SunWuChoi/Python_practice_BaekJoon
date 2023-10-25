row, col = map(int, input().split())
board = []

for _ in range(row):
    board.append(list(input()))

best = row * col

for i in range(row - 8 + 1):
    for j in range(col - 8 + 1):
        bcurr = 0
        wcurr = 0
        for ii in range(i, i + 8):
            for jj in range(j, j + 8):
                if (ii + jj) % 2 == 0:
                    if board[ii][jj] == 'W':
                        bcurr += 1
                    if board[ii][jj] == 'B':
                        wcurr += 1
                else:
                    if board[ii][jj] == 'B':
                        bcurr += 1
                    if board[ii][jj] == 'W':
                        wcurr += 1
        if min(wcurr, bcurr) < best:
            best = min(wcurr, bcurr)

print(best)