def solution(board):
    answer = 0

    board_one_row = "".join(board)
    is_count_ok = board_one_row.count('O') - board_one_row.count('X')
    if is_count_ok != 0 or is_count_ok != 1:
        return 0

    board = [list(i) for i in board]
    board_converted = list(zip(*board))
    O_cnt, X_cnt = 0, 0

    for i in range(3):
        if board[i].count('O') == 3 or board_converted[i].count('O') == 3:
            O_cnt += 1
        if board[i].count('X') == 3 or board_converted[i].count('X') == 3:
            X_cnt += 1

    i = 0
    while i < 3:
        if board[0][i] == board[1][1] == board[2][2 - i] == 'O':
            O_cnt += 1
        if board[0][i] == board[1][1] == board[2][2 - i] == 'X':
            X_cnt += 1
        i += 2

    if O_cnt and X_cnt:
        return 0
    if O_cnt == 1 and is_count_ok == 0:
        return 0
    if X_cnt == 1 and is_count_ok > 0:
        return 0
    return 1
print(solution(["OOO", "...", "XXX"]))