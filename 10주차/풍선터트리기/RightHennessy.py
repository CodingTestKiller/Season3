from collections import deque

def solution(a):
    global a_dict
    a_dict = {}
    global a_list
    a_list = a
    global sorted_a
    sorted_a = deque(sorted(a_list))
    global min_left
    min_left = a_list[0]
    global min_right
    if min_left == sorted_a[0]:
        sorted_a.popleft()
    min_right = sorted_a.popleft()

    for x in a_list:
        a_dict[x] = False
    a_dict[min_left] = True
    a_dict[min_right] = True
        
    answer = 0
    for i in range(len(a)):
        answer += check(i)
    return answer

def check(i: int):
    a_dict[a_list[i]] = True
    global min_left, min_right
    if i==0 or i==len(a_list)-1:
        return 1
    if a_list[i-1] < min_left:
        min_left = a_list[i-1]
    if a_list[i] == min_right:
        while a_dict[min_right]:
            min_right = sorted_a.popleft()

    if a_list[i] == max(min_left, min_right, a_list[i]):
        return 0
    return 1