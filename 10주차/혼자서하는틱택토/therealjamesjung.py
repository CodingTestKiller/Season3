def solution(board):
    board = [list(row) for row in board]

    O_cnt, X_cnt = 0, 0

    for row in board:
        O_cnt += row.count('O')
        X_cnt += row.count('X')
    # print('O_cnt, X_cnt', O_cnt, X_cnt)
    if O_cnt == X_cnt == 0:
        return 1
    if not (0 <= O_cnt - X_cnt <= 1):
        return 0
    
    O_win, X_win = False, False

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'O':
                O_win = True
            elif board[i][0] == 'X':
                X_win = True
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'O':
                O_win = True
            elif board[0][i] == 'X':
                X_win = True
    
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'O':
            O_win = True
        elif board[0][0] == 'X':
            X_win = True
    
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'O':
            O_win = True
        elif board[0][2] == 'X':
            X_win = True
    
    # print(O_win, X_win)
    
    if O_win and X_win:
        return 0
    elif O_win:
        if O_cnt - X_cnt == 1:
            return 1
        else:
            return 0
    elif X_win:
        if O_cnt == X_cnt:
            return 1
        else:
            return 0
    else:
        return 1
    


print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))
print(solution(["...", ".X.", "..."]))
print(solution(["...", "...", "..."]))

