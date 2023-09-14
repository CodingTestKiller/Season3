
def solution(s):
    answer = []
    for line in s:
        stack = []
        cnt_110 = 0
        for val in line:
            if(len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and val == '0'):
                cnt_110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(val)
            
            cnt_1 = 0
        for v in stack[::-1]:
            if v == '0':
                break
            else:
                cnt_1 += 1

        answer.append(''.join(stack[:len(stack)-cnt_1]) + '110' * cnt_110 + '1' * cnt_1)
            
                
            
        
    return answer