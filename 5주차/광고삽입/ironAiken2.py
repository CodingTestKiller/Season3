from collections import defaultdict

def convert_to_second(string):
    hour, minute, second = string.split(":")
    total = int(hour) * 60 * 60 + int(minute)*60 + int(second)
    
    return total
def solution(play_time, adv_time, logs):
    play_time = convert_to_second(play_time)
    adv_time = convert_to_second(adv_time)
    
    for i, data in enumerate(logs):
        start, end = data.split("-")
        logs[i] = [convert_to_second(start), convert_to_second(end)]
    logs.sort(key = lambda x : x[0])

    if play_time <= adv_time:
        return "00:00:00"
    
    timeline = [0 for _ in range(100 * 3600)]
    
    for data in logs:
        timeline[data[0]] += 1
        timeline[data[1]] -= 1
    
    for i in range(1, len(timeline)):
        timeline[i] += timeline[i-1]
        
    start, end = 0, adv_time
    ans = sum(timeline[start:end+1])
    ans_start = start
    current = ans
    while end < len(timeline) - 1:
        start += 1
        end += 1
        current -= timeline[start]
        current += timeline[end]
        if current > ans:
            ans = current
            ans_start = start+1
    
    adv_start_time = ans_start
    hour = adv_start_time // 3600
    hour = "0" + str(hour) if hour < 10 else str(hour)
    adv_start_time %= 3600
    minute = adv_start_time // 60
    minute = "0" + str(minute) if minute < 10 else str(minute)
    adv_start_time %= 60
    second = adv_start_time
    second = "0" + str(second) if second < 10 else str(second)
    
    return hour + ":" + minute + ":" + second


# from collections import defaultdict

# def convert_to_second(string):
#     hour, minute, second = string.split(":")
#     total = int(hour) * 60 * 60 + int(minute)*60 + int(second)
    
#     return total
# def solution(play_time, adv_time, logs):
#     play_time = convert_to_second(play_time)
#     adv_time = convert_to_second(adv_time)
    
#     for i, data in enumerate(logs):
#         start, end = data.split("-")
#         logs[i] = [convert_to_second(start), convert_to_second(end)]
#     logs.sort(key = lambda x : x[0])
    
#     if play_time <= adv_time:
#         return "00:00:00"
    
#     start = defaultdict(int)
#     end = defaultdict(int)
#     for data in logs:
#         start[data[0]] += 1
#         end[data[1]] += 1
    
#     flag = 0
#     timeline = []
#     start_time = 0
    
#     # 각 구간 별 계산
#     for i in range(play_time + 1):
#         if start[i]:
#             timeline.append([i-1, flag])
#             flag += 1
#         else:
#             del start[i]
            
#         if end[i]:
#             timeline.append([i, flag])
#             flag -= 1
#         else:
#             del end[i]
    
#     #시청기간내 광고 삽입시 최대 시청기간 정리
#     total_timeline = []
#     start_time = 0
#     for i, data in enumerate(timeline):
#         if i == 0:
#             total_timeline.append([data[0], 0])
#             continue
#         total_time = 0
#         adv_start = data[0] - adv_time
#         start_time = timeline[i-1][0] + 1
#         if adv_start < start_time:
#             total_time = (data[0] - start_time) * data[1]
#             for j in range(i-1, -1, -1):
#                 try:
#                     start_time = timeline[j-1][0] + 1
#                     if adv_start < start_time:
#                         total_time += (timeline[j][0] - start_time) * timeline[j][1]
#                     else:
#                         total_time += (timeline[j][0] - adv_start) * timeline[j][1]
#                         break
#                 except IndexError:
#                     total_time += (timeline[j][0] - adv_start) * timeline[j][1]
#                     break
#             total_timeline.append([data[0], total_time])
#         else:
#             total_timeline.append([data[0], (data[0] - adv_start) * data[1]])
    
#     total_timeline.sort(key = lambda x : x[0], reverse = True)
#     total_timeline.sort(key = lambda x : x[1])
    
#     adv_end_time = total_timeline[-1][0]
#     if adv_end_time - adv_time < 0:
#         adv_start_time = 0
#         for data in logs:
#             if data[1] == adv_end_time:
#                 adv_start_time = data[0]
#     else:
#         adv_start_time = adv_end_time - adv_time
        
#     hour = adv_start_time // 3600
#     hour = "0" + str(hour) if hour < 10 else str(hour)
#     adv_start_time %= 3600
#     minute = adv_start_time // 60
#     minute = "0" + str(minute) if minute < 10 else str(minute)
#     adv_start_time %= 60
#     second = adv_start_time
#     second = "0" + str(second) if second < 10 else str(second)
    
#     return hour + ":" + minute + ":" + second
        
