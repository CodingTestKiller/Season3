# 생각못한 케이스 : 2 빙고가 무적권 안되는게 아님!

def solution(board):
    
    # 개수 비교 선공 == 후공 or 선공+1 == 후공
    o_count = 0
    x_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_count += 1
            elif board[i][j] == 'X':
                x_count += 1
    if o_count != x_count and o_count != x_count+1:
        return 0
    
    # 승리
    o_win = 'OOO'
    o_win_count = 0
    x_win = 'XXX'
    x_win_count = 0
    # 가로
    for i in range(3):
        if board[i] == o_win:
            o_win_count += 1
        elif board[i] == x_win:
            x_win_count += 1
    # 대각선
    cross = board[0][0]+board[1][1]+board[2][2]
    if cross == o_win:
        o_win_count += 1
    elif cross == x_win:
        x_win_count += 1
    cross = board[0][2]+board[1][1]+board[2][0]
    if cross == o_win:
        o_win_count += 1
    elif cross == x_win:
        x_win_count += 1
    # 세로
    reversed_board = list(map(list, zip(*board)))
    for i in range(3):
        b = ''.join(reversed_board[i])
        if b == o_win:
            o_win_count += 1
        elif b == x_win:
            x_win_count += 1
            
    if o_win_count == x_win_count:
        if o_win_count >= 1:
            return 0
        
    if x_win_count >= 1 and x_count < o_count:
        return 0
    if o_win_count == 1 and x_count == o_count:
        return 0
    
    return 1