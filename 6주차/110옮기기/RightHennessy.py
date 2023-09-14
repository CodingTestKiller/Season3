# 2시간

from collections import deque

def solution(s):
    answer = []
    for x in s:
        answer.append(convert(list(x)))
    return answer

def convert(s):
    if len(s) <= 3 :
        return ''.join(s)

    count = 0
    stack = []
    for x in s:
        stack.append(x)
        if x=='0' and stack[-3:] == ['1', '1', '0']:
            count+=1
            del stack[-3:]
    
    for i in range(len(stack)-1, -1, -1):
        if stack[i]=='0':
            return ''.join(stack[:i+1] + ['1','1','0']*count + stack[i+1:])
    return ''.join(['1', '1', '0']*count + stack)
