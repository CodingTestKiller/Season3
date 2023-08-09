def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)

    a = 0
    b = 0
    answer = 0

    while a < len(A) and b < len(B):
        while A[a] >= B[b] and a < len(A) - 1:
            a += 1
        if a == len(A) - 1:
            if A[a] < B[b]:
                answer += 1
            break
        answer += 1
        a += 1
        b += 1

    return answer
