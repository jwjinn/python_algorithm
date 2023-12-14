"""
대표값

N명의 학생의 수학점수가 주어진다.

N명의 학생의 평균을 구하고 평균에 가까운 학생은 몇번째 학생인지
출력하는 프로그램을 작성해라.

평균과 가까운 점수가 여러개면 점수가 높은 학생의 번호를 답으로

그것도 같으면 학생번호가 빠른 순으로


입력:
N이 주어지고 두번째 줄은 수학점수인 N개의 자연수가 주어진다.

못푼 이유:

최소 차이인 모든 인덱스들을 어떻게 뽑는가?
[841, 1, 64, 169, 324, 49, 1, 25, 1, 36]

"""

import sys
sys.stdin=open("input.txt", "r")

N = int(input())

math = list(map(int, input().split()))
avg_math = round(sum(math)/len(math))

diff = []


for i in range(0, len(math)):
    diff.append((math[i] - avg_math) ** 2)

print(math)


print(diff)
print(min(diff))

print(diff.index(min(diff)))


# math.index(1)


# print(avg_math)