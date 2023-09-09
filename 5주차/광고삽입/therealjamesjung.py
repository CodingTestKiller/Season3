def time_to_sec(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def sec_to_time(sec):
    h = sec // 3600
    m = (sec - h * 3600) // 60
    s = sec - h * 3600 - m * 60

    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"


def solution(play_time, adv_time, logs):
    time_stamp = [0 for _ in range(360000)]

    total_play_time = time_to_sec(play_time)
    total_adv_time = time_to_sec(adv_time)

    for log in logs:
        start, end = log.split('-')
        start_sec = time_to_sec(start)
        end_sec = time_to_sec(end)

        time_stamp[start_sec] += 1
        time_stamp[end_sec] -= 1
    
    for i in range(1, total_play_time):
        time_stamp[i] += time_stamp[i - 1]

    
    start = 0
    end = total_adv_time
    max_time = sum(time_stamp[start:end])
    max_start = start

    current_time = max_time

    while end <= total_play_time:
        current_time -= time_stamp[start]
        current_time += time_stamp[end]

        if current_time > max_time:
            max_time = current_time
            max_start = start + 1
        
        start += 1
        end += 1
    
    return sec_to_time(max_start)





print(solution("02:03:55", "00:14:15", [
    "01:20:15-01:45:14",
    "00:40:31-01:00:00",
    "00:25:50-00:48:29",
    "01:30:59-01:53:29",
    "01:37:44-02:02:30"
    ]))