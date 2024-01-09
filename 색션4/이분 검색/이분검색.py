"""
임의의 N개의 숫자가 입력으로 주어집니다.

N개의 숫자를 오름차순으로 정렬한 다음, N개의 수중 한개의 수인 M이 주어지면
이분검색으로 M이 정렬된 상태에서 몇번째에 있는지를 구하시요


이진검색은 1/2, 1/2로 가기에
"""

import sys
sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
number = list(map(int, input().split()))

number.sort()


lt = 0
rt = n -1

while lt <= rt:
    mid = (lt + rt) //2

    if number[mid] == m:
        print(mid + 1)
        break

    elif number[mid] > m: # 가운데에 있는 숫자가 m보다 크면
        # 간단하게 말하면 m이 상대적으로 좌측에 있는 거임.
        # 그래서 mid보다 더 오른쪽에 있는 것은 사실 필요가 없음
        rt = mid -1
    else:
        lt = mid + 1

