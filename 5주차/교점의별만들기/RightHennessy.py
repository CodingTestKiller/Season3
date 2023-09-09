from collections import deque

dots = []

def solution(line):

    n = len(line)
    for i in range(n):
        for j in range(i+1, n):
            find_meet(line[i], line[j])

    dots.sort(key = lambda x: x[0])
    x_min = dots[0][0]
    x_max = dots[-1][0] - x_min + 1
    dots.sort(key = lambda x: x[1])
    y_min = dots[0][1]
    y_max = dots[-1][1] - y_min + 1
    answer = [['.']*x_max for _ in range(y_max)]
    for dot in dots:
        answer[dot[1]-y_min][dot[0]-x_min] = '*'
    
    answers = deque([])
    for a in answer:
        answers.appendleft(''.join(a))
    return list(answers)

def find_meet(line1, line2):
    a, b, e = line1
    c, d, f = line2

    denom = a*d - b*c
    if denom == 0:
        return
    
    x_num = b*f - e*d
    y_num = e*c - a*f
    if x_num%denom !=0 or y_num%denom != 0:
        return

    dots.append([x_num//denom, y_num//denom])
