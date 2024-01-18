"""
아나그램

순서가 다르더라도 알파펫과 그 갯수가 일치해서 배열해서 상대편의 단어가 될 수 있는
것을 아나그램이라고 한다.



"""
import sys
sys.stdin=open("input.txt", "rt")

# n1 = input()

n1 = list(map(str, input()))
# print(n1)

word1 = dict()

for i in n1:

    if word1.get(i):
        word1[i] +=1

    else:
        word1[i] =1

word1 = sorted(word1.items(), key= lambda x: x[0])
# 모든 iterator를 받는 sorted 매서드.. 그리고 애초에 정렬해서 갑을 집어넣는 것이 아니라면 딕셔너리 형태에서의 key값을 기준으로 정렬되는 딕셔너리는 없다.
# items 매서드를 이용해서 튜플로 만들고 람다식을 써야 할 듯.

print(word1)

n2 = list(map(str, input()))
# print(n1)

word2 = dict()

for i in n2:

    if word2.get(i):
        word2[i] +=1

    else:
        word2[i] =1

word2 = sorted(word2.items(), key= lambda x: x[0])
# sorted(word2, key= lambda x: x[0])
# sorted(word2)
print(word2)

if word1 == word2:
    print("YES")