from itertools import combinations
def calc(eq1,eq2):
    a,b,e = eq1
    c,d,f = eq2
    
    if a*d == b*c :
        return
    x = (b*f-e*d)/(a*d-b*c)
    y = (e*c-a*f)/(a*d-b*c)
    if x == int(x) and y == int(y):
        return [int(x),int(y)]
def solution(line):
    point_list = []
    for eq1, eq2 in combinations(line,2):
        point = calc(eq1,eq2)
        if point: point_list.append(point)
    left,right = min(point_list,key = lambda x : x[0])[0],max(point_list,key = lambda x : x[0])[0] + 1
    bottom,top = min(point_list,key = lambda x : x[1])[1],max(point_list,key = lambda x : x[1])[1] + 1
    answer = [['.'] * (right - left) for _ in range((top - bottom))]
    for x,y in point_list:
        answer[y-bottom][x-left] = '*'
    answer.reverse()
    return [''.join(a) for a in answer]