def solution(s):
    loop_count, total_zero = 0, 0
    
    while len(s) != 1:
        one_count, zero_count = 0, 0
        loop_count += 1
        
        for data in s:
            if data == "1":
                one_count += 1
            elif data == "0":
                zero_count += 1
        
        total_zero += zero_count
        s = format(one_count, 'b')
                
        
            
    answer = [loop_count, total_zero]
    return answer