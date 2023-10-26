import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def primality(n):
    if n == 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    
def solution(n, k):
    n = str(convert(n, k))
    arr = n.split('0')
    arr = [i for i in arr if i != '']
    ans = 0
    
    for num in arr:
        ans += 1 if primality(int(num)) else 0
    
    return ans