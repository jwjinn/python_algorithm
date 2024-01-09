"""
창고 정리



"""

# import sys
# sys.stdin=open("input.txt", "r")

n = int(input())

box = list(map(int, input().split()))
box.sort()

shuffle = int(input())

# print(box)

# print(min(box))

# print(box.index(14))

for i in range(shuffle):

    box[box.index(max(box))] = max(box) -1
    box[box.index(min(box))] = min(box) +1

print(max(box) - min(box))