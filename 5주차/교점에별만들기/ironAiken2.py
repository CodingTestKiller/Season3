# Ax + By + E = 0
# Cx + Dy + F = 0
# x = BF - ED / AD - BC  |  y = EC - AF / AD - BC
def solution(line):
    ans = []
    
    for i in range(len(line)-1):
        for j in range(i+1,len(line)):
            parents = line[i][0] * line[j][1] - line[i][1] * line[j][0]
            if parents == 0:
                continue
            childs_x = line[i][1] * line[j][2] - line[i][2] * line[j][1]
            childs_y = line[i][2] * line[j][0] - line[i][0] * line[j][2]
            pos_x, pos_y = childs_x / parents, childs_y / parents
            if pos_x % 1 == 0 and pos_y % 1 == 0:
                ans.append([int(pos_x), int(pos_y)])

    ans.sort(key = lambda x : x[0])
    width = abs(ans[-1][0] - ans[0][0]) + 1
    if ans[0][0] < 0:
        moved = abs(ans[0][0])
    else:
        moved = -ans[0][0]
        
    ans.sort(key = lambda y: y[1])
    height = abs(ans[-1][1] - ans[0][1]) + 1
    print(height)
    
    dic = {}
    for i, data in enumerate(ans):
        ans[i][0] += moved
        try:
            dic[data[1]].append(data[0])
        except KeyError:
            dic[data[1]] = [data[0]]
            
    board = []
    for i in range(ans[-1][1], ans[0][1] -1, -1):
        row = ["." for _ in range(width)]
        try:
            for data in dic[i]:
                row[data] = "*"
            board.append(''.join(row))
        except KeyError:
            board.append(''.join(row))
    
    return board
                