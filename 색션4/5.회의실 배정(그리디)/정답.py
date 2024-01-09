"""
5. 회의실 배정(그리드)

그리드 알고리즘은 결정적으로 어떻게 정렬을 할건지만 생각을 하면 다 된다.

회의실 배정에서는 무엇이 중요한 것이였는지 다시 생각을 해봐야 했다.

시작이 뭐가 중요하냐?

언제 끝나냐?가 중요하지. 끝난 시간을 중심으로 정렬을 하고 다음 시간을 선택해야 한다.


"""

import sys
sys.stdin=open("input.txt", "r")

n = int(input())
meeting = []

for i in range(5):
    a, b = map(int, input().split())
    meeting.append((a,b))

meeting.sort(key= lambda x : (x[1], x[0]))

et = 0
cnt = 0

for x, y in meeting:
    if x >= et:
        et = y
        cnt +=1

print(cnt)