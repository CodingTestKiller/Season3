# 누적합에 너무 집착하지 말자 ...

partial = [0]

def solution(sequence, k):
    answer = []
    
    for s in sequence:
        partial.append(s+partial[-1])
   
    i, j, size = 0, 1, len(partial)
    while j<size:
        if partial[j]-partial[i] < k:
            j += 1
        elif partial[j]-partial[i] > k:
            i += 1
        else:
            if not answer:
                answer = [i, j]
            if answer[1]-answer[0] > j-1-i:
                answer = [i,j-1]
            j += 1
        
    return answer