import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))

"""
사고 방식은 매우 간단함. 1차원 배열의 좌우에서 선택을 하기에 포인터를 2개를 생각할 필요가 있었음.
"""

lt = 0
rt = n - 1
last = 0

res = ""
tmp = []

while lt <= rt:

    # 일단 왼쪽이든, 오른쪽이든 둘다 받고
    if a[lt] > last:
        tmp.append((a[lt], "L"))
    
    if a[rt] > last:
        tmp.append((a[rt], "R"))

    tmp.sort() # 오름차순으로 정렬한 다음

    if len(tmp) == 0: # 만약 아무것도 tmp에 들어있지 않다면 last보다 다 작다는 의미이므로 반복문을 중지시킨다.
        break

    else:
        # 정렬이 되었으니, 제일 작은 것만 뽑고 포인터를 옮긴다.
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == "L":
            lt = lt+1
        else:
            rt = rt - 1

    tmp.clear()

