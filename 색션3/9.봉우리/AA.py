"""
봉우리

각 격자에는 지역의 높이가 쓰여있다.

상하좌우 숫자보다 다 높으면 그것은 봉우리이다.

봉우리가 몇개인가?


"""
import sys
# sys.stdin = open("input.txt", 'r')
n = int(input())
# mapp = [0] * (n + 2)


# a = [[0,0,0,0,0],[1,1,1,1,1]]

# print(a)

# for i in range(n):
#     a = []
#     if i ==0:
#         a.append(0 for _ in range(n + 1))


a = []
# a.append([0 for _ in range(n + 1)])
# a.append([1 for _ in range(n + 1)])

for i in range(n):
    if i ==0:
        a.append([0 for _ in range(n + 2)]) 

    temp = list(map(int, input().split()))
    temp.insert(0,0)
    temp.append(0)

    a.append(temp)

    if i == n -1:
        a.append([0 for _ in range(n + 2)])    
# print(a)

# print(a[0])
# print(a[1])
# print(a[2])

def mountain():

    count = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # print(a[i][j], end="")

            if a[i][j] > max(a[i-1][j], a[i+1][j], a[i][j -1], a[i][j +1]):
                # print("mountain")
                count +=1

        # print()
    
    return count

n = mountain()
print(n)