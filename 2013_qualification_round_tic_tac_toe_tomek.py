for case in range(1, int(input()) + 1):
    board = rows = [list(input()) for _ in range(4)]
    rows.extend(zip(*board)) # adding columns
    rows.append([board[i][i] for i in range(4)]) # adding diagonals
    rows.append([board[i][-i - 1] for i in range(4)])
    ans = 'Game has not completed'
    if all(all(s != '.' for s in row) for row in board):
            ans = 'Draw'
    for row in rows:
        if all(s == 'X' or s == 'T' for s in row):
            ans = 'X won'
        if all(s == 'O' or s == 'T' for s in row):
            ans = 'O won'
    print('Case #{}: {}'.format(case, ans))
    input()
