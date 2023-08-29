def solution(board, skill):
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        degree = -degree if type == 1 else degree
        tmp[r1][c1] += degree
        tmp[r2 + 1][c1] -= degree
        tmp[r1][c2 + 1] -= degree
        tmp[r2 + 1][c2 + 1] += degree

    for i in range(len(board) + 1):
        for j in range(1, len(board[0]) + 1):
            tmp[i][j] += tmp[i][j - 1]

    for j in range(len(board[0]) + 1):
        for i in range(1, len(board) + 1):
            tmp[i][j] += tmp[i - 1][j]

    return sum([1 if 0 < board[j][i] + tmp[j][i] else 0 for j in range(len(board)) for i in range(len(board[0]))])
