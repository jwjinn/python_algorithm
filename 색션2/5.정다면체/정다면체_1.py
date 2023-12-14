"""
정다면체

N면체와 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의
합 중 가장 확률이 높은 숫자를 출력하는 프로그램

입력:

N, M은 4, 6, 8, 12, 20중의 하나이다.

예제

입력: 4 6

출력: 5 6 7

"""

import sys

sum_result = []

sys.stdin=open("input.txt", "r")

two_dice = list(map(int, input().split()))

for i in range(1, two_dice[0] + 1):
    for j in range(1, two_dice[1] + 1):
        # print(i + j)

        sum_result.append(i + j)


all_result = list(set(sum_result))

# all_result = sum_result

print("나올 수 있는 모든 경우: ")
print(all_result)

temp = []

for i in all_result:
    print(sum_result.count(i))

    temp.append(sum_result.count(sum_result.count(i)))


# print(temp)
print("최대 값: ")
print(max(temp))

print("""""")

max_temp = max(temp)

for i in all_result:
    # print(sum_result.count(i))

    # if sum_result.count(sum_result.count(i)) == max_temp:

    #     # print(i)
    #     # print(all_result[i])


    #     print(all_result[i])

    if sum_result.count(sum_result.count(i)) == max_temp:
        print(i)
        print("True")
    else:
        print(i)
        print("False")

print(all_result)
print(all_result[5])
print(all_result[6])
print(all_result[7])