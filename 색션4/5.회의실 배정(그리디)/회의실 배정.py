"""
회의실 배정

한 개의 회의실이 있는데 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들려고 한다.

각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라.

"""

import sys
sys.stdin=open("input.txt", "r")

n = int(input())

table =[]

for _ in range(n):
    t= list(map(int, input().split()))
    table.append(t)

# print(table)

# print(table[0])
# print(table[0][1])

for i in range(n):
    print(table[i])

    now = table[i]

    for j in range(i+1, n):
        if table[j][0] >= table[i][1]:
            print(table[j])
        # print(table[j])

    print()

"""
대충 어떠한 느낌인지는 알겠지만 구현을 하는데 있어서 생각이 안남.


"""
