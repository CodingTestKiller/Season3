import math
def numberic(n,k):
    res = ''
    while n > 0:
        n,mod = divmod(n,k)
        res+=str(mod)
    return res[::-1]

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
def solution(n, k):
    # 소수판별 에라토스테네스의 체
    n = n * k 
    primes = [True for _ in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]:
            for j in range(2*i, n+1, i):
                primes[j] = False
    
    string = numberic(n,k)
    cnt = 0
    
    for num in string.split('0'):
        if(num == '1' or num== ''):
            continue
        if(is_prime_number(int(num))):
            cnt+=1
            
        
    
    return cnt