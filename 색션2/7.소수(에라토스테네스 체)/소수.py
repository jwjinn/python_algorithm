import sys

sum_result = []

sys.stdin=open("input.txt", "r")

N = int(input())

count = 0

for i in range(2 , N +1):
    if ((i % 2 != 0) & (i % 3 != 0)):
        print(i)