# 9시 40분 시작

def solution(s):
    answer = -1
    stack = []
    for alphabet in s:
        if stack and stack[-1] == alphabet:
            stack.pop()
        else:
            stack.append(alphabet)
    if stack:
        answer = 0
    else:
        answer = 1

    return answer
