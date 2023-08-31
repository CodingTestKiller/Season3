import math

def solution(picks, minerals):

    answer = 0
    picks = [0]*picks[0] + [1]*picks[1] + [2]*picks[2]
    mineral_set = convert(len(picks), minerals)
    
    mineral_count = []
    for minerals in mineral_set:
        mineral_count.append([minerals.count(0), minerals.count(1), minerals.count(2)])
    mineral_count.sort(reverse=True)
    
    for idx, mineral in enumerate(mineral_count):
        answer += calculate(picks[idx], mineral)
    
    return answer

def convert(n, minerals):
    count = min(n, math.ceil(len(minerals)/5))
    mlist = [[] for _ in range(count)]
    idx = 0

    for mineral in minerals:
        if len(mlist[idx]) ==5:            
            idx+=1
            if idx == count:
                break

        if mineral == 'diamond':
            mlist[idx].append(0)
        elif mineral == 'iron':
            mlist[idx].append(1)
        elif mineral == 'stone':
            mlist[idx].append(2)

    return mlist

def calculate(pick, minerals):
    fatigue = 0
    attack = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    for i in range(3):
        fatigue += attack[pick][i]*minerals[i]

    return fatigue