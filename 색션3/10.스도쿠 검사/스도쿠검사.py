
import sys
sys.stdin = open("input.txt", 'r')

# k = list(map(int, input().split()))

# a=[list(map(int, input().split())) for _ in range(9)]

# print(a)

a = [list(map(int, input().split())) for _ in range(9)]

temp = a[0]

# temp = [1,1,3,4,5,6,7,8,9]

"""
필요한 것은 1차원 리스트로 인덱싱 하는 것

row단위로 column 단위로 섹터(3 * 3 단위로)
"""




"""
1차원 리스트를 대입을 해서 인덱스 번호에 +!을 진행을 해서 max값이 2이상이면 중복된 값이므로 Error
"""
def checking(a):

    state = True

    # print("original")
    # print(a)
    temp = [0] * 10

    for i in a:
        temp[i] += 1

    if max(temp) > 1:
        # print("Error")
        state = False
    else:
        # print("good")
        state = True    
    # print("temp")

    # print(temp)
    return state

# checking(temp)

def rowCheck(a):

    state = True
    for i in range(9):
        s1 = checking(a[i])
        # print(s1)

        test = s1 * state
        if test == 0: # 로우가 아닌 경우만 체크하면 돈다.
            state = False
            break

    return state


    

def colCheck(a):

    state = True
    sign = 0

    for i in range(9):
        temp = []
        for j in range(9):

            if sign == 1:
                break

            # print(a[j][i], end="")
            temp.append(a[j][i]) # 임시 리스트로 컬럼을 넣는 중.
            s1 = checking(temp)  # 컬럼 단위 스도쿠 확인 테스트
            
            test = s1 * state
            if test == 0:
                state = False
                sign = 1
                break

    return state

        # print()

"""
스도쿠의 에리어 3곱하기 3, 로케이션은 정해져있음

1,1 1,4 1,7
4,1 4,4 4,7
7,1 7,4 7,7

k = [1, 4, 7]

for i in range(len(k)):
    for j in range(len(k)):
        print(k[i], end = "")
        print(k[j], end = "")

        print()

    print()

"""
def area(a):
    print(a[1][1])

    # 이렇게 하면 될 것은 확실한데 너무 코드가 지저분하다.



# print(rowCheck(a))
# print(colCheck(a))

area(a)



