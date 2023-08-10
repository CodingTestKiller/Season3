def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    cnt = 0
    
    while A and B:
        if A[-1] < B[-1]:
            cnt += 1
            A.pop()
            B.pop()
        else:
            B.pop()
            
    return cnt