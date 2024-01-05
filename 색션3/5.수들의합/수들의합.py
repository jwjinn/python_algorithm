"""
수들의 합

i부터 j번째 수까지의 합이 M이 되는 경우의 수를 구하는 프로그램을 구해라.

"""

import sys
sys.stdin=open("input.txt", "r")

N, M = map(int, input().split())
number = list(map(int,input().split()))

sum = number[0]
count = 0


for i in range(1, len(number)):
    
    sum +=number[i]

    if sum == M:
        count +=1
        sum -= number[i-1]
        print("M이랑 같다.")
        print("count: ", count)
        print("sum: ", sum)

        print("=======================")
    
    elif sum < M:
        print("M이 더큼.")
        print("sum: ", sum)
     
        print("=======================")
    
    elif sum > M:
        sum -= number[i]
        print("sum이 더큼.")
        print("sum: ", sum)

        
        print("=======================")

print(count)