"""
점수계산

연속적으로 답을 맞히는 경우에는 가산점을 준다.

연속으로 맞추면 연속으로 맞추는 횟수에 따른 점수를 제공

입력:

문제의 갯수
채점 결과

출력
점수
"""

import sys
sys.stdin=open("input.txt", "r")

N = int(input())
quiz = list(map(int, input().split()))

combo = 1
score = 0

for i in quiz:
    if i == 1:
        score += combo * 1
        combo+=1
    else:
        combo = 1

print(score)
