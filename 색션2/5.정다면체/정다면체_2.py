import sys

sys.stdin=open("input.txt", "r")
two_dice = list(map(int, input().split()))

# 모든 경우들이 나온다.
sum_result = []
for i in range(1, two_dice[0] + 1):
    for j in range(1, two_dice[1] + 1):
        # print(i + j)

        sum_result.append(i + j)



# print(sum_result)

# 나올 수 있는 모든 경우
all_result = list(set(sum_result)) 
# print(all_result)

count = []

for idx, value in enumerate(all_result):
    # print(sum_result.count(value))
    count.append(sum_result.count(value))

max_count = max(count) # 가장 많이 나오는 경우

# print(count)
# print(sum_result.count(all_result[0]))

for i in all_result:
    if sum_result.count(i) == max_count:
        print(i, end=" ")

