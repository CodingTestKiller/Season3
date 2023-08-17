def solution(commands):
    answer = []
    excel = [['EMPTY'] * 50 for _ in range(50)]
    merge_cell = [[[i, j] for j in range(50)] for i in range(50)]

    for cmd in commands:
        cmd = cmd.split(' ')

        if cmd[0] == 'UPDATE':
            if len(cmd) == 3:
                value1, value2 = cmd[1], cmd[2]
                for i in range(50):
                    for j in range(50):
                        if excel[i][j] == value1:
                            excel[i][j] = value2
            else:
                r, c, value = int(cmd[1]) - 1, int(cmd[2]) - 1, cmd[3]
                i, j = merge_cell[r][c]
                excel[i][j] = value

        elif cmd[0] == 'MERGE':
            r1, c1, r2, c2 = int(cmd[1]) - 1, int(cmd[2]) - 1, int(cmd[3]) - 1, int(cmd[4]) - 1
            x1, y1 = merge_cell[r1][c1]
            x2, y2 = merge_cell[r2][c2]

            if excel[x1][y1] == 'EMPTY':
                excel[x1][y1] = excel[x2][y2]

            for i in range(50):
                for j in range(50):
                    if merge_cell[i][j] == [x2, y2]:
                        merge_cell[i][j] = [x1, y1]

        elif cmd[0] == 'UNMERGE':
            r, c = int(cmd[1]) - 1, int(cmd[2]) - 1
            x, y = merge_cell[r][c]
            temp = excel[x][y]
            for i in range(50):
                for j in range(50):
                    if merge_cell[i][j] == [x, y]:
                        merge_cell[i][j] = [i, j]
                        excel[i][j] = 'EMPTY'
            excel[r][c] = temp

        elif cmd[0] == 'PRINT':
            r, c = int(cmd[1]) - 1, int(cmd[2]) - 1
            x, y = merge_cell[r][c]
            answer.append(excel[x][y])
    return answer

solution(["UPDATE 1 1 menu"])