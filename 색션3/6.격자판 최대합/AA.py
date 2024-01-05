"""
격자판 최대합

각 행의 합. 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력해라.

"""

import sys
# sys.stdin = open("input.txt", 'r')

n = int(input())
k = n
# print(n)

bingo = [0] * n

max = 0


for i in range(n):
    bingo[i] = list(map(int, input().split()))
    # print(sum(bingo[i]))
    if sum(bingo[i]) > max:
        max = sum(bingo[i])

# print("=========")
# print(max)



    
# print(bingo)
    
for i in range(n):
    temp = []
    for j in range(n):
        
        # print(bingo[j][i])
        temp.append(bingo[j][i])
        
       
    # print(temp)
    # print(sum(temp)) 

    if max < sum(temp):
        max = sum(temp)    

temp = []

for i in range(n):
    # print(bingo[i][i])
    temp.append(bingo[i][i])


# print("아래 대각선: ")
# print(temp)
# print(sum(temp))

if max < sum(temp):
    max = sum(temp)


# print("==========")

temp = []

for i in range(n):
    # print(bingo[i][n-i-1])
    temp.append(bingo[i][n-i-1])

# print("위로 향하는 대각선: ")
# print(temp)
# print(sum(temp))

if max < sum(temp):
    max = sum(temp)

print(max)