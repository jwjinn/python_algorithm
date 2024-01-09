"""
침몰하는 타이타닉(그리디)

유람선에는 N명의 승객이 타고 있습니다.

타이타닉의 구명보트는 2명 이하로만 탈 수 있습니다.
보트 한 개에 탈 수 있는 총 무게도 M KG 이하입니다.

N명의 승객 몸무개가 주어졌을때, 승객 모두가 탈출하기 위한 구명보트의 최소개수는?

"""

"""
큰 몸무개와 작은 몸무개를 짝지는 느낌으로 진행해야 할듯.

"""

import sys
sys.stdin=open("input.txt", "r")

n, limit = map(int, input().split())

weights = list(map(int, input().split()))
weights.sort()

print(weights)

cnt = 0
# lenn = len(weights)

while len(weights) >0:

    lenn = len(weights)

    if weights[lenn-1] + weights[0] <= limit:
        print(weights[lenn-1])
        print(weights[0])
        weights.pop(lenn-1)
        weights.pop(0)

        cnt +=1


    else:
        print(weights[lenn-1])
        weights.pop(lenn-1)
        cnt +=1
        
    print()

print(cnt)