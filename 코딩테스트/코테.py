from typing import List
from typing import Tuple


def answer(prices: List[Tuple[int, int]]) -> int:
    n = len(prices)

    # print(n)    
    # print(prices)

    gapp = []

    # print(prices[0])

    # print(prices[0][1] - prices[0][0])


    for i in range(0,n):
        gapp.append((i,prices[i][1] - prices[i][0]))

    # print(gapp)

    gapp.sort(key=lambda x: (x[1], x[0]), reverse= True) # 이렇게 해서 가장 큰 

    # gapp.sort(key=lambda x: (x[1], x[0]))

    # print(gapp)

    select_buiness = n // 2

    sum = 0

    # print(prices[0])

    sum = 0

    for i in range(0, n):
        # print(gapp[i][0]) # 앞에서부터 비즈니스를 선택해야 하는 로케이션

        loc = gapp[i][0]
        # print(loc)

        print(prices[loc])
        
        if i < select_buiness:
            sum +=prices[loc][0]
            print(prices[loc][0])

        else:
            sum +=prices[loc][1]
            print(prices[loc][1])

        
    print(sum)


    # print(sum)

    # select_buiness = n // 2

    # sum = 0

    # for i in range(0, n):

    #     if i < select_buiness:
    #         print("bussiness 선택: ", end="")
    #         print(gapp[i])
    #         sum +=gapp[i][1]

    #     else:
    #         print(gapp[i])
    #         sum +=gapp[i][1]

    # print(sum)

    return 0


answer([(10, 30), (50, 100), (20, 50), (40, 80)])

# print(answer([(10, 30), (50, 100), (20, 50), (40, 80)]) == 170)
# print(answer([(10, 100), (20, 120), (30, 140), (40, 130)]) == 280)
# print(answer([(250, 700), (50, 400), (600, 900), (150, 200), (100, 800), (400, 500)]) == 2000)