"""
공주 구하기(큐 자료구조로 해결)

왕국에는 왕자가 N명이 있다.

왕은 왕자들을 나이 순으로 1번부터 N번까지 차례로 번호를 매긴다.

1번부터 시계방향으로 돌아가며 동그랗게 앉게 한다.

그리고 1번 왕자부터 시계방향으로 돌아가며 1부터 시작하여 번호를 외치게 한다.

한 왕자가 K를 외치면 공주를 구하러 가야해서 원 밖으로 나간다.

다음 왕자부터 다시 1부터 시작해서 번호를 외친다.


마지막 남은 왕자의 번호는?
"""

import sys
sys.stdin=open("input.txt", "rt")

from collections import deque

n, k = map(int, input().split())

prince = []

for i in range(1, n +1):
   prince.append(i)


d_prices = deque(prince)

cnt = 0

while len(d_prices) > 1:
   
   if cnt < k-1:
        temp = d_prices.popleft()
        # print("다시 집어 넣는: "+str(temp))
        d_prices.append(temp)
        cnt +=1

   elif cnt == k -1:
       d_prices.popleft()
       cnt =0

print(d_prices[0])