# 8시 52분 시작
import heapq
def solution(n, k, enemy):
    answer = 0
    q = []
    for e_num in enemy:
        # 적의 수가 남은 수보다 많을 때
        if n < e_num:
            # 무적권이 없는 경우
            if k <= 0:
                break
                
            # 무적권이 남은 경우
            # 죽은병사들이 없을 경우
            revive = 0
            # 죽은 병사들이 있을 경우
            if q:
                revive = heapq.heappop(q) * -1
            k-=1
            # 부활한 병사 < 현재 라운드 병사 -> 현재라운드에 무적권 사용
            if revive < e_num:
                heapq.heappush(q,-revive)
            # 부활한 병사 >= 현재 라운드 병사 -> 이전 라운드에 무적권 사용
            else:
                heapq.heappush(q,-e_num)
                n += revive
                n -= e_num
        #적의 수가 적을 때
        else:
            heapq.heappush(q,-e_num)
            n-=e_num
        answer +=1
        
        # print('q', q, 'n', n, 'enemy', e_num)
        
        
    
            
        
        
    return answer