"""
자릿수의 합

N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요.

def digit_sum(x)로 작성하세요.

입력:
3
125 15232 97

출력

97

"""

import sys
# sys.stdin=open("input.txt", "r")

N = int(input())

number = list(input().split())

sum_list = []

for i in number: # 숫자 125, 15232, 97
    sum = 0
    # print(i)
    # print(len(i))
    for j in range(0, len(i)):
        # print(i[j], end= " ")
        sum += int(i[j])
        
    sum_list.append(sum)
    # print("*")


# print(sum_list)

# print(sum_list.index(max(sum_list)))
print(number[sum_list.index(max(sum_list))])
