# 1/4 을 구해보자
## a) 좌표를 모두 찍은 다음 원 사이에 존재하는지 확인
## b) 원 사이에 존재하는 점만 확인 - 이중 for문
## c) x좌표 찍고 y좌표 갯수 

import math

def solution(r1, r2):
    answer = countDots(r1, r2)
    return answer*4

def countDots(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        answer += maximum(i, r2)+1 - minimum(i, r1)
    return answer

def minimum(i, r):
    value = r**2-i**2
    if value <= 0: return 0
    return int(math.ceil(math.sqrt(value)))

def maximum(i, r):
    return int(math.sqrt(r**2-i**2))