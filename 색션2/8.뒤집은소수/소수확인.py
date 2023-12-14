def isPrime(x):
    if x==1:
        return False
    for i in range(2, x):
        if x%i==0:
            return False
    return True

# 간단하게 나누어떨어지는 것이 있는가?
# 있으면 소수다.