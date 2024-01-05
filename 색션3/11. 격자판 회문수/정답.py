"""
격자판 회문수

반복문을 생각을 할때, 특히 2차원 내가 생각이 잘 안되는 것은
2차원 반복문을 꼭 x,y 축으로만 활용한다는 점.

반복문을 전체적으로 돌아가야 하는 거

그거 보다 더 세부적으로 들어가는 반복문을 더 안으로 넣는 식으로 생각을 고쳐먹어야.

"""

import sys
sys.stdin=open("input.txt", "r")

board = [list(map(int, input().split())) for _ in range(7)]

"""
공통적인 것.

5자리이니 크게 3번만 확인하면 된다.

그리고 7*7이다.

컬럼으로 할 때는 5자리이니 *&X$*인지 확인하기 위해서 2번만 확인하면 됨.

"""

cnt = 0

for i in range(3): # 3번만 확인하면 되고
    for j in range(7): # 7*7이고 살펴보는 위치.
        temp = board[j][i:i+5]
        if temp == temp[::-1]:
            cnt +=1 # row확인

        for k in range(2): # 앞뒤 확인
            # 나와야 하는 것이 0일때 4임.
            if board[i+k][j] != board[5-k-1+i][j]: # 크기가 5이고. 한 로우에서 확인해야 하는 게 i번이고 5자리에서 확인해야 하는 횟수는 k
            # if board[i+k][j]!=board[i+5-k-1][j]:
                break; # 값이 다르면 반복문을 취소
        else: # else를 밖으로 뺌. if 조건을 다 충족시켰으면 단 한번 cnt+1을 위한 밖 else
            cnt+=1


print(cnt)
