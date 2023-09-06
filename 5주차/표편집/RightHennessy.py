class Node :
    def __init__(self,left = None,right = None):
        self.remove = False
        self.left = left
        self.right = right

def solution(n, k, cmd):
    table = [Node(i-1,i+1) for i in range(n)]
    table[0].left= None
    table[n - 1].right = None
    cursor = k
    stack = []
    for command in cmd:
        if command[0] == 'U':
            move = command.split()[1]
            for _ in range(int(move)):
                cursor = table[cursor].left
        elif command[0] == 'D':
            move = command.split()[1]
            for _ in range(int(move)):
                cursor = table[cursor].right
        elif command[0] == 'C':
            stack.append(cursor)
            table[cursor].remove = True

            l,r = table[cursor].left , table[cursor].right

            if l or l == 0:
                table[l].right = r
            if r:
                table[r].left = l
                cursor = r
            else:
                cursor = l
        elif command[0] == 'Z':
            c = stack.pop()
            table[c].remove = False

            l,r = table[c].left,table[c].right
            if l:
                table[l].right =c
            if r:
                table[r].left = c

    answer = ""
    for i in range(n):
        if table[i].remove :
            answer += "X"
        else:
            answer += "O"
    return answer