"""
곳감

회전을 시킨다.

2 0 3: 2번재 행을 왼쪽으로 3번 옮겨라.

0이면 왼쪽으로 1이면 오른쪽으로

처음에 감이 존재하는 배열을 입력을 받고

M개의 회전명령을 내리고

모래시계 범위에 있는 감의 갯수가 몇개인지를 파악해라.
"""

import sys
sys.stdin=open("input.txt", "r")

n = int(input())

mapp = [0] * n

for i in range(n):
    mapp[i] = (list(map(int, input().split())))

# print(mapp)

m = int(input())
rotate = [0] * m

for i in range(m):
    rotate[i] = (list(map(int, input().split())))

# print(rotate)

# 2 0 3

# def rotating(row, direction, many):
    
#     # print(mapp[row - 1])
#     length = len(mapp[row - 1])
#     # print(len(mapp[row - 1]))

#     for i in range(length):
#         # 0번째 인덱스가 2번 인덱스로 왼쪽으로 3번 이동했을 때
#         # 0번째에 2번 인덱스의 값이 들어가야 한다.
#         mapp[i] = mapp[(length) - many] # 5 - 3

#     print(mapp)

   
# rotating(2, 0, 3)

def rotating(row, direction, many):
    length = len(mapp[row - 1]) # 5
    row = row - 1

    print(mapp[row])
    # print(mapp[row][0])

     

    print(mapp[row][0])
    print(mapp[row][3])

    print()

    print(mapp[row][1])
    print(mapp[row][4])

    print()

    #
    print(mapp[row][2])
    print(mapp[row][(length - 5)])

    print()

    print(mapp[row][3])
    print(mapp[row][(abs(length - 6))])

    print()

    print(mapp[row][4])
    print(mapp[row][(abs(length - 7))])


rotating(2, 0, 3)