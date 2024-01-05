
import sys
# sys.stdin = open("input.txt", 'r')

n = int(input())

tree = [0] * n

for i in range(n):
    tree[i] = list(map(int, input().split()))

# print(tree)

center = n //2

# print(tree[0][center]) # j = 0

# print()

# print(tree[1][center-1]) # i = 1 j = 1 center = 2
# print(tree[1][center]) # j = center - i
# print(tree[1][center+1])

# print()

# print(tree[2][center - 2]) # j = 2
# print(tree[2][center - 1])
# print(tree[2][center])
# print(tree[2][center + 1])
# print(tree[2][center + 2])

# print()

# print(tree[3][center-1]) # j = 1
# print(tree[3][center])
# print(tree[3][center+1])

# for i in range(0, n):

#     if i == 0:
#         print("pass_start")
#     else:
#         if i <= center:
#             for j in range(center - i, (center + i) + 1):
#                 print(i, j)

#         elif i == n -1:
#             print("pass_end")
            
#         else:
#             for j in range(i - center, center + abs(i - center) + 1): # center = 2, i = 3, j = 1
#                 print(i, j)
#     print()

tot = []

for i in range(0, n):

    if i == 0:
        # print("pass_start")
        # print(tree[i][center])
        tot.append(tree[i][center])
    else:
        if i <= center:
            for j in range(center - i, (center + i) + 1):
                # print(i, j)
                # print(tree[i][j])
                tot.append(tree[i][j])
        elif i == n -1:
            # print("pass_end")
            # print(tree[i][center])
            tot.append(tree[i][center])
            
        else:
            for j in range(i - center, center + abs(i - center) + 1): # center = 2, i = 3, j = 1
                # print(i, j)
                # print(tree[i][j])
                tot.append(tree[i][j])
    # print()

print(sum(tot))

# for i in range(n):
#     for j in range(0, center):
#         print(tree[i][center])

# for i in range(0, n):
#     for j in range(0, n):
#         if j == center:
#         print("*", end="")

#     print()

