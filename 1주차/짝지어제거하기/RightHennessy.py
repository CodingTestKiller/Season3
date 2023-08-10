
def solution(s):
    myList = list(s)

    stack = []

    for x in myList :
        if len(stack) == 0 :
            stack.append(x)
        elif stack[-1] == x :
            stack.pop()
        else :
            stack.append(x)
    
    if len(stack) == 0 :
        return 1
    
    return 0