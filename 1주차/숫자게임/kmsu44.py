# 10시 45분 시작
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    size = len(A)
    a = 0
    b = 0
    while a < size and b < size:
        if A[a] < B[b]:
            answer += 1
            a += 1
            b += 1
        else:
            b += 1

    return answer
