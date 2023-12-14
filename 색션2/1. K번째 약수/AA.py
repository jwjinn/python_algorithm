import sys
# sys.stdin=open("input.txt", "rt")

N, K = map(int, input().split(" "))

divisor = []

for div in range(1, N+1):
    if N % div == 0:
        divisor.append(div)

if len(divisor) < K:
    # print("-1")
    print(-1)
else:
    print(divisor[K - 1])