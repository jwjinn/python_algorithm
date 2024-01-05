"""
리스트 내에서 연속적인 무엇인가를 도출해야 할 경우.
lt, rt를 활용하자.
"""


import sys
sys.stdin = open("input.txt", 'r')
n, m=map(int, input().split()) # 수의 갯수, 맞춰야 하는 숫자
a=list(map(int, input().split()))

tot = a[0]
lt = 0
rt = 1
count = 0

while True:
    if tot < m:
        if rt < n:
            tot +=a[rt]
            rt +=1
        else:
            break
    elif tot == m:
        count +=1
        tot -=a[lt]
        lt +=1

    else:
        tot -=a[lt]
        lt +=1

print(count)
