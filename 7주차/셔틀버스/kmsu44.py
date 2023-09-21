from collections import deque
def strtoint(str):
    h,m = str.split(':')
    return int(h) *60 + int(m)
def inttostr(int):
    h = int//60
    m = int % 60
    str = '%02d:%02d' % (h,m)
    return str
    
    
def solution(n, t, m, timetable):
    answer = ''
    bus_table = deque([])
    bus_time = 540
    for i in range(n):
        bus_table.append(bus_time)
        bus_time += t
    
    time_user = [0 for _ in range(1440)]
    timetable.sort()
    
    # 시간별 유저 수 구하기
    for i in timetable:
        time = strtoint(i)
        time_user[time] +=1
    prev_time = 0
    remain_crew = deque()
    can = 0
    bus_cnt = 0
    for bus_time in bus_table:
        for time in range(prev_time,bus_time+1):
            if time_user[time] !=0:
                for _ in range(time_user[time]):
                    remain_crew.append(time)
            if len(remain_crew) < m:
                can = max(can, time)
        bus_cnt +=1
        # print(inttostr(bus_time),len(remain_crew),inttostr(can),bus_cnt)
        if len(remain_crew) < m:
            remain_crew = deque()
        else:
            for _ in range(m):
                lastcrew = remain_crew.popleft()
                can= max(can,lastcrew-1)
                
        prev_time = bus_time+1
    
    answer = inttostr(can)
    
    
    
    return answer