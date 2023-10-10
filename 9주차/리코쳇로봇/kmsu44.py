from collections import deque
def BFS(board,start,end):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    q = deque()
    board[start[0]][start[1]] = 2
    q.append((start[0],start[1],0))
    while q:
        kx,ky,cnt = q.popleft()
        if (kx,ky) == end:
            return cnt
        for i in range(4):
            mx = kx
            my = ky
            while True:
                mx = mx + dx[i]
                my = my + dy[i]
                if 0 <= mx < len(board) and 0 <= my < len(board[0]) and (board[mx][my] == 0 or board[mx][my] == 2):
                    
                    continue
                else:
                    break
            mx = mx - dx[i]
            my = my - dy[i]
            if board[mx][my] != 2:
                board[mx][my] = 2
                q.append((mx,my,cnt+1))
    return -1
    
def solution(board):
    answer = 0
    n,m = len(board), len(board[0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] =='R':
                start = (i,j)
                visit[i][j] = 2
            if board[i][j] == 'G':
                end = (i,j)
            if board[i][j] == 'D':
                visit[i][j] = 3
    answer = BFS(visit,start,end)
    return answer