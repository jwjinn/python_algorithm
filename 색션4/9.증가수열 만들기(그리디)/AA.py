"""
증가수열 만들기

제일 왼쪽, 제일 오른쪽에서 수를 선택해서 증가하는 수열을 만들어라.

"""

import sys
# sys.stdin=open("input.txt", "r")

from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
num = deque(numbers)

# num.popleft()


now = 0
cnt = 0
state=""

if num[0] < num[n-1]:
    now = num.popleft()
    # print(now)
    cnt+=1
    state+="L"

elif num[0] > num[n-1]:
    now = num.pop()
    # print(now)
    cnt+=1
    state+="R"


while True:
    if now < num[len(num)-1]:
        now = num.pop()
        # print(now)
        state+="R"
        cnt+=1

    elif now < num[0]:
        now = num.popleft()
        # print(now)
        state+="L"
        cnt+=1

    else:
        print(cnt)
        print(state)
        # print("안됨")
        break


# print(num)

# if num[0] < num[n-1]:
#     print(num[0])
#     num.popleft()

# elif num[0] > num[n-1]:
#     print(num[0])
#     num.pop()

# print(num)