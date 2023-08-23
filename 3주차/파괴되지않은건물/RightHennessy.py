# 키워드 : 누적합 (partial sum vs prefix sum)
# 이게 왜 누적합..?

def solution(board, skill):

    answer = 0
    n, m = len(board), len(board[0])
    sumtable = [[0]*(m+1) for _ in range(n+1)]

    for s in skill:
        type, r1, c1, r2, c2, degree = s
        type = -1 if type == 1 else 1
        sumtable[r1][c1] += type*degree
        sumtable[r1][c2+1] += -type*degree
        sumtable[r2+1][c1] += -type*degree
        sumtable[r2+1][c2+1] += type*degree

    for x in range(n):
        sumtable[x+1][0] += sumtable[x][0]
    for y in range(m):
        sumtable[0][y+1] += sumtable[0][y]
    for x in range(n):
        for y in range(m):
            sumtable[x+1][y+1] += (sumtable[x+1][y] + sumtable[x][y+1] - sumtable[x][y])
            if board[x][y] + sumtable[x][y] > 0:
                answer += 1

    return answer