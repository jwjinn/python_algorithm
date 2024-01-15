"""
쇠막대기

(: 여는 괄호일 경우에는 무조건 스텍에 넣고

): 들어올 때는 그전에 들어온 값이 만약 (면 pop하고 토막이 나는 것이므로
길이만큼 더해야 한다.

"""

import sys
sys.stdin=open("input.txt", "r")

content = input()

# print(content)

stack = []
cnt = 0

# for i in content:
#     if i == '(':
#         stack.append(i)

#     if i == ')' and stack[-1] == '(':
#         # 가장 위에 있는 스텍이 '(' 이면 
#         stack.pop()
#         sum += len(stack)

#     if i == '(' and stack[-1] == ')':
#         stack.pop()
#         sum +=1

# print(sum)


for i in content:
    if i == '(':
        stack.append(i)

    else:
        print(content[-1])

        if content[-1] == '(':
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1

print(cnt)