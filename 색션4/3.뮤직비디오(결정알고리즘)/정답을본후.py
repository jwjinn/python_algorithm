import sys
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
music = list(map(int, input().split()))

lt = 1
rt = sum(music) # DVD의 최대 용량은 모든 곡이 다 들어가는 경우이다.

# 용량에 맞는 곳을 순서대로 집어넣는다. 이 용량으로 몇개의 DVD가 필요한가?
def Cal(capacity):

    total = 0
    cnt = 1

    for x in music:
        # 용량 초과일 경우에는 DVD수를 늘리고 현재 용량을 초기화해야 한다.
        if total + x > capacity:
            cnt +=1
            total = x # 이것까지는 넣어야지 DVD를 추가했으니
        else:
            total +=x

    return cnt

maxx = max(music)            

res = 0

while lt <= rt:
    mid = (lt + rt) //2

    # DVD수가 목표한 갯수보다 작거나 같으면
    # 최대한 작은 DVD 용량을 찾는 것이기에 그 이상을 살펴볼 이유는 없다.
    if mid >=maxx and Cal(mid) <= m:
        res = mid # 작은 곳에서 살피는 것이기에 더 있다면 그 용량이 최소용량이다.
        rt = mid -1

    else: # 오히려 갯수가 많아... 그러면 용량을 늘려야지. mid가 높도록
        lt = mid + 1

print(res)
