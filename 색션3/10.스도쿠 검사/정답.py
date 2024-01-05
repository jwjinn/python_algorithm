"""
아이디어:
체크 리스트를 만들고 해당 되는 인덱스 번호에 1을 넣으면서 스도쿠가 제대로
동작되고 있는 지 확인을 합니다.

스도쿠의 3*3 구역인 경우에는 
반복문에 해당되는 공식을 만드는 개념으로 이해해야 한다.

"""
import sys
sys.stdin=open("input.txt", "r")



def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10

        for j in range(9):
            ch1[a[i][j]] = 1 # 행 Check
            ch2[a[j][i]] = 1 # 열 Check

        if sum(ch1) != 9 or sum(ch2) !=9:
            return False
        # 함수의 return을 사용하면 좋은 점은 즉시 함수를 종료하고 나갈 수 있기 때문.

    """
    이곳에서 부터는 구역을 해야 하는데
    생각을 해보면 중심이 되는 곳은 1, 4, 7로 인덱스 번호가 정해져 있다.

    컴공생으로서 몇차원 배열은 솔직히 매우 매우 매우 꺼림직하지만 그런 사고를 할 필요가 있다.
    """

    for i in range(3): # 0, 1, 2
        for j in range(3): # 0, 1, 2
            # 이 2중 포문의 의미는 3*3의 중심이 전체 스도쿠에서 9개가 있다는 것을 의미.
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                # 이건 한 구역의 3*3을 의미한다.
                # 공식을 셀때 k, j 는 더하면서 하는 것이 맞음 하나하나 간격을 벌려야
                    ch3[a[i*3 + k][j*3 + s]]=1 # 반복문을 로우로 읽는 거니, 처음은 네모 칸의 좌측 상단이 타겟이다.
                
            if sum(ch3) !=9:
                return False


    
    return True


a = [list(map(int, input().split())) for _ in range(9)]

if check(a):
    print("YES")
else:
    print("NO")