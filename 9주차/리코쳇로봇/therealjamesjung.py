from collections import deque


def up(board, x, y):
    flag = False
    while x > 0 and board[x-1][y] != 'D':
        flag = True
        x -= 1
    if not flag or board[x][y] == 'X':
        return None
    return (x, y)

def down(board, x, y):
    flag = False
    while x < len(board) - 1 and board[x+1][y] != 'D':
        flag = True
        x += 1    
    if not flag or board[x][y] == 'X':
        return None
    return (x, y)

def left(board, x, y):
    flag = False
    while y > 0 and board[x][y-1] != 'D':
        flag = True
        y -= 1
    if not flag or board[x][y] == 'X':
        return None
    return (x, y)

def right(board, x, y):
    flag = False
    while y < len(board[0]) - 1 and board[x][y+1] != 'D':
        flag = True
        y += 1
    if not flag or board[x][y] == 'X':
        return None
    return (x, y)


def solution(board):
    board = [list(row) for row in board]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start = (i, j)
    
    min_cnt = 10**6
    visited = set()
    queue = deque([(start, 0, None)])

    while queue:
        current, cnt, last_dir = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        if board[current[0]][current[1]] == 'G':
            min_cnt = min(min_cnt, cnt)
            continue

        if cnt >= min_cnt:
            continue

        if last_dir != 'D' and up(board, current[0], current[1]):
            queue.append((up(board, current[0], current[1]), cnt+1, 'U'))
        if last_dir != 'U' and down(board, current[0], current[1]):
            queue.append((down(board, current[0], current[1]), cnt+1, 'D'))
        if last_dir != 'R' and left(board, current[0], current[1]):
            queue.append((left(board, current[0], current[1]), cnt+1, 'L'))
        if last_dir != 'L' and right(board, current[0], current[1]):
            queue.append((right(board, current[0], current[1]), cnt+1, 'R'))
        
    return min_cnt if min_cnt != 10**6 else -1


    