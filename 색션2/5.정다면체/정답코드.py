import sys

sys.stdin=open("input.txt", "r")
n, m = map(int, input().split())

cnt = [0] * (n+m+3)

# max = -135635

# 인덱스가 값, value가 횟수
for i in range(1, n+1):
    for j in range(1, m +1):
        cnt[i+j] +=1


"""
강의에서는 이렇게 했지만, 나는 max로
"""
# for i in range(n + m + 1):
#     if cnt[i] > max:
#         max = cnt[i]

# print(max)

max = max(cnt)

for index, value in enumerate(cnt):
    if value == max:
        print(index, end = " ")