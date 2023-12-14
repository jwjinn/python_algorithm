import sys
sys.stdin=open("input.txt", "r")

N = int(input())

a = list(map(int, input().split()))

ave = round(sum(a) / N)

min = 21402032

for idx, x in enumerate(a):
    tmp = abs(x - ave) # 루프문을 돌면서 각각의 점수와 평균의 거리를 측정
    if tmp < min: # 그래서 현재 거리가 더 작으면
        min = tmp # 거리 점수, 점수, 위치를 바꾼다.
        score = x
        res = idx + 1

    elif tmp == min: # 만약에 거리가 같고
        if x > score: # 점수가 더 크면
            score = x
            res = idx + 1

# 앞에서 부터 가는 것이기에 점수가 같아도 업데이트를 하지 않아야
# 더 작은 번호를 가진 사람이 그대로 유지된다.

print(ave, res)

    
