"""
랜선자르기(결정알고리즘)

앨리트 학원은 자체적으로 K개의 랜선을 가지고 있습니다.
선생님은 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을
잘라서 만들어야 했습니다.

예를 들면 300cm 짜리 랜선을 140CM 짜리 랜선을 두 개 잘라내면 20cm은 버려야 합니다.


랜선을 자를때 손실되는 길이는 없다고 가정한다.

K개의 랜선에서 N개의 랜선을 만들기 위해서 최대의 랜선 길이는?

ex)
4 11
802
743
457
539


"""

"""

이게 위에서 진행했던 이진검색을 사용할 수 있는 것인지 생각을 못함.
구간이 주어져 있고 구간 내에서 최적의 답을 찾는 과정이라면
이진 검색을 활용하는 것을 적극적으로 검토해봐야함.

"""

import sys
sys.stdin=open("input.txt", "r")

k, n = map(int, input().split())

len = []

for _ in range(k):
    t = int(input())
    len.append(t)


lt = 0
rt = max(len)

def cutLen(cutsize, allLen):
    count = 0

    for i in allLen:
       count += (i // cutsize)

    return count

# print(cutLen(200, len))


while lt <= rt:
    mid = (lt + rt) // 2
    num = cutLen(mid, len)

    if num == n:
        print(mid)
        break

    elif num > n: # 잘라지는 수가 더 많다. 자르는 수를 높혀야 한다.
        lt = mid + 1

    else:
        rt = mid - 1

