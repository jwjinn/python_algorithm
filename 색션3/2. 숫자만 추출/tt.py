
st = '00123'

count = 0

for i in st:

    print(i)

    if i == '0':
        count+=1
    else:
        count +=1
        break
        # print(i)
# print()
# print(count)
# print(st[count-1:len(st)])

# print(st[0:len(st)])


# res=0
# for x in st:
#     if x.isdecimal():
#         print(x)
#         res=res*10+int(x)
# print(res)
    
num = '0'

if num.isdecimal():
    print("decimal")