def solution(data, col, row_begin, row_end):
    answer = None
    data.sort(key=lambda x: [x[col-1], -x[0]])

    
    for i in range(row_begin-1, row_end):
        tmp = 0
        for x in data[i]:
            tmp += x % (i+1)
        # print(tmp, i)
        if not answer:
            answer = tmp
        else:
            answer = answer ^ tmp
    
    print(answer)

    return answer

solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3)