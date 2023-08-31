from bisect import bisect


def solution(sequence, k):
    start = 0
    end = 0
    _sum = sequence[0]
    result = []

    sequence = sequence[:bisect(sequence, k)]

    while True:
        # print(start, end, _sum)
        try:
            if _sum < k:
                if result and end - start >= result[1] - result[0]:
                    _sum -= sequence[start]
                    start += 1
                else:
                    end += 1
                    _sum += sequence[end]    
            elif _sum > k:
                _sum -= sequence[start]
                start += 1

            if _sum == k:
                if not result:
                    result = [start, end]
                elif end - start < result[1] - result[0]:
                    result = [start, end]
                _sum -= sequence[start]
                start += 1
        except IndexError:
            break    
    
    return result
        


print(solution([1, 2, 3, 3, 3, 3, 3, 5], 3))