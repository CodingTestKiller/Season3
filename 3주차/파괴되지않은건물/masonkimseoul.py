
def solution(board, skill):
    answer = 0
    N = len(board[0])
    M = len(board)

    status = [[0] * (N + 1) for _ in range(M + 1)]

    for s in skill:
        type = -1
        if s[0] == 2: type = 1
        x1, y1, x2, y2 = s[1], s[2], s[3], s[4]
        degree = s[5]

        status[x1][y1] += degree * type
        status[x1][y2 + 1] -= degree * type
        status[x2 + 1][y1] -= degree * type
        status[x2 + 1][y2 + 1] += degree * type

    for i in range(M):
        for j in range(1, N):
            status[i][j] += status[i][j - 1]

    for i in range(N):
        for j in range(1, M):
            status[j][i] += status[j - 1][i]

    for i in range(M):
        for j in range(N):
            board[i][j] += status[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer