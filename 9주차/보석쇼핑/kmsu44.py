from collections import deque,defaultdict
def solution(gems):
    answer = []
    t = defaultdict(int)
    cnt = len(set(gems))
    left = 0
    right = 0
    size = len(gems)
    tmp_answer = []
    while left < size and right < size and left <= right:
        t[gems[right]] += 1
        while t[gems[left]] > 1:
            t[gems[left]] -= 1
            left +=1
            
        if len(t) == cnt:
            tmp_answer.append((left+1,right+1))
            left += 1
            right = left
            t = defaultdict(int)
            continue
        right +=1
    tmp = [1,size]
    for ans in tmp_answer:
        if tmp[1] - tmp[0] > ans[1] - ans[0]:
            tmp = ans
    answer = tmp
    
    return answer