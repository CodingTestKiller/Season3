def solution(A, B):
    answer = 0
    i = 0
    idx = 0
    A.sort()
    B.sort()
    size = len(A)
    while B:
        if max(idx,i) >= size: 
            break
        if A[idx] >= B[i] : 
            i += 1
        else:
            idx += 1
            i += 1
            answer += 1 
    return answer