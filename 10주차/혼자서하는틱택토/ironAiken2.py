def solution(board):
    # 대각선
    diagonal = [[[0,0], [1,1], [2,2]], [[0,2], [1,1], [2,0]]]
    
    # 순서 맞는지 판별
    cnt_O, cnt_X = 0, 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == 'O': cnt_O += 1
            if board[i][j] == 'X': cnt_X += 1
    if abs(cnt_O - cnt_X) > 1:
        return 0
    if cnt_O < cnt_X:
        return 0
    # 빙고 완성 판별 
    cnt = 0
    for rows in board:
        row = list(set(rows))
        if '.' in row:
            continue
        if len(row) == 1:
            cnt += 1
            if row[0] == 'O' and cnt_O <= cnt_X:
                return 0
            if row[0] == 'X' and cnt_X < cnt_O:
                return 0
    if cnt > 1: return 0
    
    cnt = 0
    for i in range(3):
        height = list(set((board[0][i], board[1][i], board[2][i])))
        if '.' in height:
            continue
        if len(height) == 1:
            cnt += 1
            if height[0] == 'O' and cnt_O <= cnt_X:
                return 0
            if height[0] == 'X' and cnt_X < cnt_O:
                return 0
    if cnt > 1: return 0

    for data in diagonal:
        a, b, c = data[0], data[1], data[2]
        diag = list(set((board[a[0]][a[1]], board[b[0]][b[1]], board[c[0]][c[1]])))
        if '.' in diag:
            continue
        if len(diag) == 1:
            if diag[0] == 'O' and cnt_O <= cnt_X:
                return 0
            if diag[0] == 'X' and cnt_X < cnt_O:
                return 0
 
    return 1