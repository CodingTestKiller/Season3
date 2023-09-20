from collections import deque


def minutes_to_time(minutes):
    return str(minutes // 60).zfill(2) + ":" + str(minutes % 60).zfill(2)


def solution(n, t, m, timetable):
    answer = ''
    _timetable = []

    for time in timetable:
        _h, _m = time.split(':')
        _timetable.append(int(_h) * 60 + int(_m))
    
    _timetable = deque(sorted(_timetable))

    bus_times = [540 + t * i for i in range(n)]

    for bus_time in bus_times[:-1]:
        if n == 1:
            break
        for _ in range(m):
            if _timetable and _timetable[0] <= bus_time:
                _timetable.popleft()
            else:
                break
        n -= 1
    
    if not _timetable:
        answer = bus_times[-1]
    else:
        if len(_timetable) < m:
            answer = bus_times[-1]
        elif _timetable[m - 1] > bus_times[-1]:
            answer = bus_times[-1]
        else:
            answer = _timetable[m - 1] - 1

    return minutes_to_time(answer)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))