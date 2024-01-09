"""
씨름 선수

N명의 지원자가 지원을 했습니다.

"다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나,
무거운 지원자만 뽑기로 했습니다."

A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재하면 A지원자는 탈락

"""

import sys
sys.stdin=open("input.txt", "r")

n = int(input())

information = []

for i in range(n):
    h, w = map(int, input().split())

    information.append((h, w))


information.sort(key = lambda x : (x[0], x[1]))
# 키순으로 생각했을때 뒤에 있는 키작은 사람은 비교할 필요가 없다.
# 단지 몸무게만 보면 됨.

cnt = 0

for i in range(n-1):
    # print(information[i])

    temp = []

    for j in range(i+1, n):
        # print(information[j][1])
        temp.append(information[j][1])

    # print(temp)
    # print(max(temp))
    
    if information[i][1] > max(temp):
        print(information[i])
        print("SELECT") # 키가 가장 큰 사람은 그냥 +1하면 됨.
        cnt +=1

print(cnt+1)


