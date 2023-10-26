def solution(board):
    check_list =[
    [(0,0),(0,1),(0,2)], # row1
    [(1,0),(1,1),(1,2)], # row2
    [(2,0),(2,1),(2,2)], # row3
    [(0,0),(1,0),(2,0)], # col1
    [(0,1),(1,1),(2,1)], # col2
    [(0,2),(1,2),(2,2)], # col3
    [(0,0), (1,1),(2,2)], # diagonal1
    [(2,0),(1,1),(0,2)], # diagonal2
    ]
    count1 = 0
    count2 = 0
    for row in board:
        count1 += row.count('O')
        count2 += row.count('X')
    # X의 수가 더 많을 때
    if abs(count2-count1) > 1:
        return 0
    if count1 < count2:
        return 0
    for check in check_list:
        a,b,c = check
        ax,ay = a
        bx,by = b
        cx,cy = c
        if board[ax][ay] =='O' and board[bx][by] =='O' and board[cx][cy] =='O':
            if count1 == count2:
                return 0
        if board[ax][ay] =='X' and board[bx][by] =='X' and board[cx][cy] =='X':
            if count1 > count2:
                return 0
    return 1