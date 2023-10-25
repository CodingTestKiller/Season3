def input_min(balloons):
        _min = []
        tmp = balloons[0]
        
        for b in balloons:
            if tmp > b:
                tmp = b
            _min.append(tmp)
            
        return _min
    
def solution(a):
    return len(set(input_min(a) + input_min(a[::-1])))