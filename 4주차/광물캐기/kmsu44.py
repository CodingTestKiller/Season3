# 9시 30분 시작
def findscore(start, end, picks, minerals):
    score = 0
    if picks[0] > 0:
        score += end-start+1
        picks[0] -= 1
    elif picks[1] > 0:
        for i in range(start, end+1):
            mineral = minerals[i]
            if mineral == 'diamond':
                score += 5
            elif mineral == 'iron':
                score += 1
            else:
                score += 1
        picks[1] -= 1
    else:
        for i in range(start, end+1):

            mineral = minerals[i]
            if mineral == 'diamond':
                score += 25
            elif mineral == 'iron':
                score += 5
            else:
                score += 1
        picks[1] -= 1
    return score


def solution(picks, minerals):
    answer = 0
    cnt = 0
    score = 0
    L = []
    start = 0
    size = sum(picks) * 5
    flag = True
    for idx, mineral in enumerate(minerals):
        if mineral == 'diamond':
            score += 25
        elif mineral == 'iron':
            score += 5
        else:
            score += 1
        cnt += 1
        if cnt == 5:
            cnt = 0
            L.append((score, start, idx))
            score = 0
            start = idx+1
        if idx == size:
            flag = False
            break
    if flag:
        L.append((score, start, len(minerals)-1))
    L.sort(key=lambda x: -x[0])
    for score, start, end in L:
        answer += findscore(start, end, picks, minerals)

    return answer
