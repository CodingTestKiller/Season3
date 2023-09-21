# 2시 20분 시작
def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col-1],-x[0]))
    for row in range(row_begin-1,row_end):
        s = 0
        for j in data[row]:
            s += j % (row+1)
        answer ^= s
    return answer