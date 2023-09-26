# 수ㅐㅣ바 힙큐가 먼디

from collections import deque
import heapq

def solution(n, k, enemy):

    enemy_list = deque(enemy)
    defence_list = []

    if len(enemy_list) <= k:
        return len(enemy_list)

    answer = k
    for _ in range(k):
        en = enemy_list.popleft()   
        heapq.heappush(defence_list, en)

    kill_count = 0
    while enemy_list:
        en = enemy_list.popleft()
        tmp = heapq.heappop(defence_list)
        if tmp < en:
            heapq.heappush(defence_list, en)
            en = tmp
        else:
            heapq.heappush(defence_list, tmp)

        if kill_count + en > n:
            return answer
        kill_count += en
        answer +=1 

        
    return answer