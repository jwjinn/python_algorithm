
# 대/소문자
msg = "It is Time"
print(msg.upper())
print(msg.lower())

# 위치확인
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))

# T가 몇개 있는가?
print(tmp.count('T'))

# slices
print(msg[:2])
print(msg[3:5])


# 길이
print(len(msg))

# 문자열 출력
for i in range(len(msg)):
    print(msg[i], end=" ")

print()

for x in msg:
    print(x, end = ' ')

print()

# 대문자만 출력

for x in msg:
    if x.isupper():
        print(x , end=' ')

print()

# 소문자만 출력

for x in msg:
    if x.islower():
        print(x , end=' ')

print()

# 알파벳만 출력

for x in msg:
    if x.isalpha():
        print(x , end=' ')

print()

# 아스키코드로 - chr를 ord(숫자)로 변경해라.

tmp = 'AZ'

for x in tmp:
    print(ord(x))


tmp = 'az'

for x in tmp:
    print(ord(x))

# 아스키를 글자로.

tmp = 65
print(chr(tmp))