from collections import deque

def solution(A, B):
    
    count = 0

    A.sort()
    B.sort()
    
    while (len(A)!=0) & (len(B)!=0) :
        if A[-1] >= B[-1] :
            A.pop()
        else :
            A.pop()
            B.pop()
            count += 1

    return count