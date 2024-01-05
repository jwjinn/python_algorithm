import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())

for i in range(m):
    h, t, k=map(int, input().split())

    if t == 0: # 왼쪽으로 보내는 거
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

print(a)

s = 0
e = n
tot = 0

print(a[0][s:e])

for i in range(n):
    # print(sum(a[i][s:e]))
    tot += sum(a[i][s:e])

    if i < (n //2):
        s +=1
        e -=1
    else:
        s -=1
        e +=1

print(tot)