
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
class Node :
    def __init__(self,left = None,right = None):
        self.remove = False
        self.left = left
        self.right = right
def solution(n, k, cmd):
    # linked -list
    table = [Node(i-1,i+1) for i in range(n)]
    table[0].left= None
    table[n - 1].right = None
    cursor = k
    stack = []
    for i in cmd:
        if i[0] == 'U':
            pos, move = i.split()
            for _ in range(int(move)):
                cursor = table[cursor].left
        elif i[0] == 'D':
            pos,move = i.split()
            for _ in range(int(move)):
                cursor = table[cursor].right
        elif i[0] == 'C':
            stack.append(cursor)
            table[cursor].remove = True

            l,r = table[cursor].left , table[cursor].right

            if l or l == 0:
                table[l].right = r
            # 마지막행이면
            if r:
                table[r].left = l
                cursor = r
            else:
                cursor = l
        else:
            c = stack.pop()
            table[c].remove = False

            l,r = table[c].left,table[c].right
            # 복원된 행이 첫째행이아니라면
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
