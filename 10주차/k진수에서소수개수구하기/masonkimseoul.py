def is_prime_number(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    converted_digit = []
    while n > 0:
        converted_digit.append(n % k)
        n //= k

    converted_num = []
    tmp = 0
    while converted_digit:
        num = converted_digit.pop()

        if num != 0:
            tmp += num
            tmp *= 10
        else:
            tmp //= 10
            converted_num.append(tmp)
            tmp = 0

    converted_num.append(tmp // 10)
    for i in converted_num:
        if is_prime_number(i):
            answer += 1
    return answer

print(solution(437674, 3))