def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)

    for _ in range(len(A)):
        if A[-1]<B[-1]:
            answer += 1
            A.pop()
            B.pop()
        else:
            B.pop()

    return answer