"""
K번째 수

N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열에서 s번째부터 
e번째 까지의 수를 오름 차순 정렬했을 때 K번째로 나타나는 숫자를 출력하는
프로그램을 작성하세요.


입력:
첫번째 줄 테스트 케이스 T(1<=T<=10)

각 케이스별
첫번째 줄은 자연수 N, s, e, k가 차례로 주어진다.
두번째 줄은 N개의 숫자가 차례로 주어진다.
"""

import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    number = list(map(int, input().split()))

    number = number[s-1:e]
    number.sort()
    print("#"+ str(i + 1) +" " + str(number[k-1]))

    number.clear()


# """

# split(" ")로 했을 때

# Traceback (most recent call last):
#   File "c:\Users\jwjin\Desktop\개발\알고리즘\색션2\K번째 수\k번째수.py", line 24, in <module>
#     number = list(map(int, input().split(" ")))
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: ''
# PS C:\Users\jwjin\Desktop\개발\알고리즘\색션2\K번째 수> 
# """

# # N, s, e, k = map(int, input().split(" "))

# # n1 = list(map(int, input().split(" ")))
# # print(n1)

# # n1.sort()
# # print(n1)

# # print(n1[k])

# # N, s, e, k = map(int, input().split(" "))

# # n1 = list(map(int, input().split(" ")))
# # print(n1)

# # n1.sort()
# # print(n1)

# # print(n1[k])

