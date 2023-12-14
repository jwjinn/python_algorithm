"""
뒤집은 소수

N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면
그 수를 출력하는 프로그램을 작성해라.



"""

import sys
sys.stdin=open("input.txt", "r")

N = int(input())

num = list(input().split())

inverseNumber = []

def reverse(x):
    temp_number = ""
    for i in range(len(x) - 1, -1, -1):
        

        if x[i] == '0':
            continue
        else:
            # print(x[i], end="")
            temp_number += x[i]
            # inverseNumber.append(int(x[i]))
            # print(temp_number)
            # inverseNumber.append(int(temp_number))
    # print()

    inverseNumber.append(int(temp_number))

for i in num:
    reverse(i)

# inverseNumber.sort()
# print(inverseNumber)
# print(inverseNumber)

# print(max(inverseNumber))


"""
소수 판별
"""
# print(max(inverseNumber) + 1)
prime = [0] * (max(inverseNumber) + 1)
# cnt = 0
loc = 0

prime_list = []

for i in range(2, len(prime)):
    # print(i)
    if prime[i] == 0: # 소수다.
        # cnt +=1
        # print(i)
        if i in inverseNumber:
            prime_list.append(i)

        for j in range(i, len(prime), i):
            # print(j)
            prime[j] = 1

# prime_list.sort(reverse=True)

for i in prime_list:
    print(i, end = " ")