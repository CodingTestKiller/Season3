from collections import deque
def solution(board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    N = len(board)
    M = len(board[0])

    distance = [[99999 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        board[i] = list(board[i])
        for j in range(M):
            if board[i][j] == 'R':
                queue.append((i, j, 0))
                distance[i][j] = 0

    while queue:
        x, y, dist = queue.popleft()

        if board[x][y] == 'G':
            return dist

        for i in range(4):
            nx = x
            ny = y

            while nx + dx[i] >= 0 and nx + dx[i] < N and ny + dy[i] >=0 and ny + dy[i] < M and board[nx + dx[i]][ny + dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]

            if distance[nx][ny] > dist + 1:
                distance[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))
    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))