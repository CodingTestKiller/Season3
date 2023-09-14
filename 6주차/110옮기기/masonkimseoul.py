from collections import deque

def solution(s):
    answer = []
    for str in s:
        stack = []
        cnt = 0
        for s in str:
            if s == '0':
                if stack[-2:] == ['1', '1']:
                    cnt += 1
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(s)
            else:
                stack.append(s)

        if cnt == 0:
            answer.append(str)
        else:
            res = deque()

            while stack:
                if stack[-1] == '1':
                    res.append(stack.pop())
                elif stack[-1] == '0':
                    break

            while cnt > 0:
                res.appendleft('0')
                res.appendleft('1')
                res.appendleft('1')
                cnt -= 1

            while stack:
                res.appendleft(stack.pop())
            answer.append(''.join(res))

    return answer