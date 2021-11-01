a = input().split('-')
result = 0

for i in a[0].split('+'):
    result += int(i)

for i in a[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)


#### 반례 찾아보기( 제출하면 안된다.... )
# a = input().split('-')
# plus = minus = 0

# if '+' in str(a):
#     for i in range(len(a)):
#         b = a[i].split('+')
#         if len(b) < 2:
#             minus += int(a[i])
#         else:
#             for j in range(len(b)):
#                 plus += int(b[j])
    
#     if plus > minus and minus != 0:
#         print(minus - plus)
#     else:
#         print(plus - minus)
# else:
#     for i in range(len(a)):
#         if minus == 0:
#             if i == 0:
#                 minus = int(a[i])
#             else:
#                 minus -= int(a[i])
#         else:
#             minus -= int(a[i]) 
#     print(minus)