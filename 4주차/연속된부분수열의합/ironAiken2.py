def solution(sequence, k):
    answer = [0, len(sequence) - 1]
    
    p1, p2 = 0, 0
    flag = 0
    while p2 < len(sequence):
        if flag < k:
            flag += sequence[p2]
            p2 += 1
        elif flag > k:
            flag -= sequence[p1]
            p1 += 1
        else:
            if p2 - p1 - 1 < answer[1] - answer[0]:
                answer = [p1, p2-1]
            flag += sequence[p2]
            p2 += 1
    
    p2 -= 1
    while p1 < len(sequence):
        if flag < k:
            break
        flag -= sequence[p1]
        p1 += 1
        if flag == k and p2 - p1 < answer[1] - answer[0]:
            answer = [p1, p2]
            
        
    return answer