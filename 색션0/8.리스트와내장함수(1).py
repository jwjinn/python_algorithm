import random as r

# 빈 리스트 생성
a = []
b = list()

# 내용있는 리스트 생성
a = [1, 2, 3, 4, 5]
# print(a)
# print(a[0])

b = list(range(1, 11))
# print(b)

# 두 리스트를 합침.
c = a + b
# print(c)

# 리스트 맨 마지막에 값 추가
print(a)
a.append(6)
print(a)

# n번 인덱스에 값 추가
a.insert(3, 7) # 3번 인덱스에 7
print(a)

# 맨 마지막 값 뺀다.
print(a.pop())

print("pop이후 리스트")
print(a)

# 원하는 인덱스 값을 뺀다.
a.pop(3)
print(a)

# 리스트에서 원하는 값을 제거
a.remove(4) # 인덱스 번호가 아닌 값을 제거.
print(a)

# 리스트에서 해당 값의 인덱스를 출력
print(a.index(5)) # 5라는 값의 index를 출력


# 리스트에서 산술함수
a = list(range(1, 11))
print(a)
print(sum(a))

print(max(a))
print(min(a))

print(min(7, 5))


print(a)

# 정렬

# 무작위
r.shuffle(a)
print(a)

# 내림차순
a.sort(reverse=True)
print(a)

# 오름차순
a.sort()
print(a)

#초기화
a.clear()
print(a)