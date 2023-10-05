import heapq

def solution(n, k, enemy):
    if len(enemy) <= k:
        return len(enemy)

    i = k
    heap = enemy[:k]
    heapq.heapify(heap)
    while n >= 0 and i < len(enemy):
        heapq.heappush(heap, enemy[i])
        n -= heapq.heappop(heap)
        i += 1

    if i == len(enemy) and n >= 0:
        i += 1

    return i - 1