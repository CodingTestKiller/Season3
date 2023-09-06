convertor = [60*60, 60, 1]

def solution(play_time, adv_time, logs):

    play_time = list(map(int, play_time.split(':')))
    play_time = sum(convertor[i]*play_time[i] for i in range(3))

    adv_time = list(map(int, adv_time.split(':')))
    adv_time = sum(convertor[i]*adv_time[i] for i in range(3))

    log_time = []
    for log in logs:
        start, end = [list(map(int, time.split(':'))) for time in log.split('-')]
        start_time = sum(convertor[i]*start[i] for i in range(3))
        end_time = sum(convertor[i]*end[i] for i in range(3))
        log_time.append([start_time, end_time])

    time_line = [0]*(play_time + 1)
    for log in log_time:
        start, end = log
        time_line[start] += 1
        time_line[end] -= 1

    # 시간대 별 누적 사용자 수
    for i in range(1, len(time_line)):
        time_line[i] += time_line[i-1]
    # 누적합
    for i in range(1, len(time_line)):
        time_line[i] += time_line[i-1]

    max_count = 0
    answer_time = 0
    for i in range(0, play_time - adv_time):
        count = time_line[i + adv_time] - time_line[i]
        if count > max_count:
            max_count = count
            answer_time = i

    answer = []
    if answer_time != 0:
        answer_time += 1
    for i in range(3):
        answer.append(format(answer_time//convertor[i], '02'))
        answer_time %= convertor[i]

    return ':'.join(list(map(str, answer)))
