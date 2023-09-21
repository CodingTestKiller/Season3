def timecalc(T):
    H = int(T[:2]) * 3600
    M = int(T[3:5]) * 60
    S = int(T[6:8])
    MS = int(T[9:])
    return (H + M + S) * 1000 + MS

def start(T, duration):
    tmp = duration[:-1]
    duration = int(float(tmp) * 1000)
    return timecalc(T) - duration + 1

def solution(lines):
    answer = 0
    s = []
    e = []

    for t in lines:
        time = t.split(" ")
        s.append(start(time[1], time[2]))
        e.append(timecalc(time[1]))

    for i in range(len(lines)):
        cnt = 0
        cur = e[i]
        for j in range(i, len(lines)):
            if cur > s[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)

    return answer