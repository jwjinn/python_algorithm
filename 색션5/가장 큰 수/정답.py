"""
이 문제를 푸는 데 가장 어려운 점은 스텍이라는 개념을 생각하는 것이다.

예를 들자.

5 2 7 6 8 2 3 이라는 숫자가 들어와서 세자리의 숫자를 빼서 가장 큰 수를 도출해라. 라고 한다면...

스택이라는 개념을 생각할 수 있을까?

기존에 들어있는 숫자를 비교하고 조건에 맞춰서 뺀다. -> 스택이라고 생각해야 하는데.. 어렵네..
"""

import sys
sys.stdin=open("input.txt", "rt")
num, m=map(int, input().split())
num=list(map(int, str(num)))

stack = []

for x in num:
    while stack and m > 0 and stack[-1] < x:
        # stack이 차있고 뺄 횟수가 남아있고 가장 최근에 들어온 값이 더 작으면
        stack.pop() # 스택을 빼고
        m -=1 # 기회를 줄인다.
    stack.append(x)

if m !=0:
    stack = stack[:-m]
res = "".join(map(str, stack))

print(res)