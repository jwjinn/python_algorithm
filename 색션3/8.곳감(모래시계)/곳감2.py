import sys
sys.stdin=open("input.txt", "r")

n = int(input())

mapp = [0] * n

for i in range(n):
    mapp[i] = (list(map(int, input().split())))

# print(mapp)

m = int(input())
rotate = [0] * m
# new = [0] * m

for i in range(m):
    rotate[i] = (list(map(int, input().split())))

def rotating(row, direction, many): # 2 0 3
    row = row - 1
    length = len(mapp[row])
    temp = []
    

    # print(mapp[row])

    if direction == 0:


        for i in range(length):

            if i + many < length: # i가 1까지
                # print("조건1`")
                # mapp[row][i] = mapp[row][i + many]
                # print(mapp[row][i])
                # print(mapp[row][i + many])

                temp.append(mapp[row][i + many])

                # mapp[row][i] = mapp[row][i + many]
                # mapp[row][i] = ori[row][i + many]


            else:
                # mapp[row][i] = mapp[row][abs(length - (i + many))]
                # print("조건2`")
                loc = abs(length - (i + many))
                # print(loc)
                # print(mapp[row][i])
                # print(mapp[row][abs(length - (i + many))])
                # mapp[row][i] = mapp[row][abs(length - (i + many))]
                # mapp[row][i] = ori[row][abs(length - (i + many))]

                temp.append(mapp[row][abs(length - (i + many))])
                
                # mapp[row] = temp

        # print(temp)
        # print(mapp[row])

        mapp[row] = temp
    # print(mapp[row])

    # print(mapp[row])

    elif direction == 1:

            for i in range(length):

                if i >= length: # i가 3까지
                    
                    temp.append(mapp[row][i - many])
                    

                else:

                    # loc = abs(length - (i + many))
                    loc = length - many + i + 2 # i = 0 , loc = 4 - 3 + 0 
                    temp.append(mapp[row][loc])

    print(mapp[row])
    mapp[row] = temp

rotating(2,0,3)
print(mapp)

rotating (4,0,3)
print(mapp)