# import sys
# sys.stdin=open("input.txt", "rt")

# n = input()
# print(n)

"""
K번째 약수

어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때, 나머지가 0이면
q는 p의 약수이다.

입력:
N, K

출력:
N의 약수들 중 K번째로 작은 수를 출력한다.

ex) 6 3

6의 약수 중 3번째로 작은 수

1, 2, 3, 6

3출력

K번째 약수가 존재하지 않으면 -1을 리턴.

"""

N, K = map(int, input().split(" "))

divisor = []

print(N, K)

for div in range(1, N+1):
    if N % div == 0:
        divisor.append(div)

# print(divisor)
# print(divisor[3 - 1])

# print(len(divisor))

if len(divisor) < K:
    print("-1")
    (-1)
else:
    print(divisor[K - 1])