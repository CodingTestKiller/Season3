## a) positions를 돌면서 체크 함 -> 6번, 7번 시간초과
## b) 생각해보니 돌면서 체크를 할 필요가 없음. 마지막 거와만 비교하면 댐

positions = []

def solution(targets: list):
    targets.sort()
    positions.append(targets[0])

    for target in targets[1:]:
        if isAttackPossible(target):
            continue
        else:
            positions.append(target)
    return len(positions)

def isAttackPossible(target):
    idx = len(positions)-1
    position = positions[idx]
    if position[1] <= target[0] or target[1] <= position[0]:
        return False
    elif position[0] <= target[0] and target[1] <= position[1]:
        positions[idx][0] = target[0]
        positions[idx][1] = target[1]
        return True
    elif position[0] <= target[0]:
        positions[idx][0] = target[0]
        return True
    elif target[1] <= position[1]:
        positions[idx][1] = target[1]
        return True
    elif target[0] <= position[0] and position[1] <= target[1]:
        return True