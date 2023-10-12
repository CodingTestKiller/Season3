# 20m
import math


def time_to_min(time):
    h, m = [int(x) for x in time.split(':')]
    return h*60+m


def solution(fees, records):
    answer = []
    parking_lot = {}
    cars = {}
    
    min_time, min_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
    
    for record in records:
        timestamp, car, action = record.split()
        
        if car in parking_lot:
            parked_time = time_to_min(timestamp) - parking_lot[car]
            if car in cars:
                cars[car] += parked_time
            else:
                cars[car] = parked_time
            del parking_lot[car]
        else:
            parking_lot[car] = time_to_min(timestamp)
    
    end_time = time_to_min('23:59')
    
    for car, time in parking_lot.items():
        parked_time = end_time - time
        if car in cars:
            cars[car] += parked_time
        else:
            cars[car] = parked_time
    

    for car, time in sorted(cars.items()):
        # print(car, time)
        fee = 0
        if time > min_time:
            fee += min_fee
            fee += math.ceil((time - min_time) / unit_time) * unit_fee
        else:
            fee = min_fee
        answer.append(fee)
        
    
    return answer