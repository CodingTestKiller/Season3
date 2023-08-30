def solution(picks, minerals):
    answer = 0
    pick_cnt = sum(picks)
    mnr_max = pick_cnt * 5
    if mnr_max < len(minerals):
        minerals = minerals[:mnr_max]

    i = 0
    mnr_count = []
    while i < len(minerals):
        if i + 5 <len(minerals):
            tmp = [minerals[i:i+5].count("diamond"), minerals[i:i+5].count("iron"), minerals[i:i+5].count("stone")]
        else:
            tmp = [minerals[i:].count("diamond"), minerals[i:].count("iron"), minerals[i:].count("stone")]
        i += 5
        mnr_count.append(tmp)
    mnr_count.sort(key = lambda x: (-x[0], -x[1]))

    for i in mnr_count:
        if picks[0] > 0:
            picks[0] -= 1
            answer += sum(i)
        elif picks[1] > 0:
            picks[1] -= 1
            answer += i[0] * 5 + i[1] + i[2]
        elif picks[2] > 0:
            picks[2] -= 1
            answer += i[0] * 25 + i[1] * 5 + i[2]
        else:
            break
    return answer
