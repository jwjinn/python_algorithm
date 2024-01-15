from typing import List
from typing import Tuple

class ScorePair:
    def __init__(self, left_user_id: int, right_user_id: int, score: float) -> None:
        self.left_user_id = left_user_id
        self.right_user_id = right_user_id
        self.score = score

    def returnInformation(self):
        return [self.left_user_id, self.right_user_id, self.score]

class MatchmakingAggregator:

    @staticmethod
    def aggregate(n: int, score_pairs: List[List[ScorePair]]) -> List[Tuple[int, int]]:

        print("들어오는 총 사람의 수")
        print(n)

        print("2차원 배열의 크기") # 2개니까 배열을 둘까지 돌려야 함.
        print(len(score_pairs))

        print(len(score_pairs[0])) # 한 개 리스트에 있는 경우. 길이가 하나니까 한번만.


        temp = []

        two_dimension_size = len(score_pairs)

        for i in range(0, two_dimension_size):
            temp.append(len(score_pairs[i]))

        print(temp)
        print("---------")

        t = []

        for i in range(0, len(temp)):
            for j in range(0, temp[i]):
                print(score_pairs[i][j].returnInformation())

                t.append(score_pairs[i][j].returnInformation())

        print(t)

        t.sort(key= lambda x: [x[2], x[1], x[0]], reverse=True)
        print("===")
        print(t)

        first = (t[0][0],t[0][1])
        print(first)

        # 
        # for i in range(0, len(temp)):
        #     print(score_pairs[i][temp[i]-1].returnInformation())

        
        # for i in range(0, len(temp)):
        #     for j in range(0, len(temp)-1):
        #         print(score_pairs[j][temp[i]-1].returnInformation())



        # cnt = 0
        # while cnt < n:


        # print(score_pairs.shape)

        # print(score_pairs[0][0].returnInformation())

        # print(score_pairs[1][0].returnInformation())
        # print(score_pairs[1][1].returnInformation())

        # print(score_pairs[2][0].returnInformation())
        # print(score_pairs[2][1].returnInformation())
        # print(score_pairs[2][2].returnInformation())

        return []

# t = ScorePair(0, 1, 10)

# print(t.returnInformation())


print(MatchmakingAggregator.aggregate(3, [
  [ScorePair(0, 1, 10)],
  [ScorePair(0, 2, 5),
   ScorePair(1, 2, 1)],

    [ScorePair(0, 2, 5),
   ScorePair(1, 2, 1),
   ScorePair(1, 2, 1)
   ]
]
))