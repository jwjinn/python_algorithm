"""
단어찾기 해쉬

현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다.
N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다.

N개의 단어를 입력받고 다음에 N-1개의 단어를 입력받아 나오진 단어를 확인하자.

"""

import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

word = dict()

for i in range(n):
    word[input()] = 0

# print(word)
    
for j in range(n - 1):
    word[input()] = 1

# print(word)

# print(word.values[0])

for key, value in word.items():
    if value == 0:
        print(key)