# 단순 노동 구현.. 하기 싫어 죽는 줄

from collections import deque
import math

def solution(fees, records):
    default_time, default_price, unit_time, unit_price = fees
    cars = dict()
    answer = []

    for record in records:
        time, car, state = record.split(' ')
        try:
            cars[int(car)].append([time, state])
        except: 
            cars[int(car)] = [[time, state]]

    for key in cars.keys():
        if cars[key][-1][1] == 'IN':
            cars[key].append(['23:59', 'OUT'])

        history = deque(cars[key])
        sum_time = 0
        while history:
            in_history = convert_to_time(history.popleft()[0])
            out_history = convert_to_time(history.popleft()[0])
            sum_time += (out_history - in_history)

        price = default_price
        sum_time -= default_time
        if sum_time > 0:
            price += unit_price*math.ceil(sum_time/unit_time)
        answer.append([key, price])

    answer.sort()
    answer = [x[1] for x in answer]

    return answer

def convert_to_time(s: str):
    h, m  = list(map(int, s.split(':')))
    return h*60+m