"""
후위표시식.

숫자와 연산자를 동시에 생각한 것이 패착이지 않았나 싶다.

숫자는 별개로 생각하고 연산자의 경우에는 우선순위를 생각해서 진행했어야 했다.

"""

import sys
sys.stdin=open("input.txt", "r")
a=input()
stack=[]
res=''

for x in a:
    if x.isdecimal():
        res+=x

    else:
        if x == '(':
            stack.append(x)
            # 여는 괄호는 무조건 집어 넣고 봐야.
            # (는 ) 만나기 전까지의 발사대.
        
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                # 우선순위가 높은 연산자. 본인보다 먼저 나온 연산자만이 우선순위가 높다.
                res+=stack.pop()

            stack.append(x)

        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                # 위 두 연산자는 기본적으로 우선순위가 매우 낮다.
                # 그래서 기본적으로 다 pop해야 하는 것이 맞지만.
                # (가 있으면 연산자는 괄호안에 있다는 뜻이므로 pop을 멈춰야 한다.
                res +=stack.pop()

            stack.append(x)

        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)
