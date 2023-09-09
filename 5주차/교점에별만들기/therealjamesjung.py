min_x = 100000000000
min_y = 100000000000
max_x = -100000000000
max_y = -100000000000

def get_intersection(line1, line2):
    global min_x, min_y, max_x, max_y

    try:
        x = ((line1[1] * line2[2]) - (line1[2] * line2[1])) / ((line1[0] * line2[1]) - (line1[1] * line2[0]))
        y = ((line1[2] * line2[0]) - (line1[0] * line2[2])) / ((line1[0] * line2[1]) - (line1[1] * line2[0]))
    except ZeroDivisionError:
        return None

    if x.is_integer() and y.is_integer():
        min_x = min(min_x, int(x))
        min_y = min(min_y, int(y))
        max_x = max(max_x, int(x))
        max_y = max(max_y, int(y))
        return (int(x), int(y))
    else:
        return None


def solution(line):
    points = set()

    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line[i][0] * line[j][1] - line[i][1] * line[j][0] == 0:
                continue
            point = get_intersection(line[i], line[j])
            if point:
                points.add(point)
    
    graph = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for point in points:
        graph[max_y - point[1]][point[0] - min_x] = '*'
    
    return [''.join(row) for row in graph]
