from collections import deque
moves = [[0,-1],[0,1],[1,0],[-1,0]]
# 시작점 인덱스 탐색, 10,000
def find_goal_index(board):    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                return (i, j)

def solution(board):
    cons = find_goal_index(board)
    s_i, s_j = cons[0], cons[1]
    e_i, e_j = len(board), len(board[0])
    
    q = deque()
    q.append((s_i, s_j, 0))
    
    visit = [[False for _ in range(e_j)] for _ in range(e_i)]
    visit[s_i][s_j] = True
    
    while q:
        i, j, cnt = q.popleft()
        if board[i][j] == 'G':
            return cnt
        
        for move in moves:
            ni, nj = i, j
            while 0 <= ni + move[0] < e_i and 0 <= nj + move[1] < e_j and board[ni + move[0]][nj + move[1]] != 'D':
                ni += move[0]
                nj += move[1]
            if visit[ni][nj] == False:
                visit[ni][nj] = True
                q.append((ni, nj, cnt+1))
                
    return -1