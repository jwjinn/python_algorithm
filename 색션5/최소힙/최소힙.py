"""
최소힙

구성은 부모 노드값이 왼쪽 자식과 오른 자식노드의 값보다 작게 트리를 구성해야 한다.

부모가 왼쪽, 오른쪽 자식노드보다 작아야 한다.

내가 풀지 못한 이유는 노드의 원리를 알지 못했던 점, 파이선에 관련 매서드가
있다는 점을 몰랐다는 점.


"""

import sys
import heapq as hq

sys.stdin=open("input.txt", "rt")
a = []

while True:
    n = int(input())

    if n == -1:
        break

    if n == 0:
        if len(a) ==0:
            print(-1)

        else:
            print(hq.heappop(a))

    else:
        hq.heappush(a, n)