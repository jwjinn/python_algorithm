
# 리스트 슬라이싱
a = [23, 12 ,36, 53, 19]
print(a[:3])


# enumerate: 리스트의 인덱스와 값을 동시에 리턴
for x in enumerate(a):
    print(x)
    print(x[0])

# 리스트는 값 변경이 된다.
b = [1, 2, 3, 4, 5]
b[0] = 7
print(b) # 튜플은 안됨


# enumerate 사용법
for x in enumerate(a):
    print(x[0], x[1])

print()

for index, value in enumerate(a):
    print(index, value)

print()


# 함수 사용법

# 모두가 참이라면
print(a)

if all(60 > x for x in a):
    print("YES")
else:
    print("NO")


if all(50 > x for x in a):
    print("YES")
else:
    print("NO")

# 하나라도 참이라면
if any(15 > x for x in a):
    print("YES")
else:
    print("NO")