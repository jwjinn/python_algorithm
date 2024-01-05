import sys
sys.stdin=open("input.txt", "r")
a=list(range(21))
for _ in range(10):
    s, e=map(int, input().split()) # 5 10
    for i in range((e-s+1)//2): # 3 i가 0,1,2
        a[s+i], a[e-i]=a[e-i], a[s+i] # 3
a.pop(0)
for x in a:
    print(x, end=' ')

# 말그대로 대입해서 바꿔버리네.