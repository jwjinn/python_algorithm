"""
응급실

• 환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자목록을 꺼냅니다.
• 나머지 대기 목록에서 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로 
 다시 넣습니다. 그렇지 않으면 진료를 받습니다.


즉, 꺼냈을 때, 나보다 위험도가 높은 사람이 없어야 한다.

"""

import sys
# sys.stdin=open("input.txt", "rt")

from collections import deque

n, m = map(int, input().split())
score = list(map(int, input().split()))

t_score = []

for i in range(0, n):
    t_score.append((i, score[i]))

# print(t_score)

d_score = deque(t_score)

cnt = 0

# print(max(d_score, key= lambda x : (x[1], x[0]))[1])

# 일단 leftpop을 하고 가장 크면 확인.
while True:
    temp = d_score.popleft()

    maxx = max(d_score, key= lambda x : (x[1], x[0]))[1]

    # print("left_pop된 내용물: ", end="")
    # print(temp)

    if int(temp[1]) > maxx:
        # 제일 우선순위가 높음.
        # print("우선순위가 높아서 나감 내용물: ", end="")
        # print(temp)
        cnt +=1

        

        if temp[0] == m:            
            # print(cnt)
            break

    elif int(temp[1]) < maxx:
        d_score.append(temp)

        

    elif int(temp[1]) == maxx:
            cnt +=1
            
            if temp[0] == m:
                print(cnt)
                break

    

