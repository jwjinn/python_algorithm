
"""
카드 역배치

1부터 20까지 숫자가 배열되어 있고 구간이 주어지면, 해당 구간을 역순으로 놓는다.

그것을 지속적으로 반복하면 된다.

10개의 구간이 주어지고 그 구간만큼 역순으로 배치를 하고 마지막에는 최종 배치된 숫자를 보여주면 된다.


"""

import sys
# sys.stdin=open("input.txt", "r")

first = []

for i in range(1, 21):
    first.append(i)


def reverse(number, x, y):

    # print("들어오는 원문 배열: ")
    # print(number)

    temp = []
    front = number[0:x-1]
    back = number[y:len(number)]

    x = x - 1
    y = y - 1

    # print("앞의 배열: ")
    # print(front)
    
    # print("뒤의 배열: ")
    # print(back)

    for i in range(y, x-1, -1):
        # print(i)
        temp.append(number[i])
    
    # print("temp")
    # print(temp)


    
    out = front + temp + back

    # print("out되는 배열")

    # print(out)
    return out

# k = reverse(number,5,10)

reversing = []

for i in range(0, 10):
    n, m = map(int, input().split())

    # reversing = number

    if i ==0:
        reversing = first

    reversing = reverse(reversing, n, m)
    # print(reversing)

# print("=============")
for i in reversing:
    print(i, end=" ")