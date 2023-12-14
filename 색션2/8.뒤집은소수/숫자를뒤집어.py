def reverse(x):
    res=0
    while x>0: # 1234
        t=x%10 # 4, 3, 2
        res=res*10+t # 4, 43, 432
        print(res)
        x=x//10 # 123, 12
        # print(x)
    return res

print(reverse(1234))

# 나머지와 곱셈.


