import sys
sys.stdin=open("input.txt", "r") # 12315
s=input()
res=0
for x in s:
    if x.isdecimal(): # 들어오는 문자가 숫자이면
        res=res*10+int(x) # 1, 기존에 있는 값에 * 10을 하고 새로들어온 값 +x

print(res)


cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)