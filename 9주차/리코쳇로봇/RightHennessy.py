from collections import deque

def solution(board):
    def move(d, x, y):
        while True: 
            x += d[0]
            y += d[1]
            if x < 0 or x >= x_max or y < 0 or y >= y_max:
                break
            if board[x][y] == 'D':
                break
        return x-d[0], y-d[1]

    x_max = len(board)
    y_max = len(board[0])
    visited = [[-1]*y_max for _ in range(x_max)]
    queue = deque([])

    for x in range(x_max):
        for y in range(y_max):
            if board[x][y] == 'R':
                queue.append([x,y])
                visited[x][y] = 0
            if board[x][y] == 'G':
                x_end, y_end = x, y

    # 4방향 이렇게.. 진짜 천재인가
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    while queue:
        x, y = queue.popleft()
        for d in directions:
            x_next, y_next = move(d, x, y)
            if visited[x_next][y_next] == -1:
                queue.append([x_next, y_next])
                visited[x_next][y_next] = visited[x][y] + 1
    
    return visited[x_end][y_end]