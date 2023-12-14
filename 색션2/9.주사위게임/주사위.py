"""
주사위 게임

1에서부터 6까지의 눈을 가진 주사위, 3개를 던진다.

규칙(1): 같은 눈이 3개가 나오면 10,000 + (같은 눈) * 1000
(2): 같은 눈이 2개: 1000 + (같은 눈)*100
(3): 모두 다른 눈: 가장 큰 눈* 100

사람이 던져서 나온 주사위에서 가장 상금을 많이 탄 금액만 출력해라. 

"""

import sys
sys.stdin=open("input.txt", "r")
N = int(input())
dice = [0] * N

def check_same(x):

    count = 0
    same_number=0

    # print(dice[x])

    if dice[x][0] == dice [x][1]:
        # print("1,2 같음")
        count +=1
        same_number = dice[x][0]
    if dice[x][0] == dice[x][2]:
        # print("1, 3 같음")
        count +=1
        same_number = dice[x][0]
    if dice[x][1] == dice[x][2]:
        # print("2,3 같음")
        count +=1
        same_number = dice[x][1]

    if count ==1:
        count+=1

    if same_number == 0:
        same_number = max(dice[x])
    # print(count)
    return count, same_number

money = []

for i in range(0, N):
    dice[i] = list(map(int, input().split()))
    # print(check_same(i))

    count, point = check_same(i)

    if count == 3:
        money.append(10000 + point * 1000)
    elif count == 2:
        money.append(1000 + point * 100)
    elif count == 0:
        money.append(point * 100)

print(max(money))

    

 











