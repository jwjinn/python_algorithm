"""
회문 문자열 검사

N개의 문자열 데이터를 입력받아, 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우
이면 YES, 아니면 NO를 출력

단, 대소문자를 구별하지 않는다.

"""

import sys
sys.stdin=open("input.txt", "r")

N = int(input())



def check_word(x):

    x = x.lower()
    # print(x)
    # print(len(x))
    # print(len(x) 2)
    # print(len(x) // 2)

    # if len(x) % 2 !=0:
    #     print('홀수 길이')
    # else:
    #     print('짝수')

    # print(x[0])
    # print(x[-1])

    # print(x[1])
    # print(x[-2])

    state = False

    for i in range(0, len(x) // 2):
        # print("i의 값: "+str(i))
        if x[i] == x[(i+1) * (-1)]:
            
            # print(x[i])
            # print(x[(i+1) * (-1)])
            state = True
        else:
            # print(x[i])
            # print(x[(i+1) * (-1)])
            state = False
            break

    return state

# print(check_word(word[3]))


for i in range(0, N):
    if check_word(input()) == True:
        print("#" + str(i+1) + " YES")
    else:
        print("#" + str(i+1) + " NO")