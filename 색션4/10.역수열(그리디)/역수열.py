"""
역수열

1부터 n까지 각각의 수 앞에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것이 역수열

4 8 6 2 5 1 3 7

1앞에 놓인 1보다 큰 수는 4 8 6 2 5 라서 5개이다.
2앞에 놓인 2보다 큰 수는 4, 8, 6. 이렇게 3개,

따라서 4 8 6 2 5 1 3 7의 역수열은 5 3 4 0 2 1 1 0 이 된다.

"""

import sys
sys.stdin=open("input.txt", "r")

n = int(input())
numbers = list(map(int, input().split()))

print(numbers)