def solution(board, skill):
    answer = 0
    sum_table = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for p, r1, c1, r2, c2, dg in skill:
        sum_table[r1][c1] += dg if p == 2 else -dg
        sum_table[r1][c2 + 1] += -dg if p == 2 else dg
        sum_table[r2 + 1][c1] += -dg if p == 2 else dg
        sum_table[r2 + 1][c2 + 1] += dg if p == 2 else -dg
    for i in range(len(sum_table) - 1):
        for j in range(len(sum_table[0]) - 1):
            sum_table[i][j + 1] += sum_table[i][j]
            
    for j in range(len(sum_table[0]) - 1):
        for i in range(len(sum_table) - 1):
            sum_table[i + 1][j] += sum_table[i][j]
            
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += sum_table[i][j]
            if board[i][j] > 0: answer += 1
    return answer