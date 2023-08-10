def solution(s):    
    while True:
        remain = []
        
        for data in s:
            if remain and remain[-1] == data:
                remain.pop()
            else:
                remain.append(data)
                
        if remain:
            return 0
        else:
            return 1