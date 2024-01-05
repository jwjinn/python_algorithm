import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res=0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)


"""
뭔가 규칙적인 리스트에서 시리얼하게 뽑아내는 것이 있으면 한번 두개의 포인터를 사용하는 것도 고려를 해봐야 한다.

"""