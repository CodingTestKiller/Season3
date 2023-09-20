from collections import deque

def solution(n, t, m, timetable):
    
    timetable.sort()
    time_table = deque([convert_to_time(time) for time in timetable])
    bustime = [60*9]
    for _ in range(n-1):
        bustime.append(bustime[-1]+t)   
    bus_time = deque(bustime)

    real_bus = []
    while time_table and bus_time:
        tmp = []
        bus = bus_time.popleft()
        count = 0
        while count < m:
            try:
                person = time_table.popleft()
            except:
                break    
            if person > bus:
                time_table.appendleft(person)
                break
            tmp.append(person)
            count += 1
        real_bus.append(tmp)

    if len(bus_time) != 0:
        return convert_to_string(bustime[-1])

    if len(real_bus[-1]) == m:
        return convert_to_string(real_bus[-1][-1]-1)
    else :
        return convert_to_string(bustime[-1])


def convert_to_time(time: str):
    h, m = list(map(int,time.split(':')))
    return h*60 + m

def convert_to_string(time: int):
    h, m = time//60, time%60
    return format(h, '02')+':'+format(m, '02')