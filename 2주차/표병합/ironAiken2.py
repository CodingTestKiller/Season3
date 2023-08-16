parent = [[(r, c) for c in range(51)] for r in range(51)]
cells = [['EMPTY']*51 for _ in range(51)]
result = []

def find(r, c) :
    if (r, c) == parent[r][c] :
        return parent[r][c]
    pr, pc = parent[r][c]
    parent[r][c] = find(pr, pc)
    return parent[r][c]

def union(r1, c1, r2, c2) :
    parent[r2][c2] = parent[r1][c1]

def UPDATE(r, c, msg) :
    pr, pc = find(r, c) 
    cells[pr][pc] = msg

def UPDATE_VAL(msg1, msg2):
    for r in range(51) :
        for c in range(51) :
            pr, pc = find(r, c)
            if cells[pr][pc] == msg1 :
                cells[pr][pc] = msg2
    
def MERGE(r1, c1, r2, c2) :
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)
    
    if (r1, c1) == (r2, c2) :
        return
    if cells[r1][c1] != "EMPTY" :
        union(r1, c1, r2, c2)
    else :
        union(r2, c2, r1, c1)

def UNMERGE(r, c):
    pr, pc = find(r, c)
    msg = cells[pr][pc]
      
    merge_list = list()
    for ar in range(51) :
        for ac in range(51) :
            apr, apc = find(ar, ac)
            if (apr, apc) == (pr, pc) :
                merge_list.append((ar, ac))
                
    for ar, ac in merge_list :
        parent[ar][ac] = (ar, ac)
        cells[ar][ac] = "EMPTY" if (ar, ac) != (r, c) else msg
    
def PRINT(r, c) :
    pr, pc = find(r, c)
    result.append(cells[pr][pc])
        
def solution(commands):
    for command in commands :
        cmd, *arg = command.split()
        if cmd == "UPDATE" :
            if len(arg) == 3 :
                r, c, value = arg
                UPDATE(int(r), int(c), value)
            else :
                value1, value2 = arg
                UPDATE_VAL(value1, value2)
        elif cmd == "MERGE" :
            r1, c1, r2, c2 = map(int, arg)
            MERGE(r1, c1, r2, c2)
        elif cmd == "UNMERGE" :
            r, c = map(int, arg)
            UNMERGE(r, c)
        else :
            r, c = map(int, arg)
            PRINT(r, c)
            
    return result

# 빡구현 하다가 포기
# import sys
# sys.setrecursionlimit(10**9)

# check = [[False for _ in range(51)] for _ in range(51)]
# def search_field(graph, val1, val2):
#     for i in range(51):
#         for j in range(51):
#             if graph[i][j] == []:
#                 continue
#             if graph[i][j][0] == val1:
#                 graph[i][j][0] = val2
# def renew(graph, child, value):
#     global check
    
#     for data in child:
#         i, j = int(data[0]), int(data[1])
#         if check[i][j] == True:
#             continue
#         graph[i][j][0] = value
#         renew(graph, graph[i][j][1], value)
    
# def functions(graph, cmd, answer):
#     if cmd[0] == 'UPDATE':
#         if len(cmd) == 4:
#             print(cmd[3])
#             i, j = int(cmd[1]), int(cmd[2])
#             graph[i][j][0] = cmd[3]
#             renew(graph, graph[i][j][1], cmd[3])
#         else:
#             search_field(graph, cmd[1], cmd[2])
#     elif cmd[0] == 'MERGE':
#         r1, c1, r2, c2 = int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4])
#         graph[r1][c1][1].append([r2,c2])
#         graph[r2][c2][1].append([r1,c1])
#         if graph[r1][c1][0] == "EMPTY":
#             graph[r1][c1][0] = graph[r2][c2][0]
#         else:
#             graph[r2][c2][0] = graph[r1][c1][0]
        
#     elif cmd[0] == 'UNMERGE':
#         pass
#     elif cmd[0] == 'PRINT':
#         r, c = int(cmd[1]), int(cmd[2])
#         answer.append(graph[r][c][0])
    
# def solution(commands):
#     global check
#     graph = [[['EMPTY', []] for _ in range(51)] for _ in range(51)]
#     answer = []
    
#     for command in commands:
#         cmd = command.split(' ')
#         functions(graph, cmd, answer)
#         check = [[False for _ in range(51)] for _ in range(51)]
    
#     return answer