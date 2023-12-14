"""

K번째 큰 수

현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있다.

3장의 카드에 적힌 수를 합한 값을 기록하고자 한다.

이렇게 기록해서 K번째로 큰 수를 출력

모든 케이스를 커버하는 법?

내가 생각하지 못한 것은 3차원배열을 사용하는 법



"""
import sys

sys.stdin=open("input.txt", "rt")

N, K = map(int, input().split())

numbers = list(map(int,input().split()))

print(numbers)

# numbers[0] + numbers[1] + numbers[2]
# numbers[0] + numbers[1] + numbers[3]
# numbers[0] + numbers[1] + numbers[4]
# numbers[0] + numbers[1] + numbers[5]
# numbers[0] + numbers[1] + numbers[6]
# numbers[0] + numbers[1] + numbers[7]
# numbers[0] + numbers[1] + numbers[8]
# numbers[0] + numbers[1] + numbers[9]

# numbers[0] + numbers[2] + numbers[3]
# numbers[0] + numbers[2] + numbers[4]

# sum = 0

sum = []

for i in range(1, len(numbers)):
    for n in range(i+1, len(numbers)):
        print(i, n)

        # sum = numbers[0] + numbers[i] + numbers[n]
        sum.append(numbers[0] + numbers[i] + numbers[n])
        # print(sum)

sum.sort()

print(sum)