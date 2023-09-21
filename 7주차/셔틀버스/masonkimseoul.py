def timecalc(T):
    H, M = T.split(':')
    return int(H) * 60 + int(M)

def solution(n, t, m, timetable):
    answer = 0

    crew = []
    for i in timetable:
        crew.append(timecalc(i))
    crew.sort()

    bus_arrival = []
    for i in range(n):
        bus_arrival.append(540 + i * t)

    idx = 0
    for bus in bus_arrival:
        cnt = 0
        while idx < len(crew) and crew[idx] <= bus and cnt < m:
            idx += 1
            cnt += 1

        if cnt < m:
            answer = bus
        else:
            answer = crew[idx - 1] - 1

    hour = answer // 60
    minute = answer % 60
    
    return '%02d:%02d' % (hour, minute)