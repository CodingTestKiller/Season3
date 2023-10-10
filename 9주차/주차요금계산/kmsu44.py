# 11시 35분 시작
from collections import defaultdict
import math
def hourtomin(str):
    h,m = str.split(':')
    return int(h) * 60 + int(m)
    
    
def solution(fees, records):
    answer = []
    D = defaultdict(list)
    for record in records:
        time, number, case = record.split(' ')
        D[number].append((hourtomin(time),case))
        
    sub_answer = defaultdict(int)
    for number in D:
        last_time = hourtomin('23:59')
        while D[number]:
            cur_time,cur_case = D[number].pop()
            if cur_case == 'IN':
                sub_answer[number] += last_time-cur_time
            else:
                last_time = cur_time
    base_time, base_rate, unit, unit_fee = fees
    
    answer_list = []
    for number in sub_answer:
        if sub_answer[number] < base_time:
            answer_list.append((number,base_rate))
        else:
            sub_answer[number] -= base_time
            answer_list.append((number,math.ceil(sub_answer[number] / unit) * unit_fee + base_rate))    
    answer_list.sort(key=lambda x : x[0])
    for number,fee in answer_list:
        answer.append(fee)
        
    
    return answer