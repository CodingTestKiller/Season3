def solution(a):
    answer = 2

    left_array = [a[0]]
    right_array = [a[-1]]

    for i in range(1, len(a)):
        min_value = a[i] if left_array[-1] > a[i] else left_array[-1]
        left_array.append(min_value)

        min_value = a[- 1 - i] if right_array[-1] > a[- 1 - i] else right_array[-1]
        right_array.append(min_value)

    for i in range(1, len(a) - 1):
        if left_array[i - 1] > a[i] or right_array[-2 - i] > a[i]:
            answer += 1

    return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))