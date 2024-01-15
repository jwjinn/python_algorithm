import sys
# sys.stdin=open("input.txt", "rt")

a=  input()

# print(a)

stack = []

for x in a:
    if x.isdecimal():
        stack.append(x)

    else:
        first_number = int(stack.pop())
        second_number = int(stack.pop())

        if x == '*':
            result = first_number * second_number
            stack.append(result)

        elif x == '/':
            result = first_number / second_number
            stack.append(result)
                   
        elif x == '+':
            result = first_number + second_number
            stack.append(result)

        elif x == '-':
            result = second_number - first_number
            stack.append(result)


print(stack[0])