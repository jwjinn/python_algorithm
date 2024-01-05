"""
숫자만 추출

문자와 숫자가 섞여 있는 문자열에서 숫자만 뽑아서 출력 그리고 약수의 개수도.

"""

import sys
sys.stdin=open("input.txt", "r")

st = input()

number =""

def whereStart(st):
    count = 0
    
    for i in st:

        # print(i)

        if i == '0':
            count+=1
        else:
            count +=1
            break
            # print(i)
    # print()
    # print(count)
    # print(st[count-1:len(st)])
    return st[count-1:len(st)]


for i in st:
    # print(i)

    if not('A' <= i <= 'z'):
        # print(i)
        number +=i
# print(number)
        
num = whereStart(number)
print(num)

sosu = 0

for i in range(1, int(num) +1):
    # print(i)
    if int(num) % i ==0:
        sosu +=1

print(sosu)