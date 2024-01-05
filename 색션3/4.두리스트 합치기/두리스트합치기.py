"""
두 리스트 합치기



"""
import sys
sys.stdin=open("input.txt", "r")


n1 = int(input())
number1 = list(map(int,input().split()))

n2 = int(input())
number2 = list(map(int,input().split()))


# print(number1)
# print(number2)

new = number1 + number2

new.sort()
print(new)

for i in new:
    print(i, end = " ")


