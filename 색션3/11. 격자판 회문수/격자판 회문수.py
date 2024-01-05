"""
7 * 7 격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.

회문수란 121과 같이 앞으로 뒤로 읽을 때 같은 수를 의미합니다.

와 개빡세다. 비고가??????

계획을 세워야 하는데?, 인덱스에 넣는 식으로 해야 하지 않을까

리스트에 rt lt를 이용하면 되지 않을까?
"""

example = [6,1,2,3,2,1,1]

def check(num):
    rt=0
    lt= len(num) - 1

    temp=""
    print(num)
    for i in num:
        temp+=str(i)

    print(temp)

    print(temp[::-1])

    if temp == temp[::-1]:
        print("회문 문자열입니다.")
    else:
        print("회문 문자열이 아닙니다.")

check(example)
