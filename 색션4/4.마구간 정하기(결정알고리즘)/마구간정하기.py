"""
마구간 정하기

x1, x2, x3, ----- , xN

현수는 C마리의 말을 가지고 있습니다.
두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다.

가장 가까운 두 말의 거리가 최대가 되는 거리의 최대값을 구해라.

5 3
1
2
8
4
9


정답
3

"""

"""
정답을 본 후, 문제는 무엇을 최소값으로 설정을 할지, 최대값으로 설정을 할 지 감을 잡지 못했다는 점이다.

수직선상에서의 최소, 최대값을 설정하는 것에만 집중을 하자.

"""

import sys
sys.stdin=open("input.txt", "r")

n,c = map(int, input().split())

horseLocation = []

for _ in range(n):
    horseLocation.append(int(input()))

horseLocation.sort()

lt = horseLocation[0]
rt = horseLocation[n-1]

# 이 간격으로 다 들어가는가? 리턴되는 값은 들어갈 수 있는 마구간의 수
def setHorse(interval):
    start = horseLocation[0]

    cnt = 1

    for i in range(1, len(horseLocation)):
        # print(horseLocation[i])
        if horseLocation[i] - start >= interval:
            start = horseLocation[i]
            cnt +=1

    # print("cnt: "+str(cnt))

    return cnt


# setHorse(3)        

res = 0

while lt <=rt:

    mid = (lt + rt) // 2

    # print(mid)
    if setHorse(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid -1
    
print(res)