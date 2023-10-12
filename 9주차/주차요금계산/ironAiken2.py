from collections import defaultdict
import math

def conversion(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

def solution(fees, records):
    dict = defaultdict(int)
    # 정렬
    for i, record in enumerate(records):
        time, num, come_and_go = record.split(' ')
        time = conversion(time)
        records[i] = [time, num, come_and_go]
    records.sort(key=lambda x:x[1])    
    # 시간계산
    for i in range(len(records)):
        if records[i][2] == 'OUT':
            continue
        try:
            if records[i+1][2] != 'OUT':
                dict[records[i][1]] += 1439 - records[i][0]
            else:
                dict[records[i][1]] += records[i+1][0] - records[i][0]
        except IndexError:
            dict[records[i][1]] += 1439 - records[i][0]
    # 요금계산
    ans = []
    for key in dict:
        if dict[key] <= fees[0]:
            ans.append(fees[1])
        else:
            ans.append(fees[1] + (math.ceil((dict[key] - fees[0]) / fees[2])) * fees[3])
                       
    return ans