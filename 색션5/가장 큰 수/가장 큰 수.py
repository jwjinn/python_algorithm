"""
가장 큰 수

해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다.

ex) 5276823 에서 3개의 자릿수를 제거할 경우 가장 큰 수는 7823이다.

그러면...

처음에는 가장 중요한 것이 첫자릿수이니... 3번의 기회안에서 가장 큰 첫자리를 골라야 한다.
5 -> 2 -> 7: 이것만으로 일단 2번 활용.

그 다음자리에서 한번 더 없애야 하는 데, 6과 8사이에서 6을 제거하면 더 큰 숫자가 된다. 앞에서부터 숫자를 자르면 될듯...

"""

import sys
sys.stdin=open("input.txt", "r")

from collections import deque

number, n = input().split()
n = int(n)

# print(number)

num = []

for i in number:
    num.append(int(i))

num = deque(num)

print(num)
# n값이 3이면 n+1만큼은 확인해야 한다. 즉, 5276까지는 확인하고 7이 크므로 그 앞의 숫자 둘은 제거.


last = 0
cnt = 0
start = 0 

# 자를 수 있는 횟수 +1만큼은 확인해야.
for i in range(start, n-cnt+1):
    # print(num[i])

    if num[i] > last:
        # print(num[i])
        last = num[i]

# print(last)

# print(num.index(7))

for i in range(num.index(7)):
    cnt +=1
    del num[0] # 7이 있는 인덱스 전까지 확인.
    
start +=1
print(num)
"""

"""

# print(num[start])

for i in range(start, n-cnt+1+1): # 1, 
    print(num[i])

"""
이런식으로 하면 풀수는 있을 듯 한데,,, 너무 더럽다.
너무 나 많은 for문과 반복문은 컴공생의 의욕을 떨군다.
"""