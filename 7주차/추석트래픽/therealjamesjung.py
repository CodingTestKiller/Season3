def time_to_milliseconds(time):
    h, m, s = time.split(':')
    
    result = 0
    result += int(h) * 3600 * 1000
    result += int(m) * 60 * 1000
    try:
        result += int(s.split('.')[0]) * 1000 + int(s.split('.')[1])
    except IndexError:
        result += int(s) * 1000
    
    return result

def format_miliseconds(ms):
    ms = ms[:-1]
    result = 0
    try:
        result += int(ms.split('.')[0]) * 1000 + int(ms.split('.')[1])
    except IndexError:
        result += int(ms) * 1000
    
    return result

def solution(lines):
    answer = 0
    start_times = []
    end_times = []

    for line in lines:
        date, time, duration = line.split(' ')
        end = time_to_milliseconds(time)
        start = end - format_miliseconds(duration) + 1

        start_times.append(start)
        end_times.append(end)

    
    for i in range(len(lines)):
        cnt = 0
        start = start_times[i]
        end = start + 1000

        for j in range(len(lines)):
            if start <= end_times[j] and  start_times[j] < end:
                cnt += 1

        # print(start, end, cnt)
        answer = max(answer, cnt)
    

    for i in range(len(lines)):
        cnt = 0
        start = end_times[i]
        end = start + 1000

        for j in range(len(lines)):
            if start <= end_times[j] and  start_times[j] < end:
                cnt += 1


        # print(start, end, cnt)
        answer = max(answer, cnt)


    return answer


lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]

print(solution(lines))