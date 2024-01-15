"""
교육과정 설계

현수는 1년의 수업 계획을 짜야 합니다.

필수 과목은 반드시 이수해야 하며, 그 순서도 정해져 있습니다.

총 과목이 A, B, C, D, E, F, G가 있고 필수과먹이 CBA로 주어지면 이 순서대로
수업계획을 짜야 합니다.

주어진 수업 설계가 잘 되었다면, YES.
잘못된 것이면 NO를 출력하는 프로그램을 작성하세요.

"""

import sys
sys.stdin=open("input.txt", "rt")

from collections import deque
import copy

temp = input()
essential = []
for i in temp:
    essential.append(i)

essential = deque(essential)

n = int(input())

# list_essentail = [0] * n

# for i in range(n):
#     list_essentail[i] = essential

# print(list_essentail)


compare = [0] * n

for i in range(n):
    temp = input()
    t = []
    # print(temp)
    for k in temp:
        # compare[i].append(k)
        # print(k)
        
        t.append(k)

    compare[i] = deque(t)
    # print(t) 

# print(compare)


"""
essential 리스트에서는 필수과목의 순서가 기록

compare 리스트에서는 제대로 교육 순서가 되어있는 지 확인할 과목 리스트들이 있다.

과목들을 팝하고 essential도 있으면 팝하는 식으로 진행하면 될듯.

"""

# print(compare[0])

# print(list_essentail)


for t in range(n):

    # print("essential:")
    # print(essential)
    # temp_essential = essential 이렇게 하면 왜 인지 큐가 사라짐,

    # temp_essential = list_essentail[t] # 설마 deque copy by reference?

    temp_essential = copy.copy(essential)

    # print("id - temp_essentail: ", id(temp_essential))
    # print("id - essentail: ", id(essential))

    """
    id - temp_essentail:  1885241703248
    id - essentail:  1885241703248

    deque를 = 를 하면 copy by reference

    """

    # print("temp_essential")
    # print(temp_essential)
    while (len(compare[t]) > 0):



        letter = compare[t].popleft()

        # print(letter)

        if letter == temp_essential[0]:
            tt = temp_essential.popleft()
            # print("temp_essential left_pop: ", tt)

            if len(temp_essential) == 0:
                print(f"#{t+1} YES")
                break

    
    if len(temp_essential) > 0:
        print(f"#{t+1} NO")





# t = 0

# while (len(compare[t]) > 0):

#     temp_essential = essential

#     letter = compare[t].popleft()

#     print(letter)

#     if letter == temp_essential[0]:
#         tt = temp_essential.popleft()
#         print("temp_essential: ", tt)

#         if len(temp_essential) == 0:
#             break
