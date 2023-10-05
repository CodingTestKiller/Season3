from heapq import heappush, heappop

def solution(n, k, enemy):
    heap = []
    
    for i in range(len(enemy)):
        heappush(heap, enemy[i])
        if len(heap) > k:
            n -= heappop(heap)
            if n < 0:
                return i
                
    return len(enemy)