import sys
sys.stdin=open("input.txt", "r")
s=input()
stack=[]
cnt=0
for i in range(len(s)):

    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(': # 앞의 값이 (먄 - 살펴보는 대상은 원본 리스트임.
            cnt+=len(stack)
        else:
            cnt+=1
print(cnt)