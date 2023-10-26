

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    num = ''

    while n:
        num += str(n % k)
        n //= k
    
    answer = 0

    num = num[::-1]
    print(num)

    for x in [int(_) for _ in num.split('0') if _ != '']:
        if is_prime(int(x)):
            answer += 1
    
    return answer


# print(solution(437674, 3))
print(solution(110011, 10))