def solution(board, skill):
    answer = 0
    tmp = [[0 for _ in range(len(board[0])+2)] for _ in range(len(board)+2)]
    skill.sort(key=lambda x: [x[1], x[2]])
    for t, x1, y1, x2, y2, degree in skill:
        if t == 1:
            degree *= -1
        tmp[x1+1][y1+1] += degree
        tmp[x2+2][y2+2] += degree
        tmp[x1+1][y2+2] -= degree
        tmp[x2+2][y1+1] -= degree

    for col in range(1, len(board)+2):
        for row in range(1, len(board[0])+2):
            tmp[col][row] += tmp[col][row-1]
    for row in range(1, len(board[0])+2):
        for col in range(1, len(board)+2):
            tmp[col][row] += tmp[col-1][row]

    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):
            board[i-1][j-1] += tmp[i][j]
            if board[i-1][j-1] > 0:
                answer += 1

    return answer
