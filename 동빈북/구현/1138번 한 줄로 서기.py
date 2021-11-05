n = int(input())
h = list(map(int, input().split()))

# abc = [0 for _ in range(n)]
line_up = []

for i in range(n):
    line_up.insert(h[n-1-i], n-i)

for iine in line_up:
    print(iine, end=' ')

# for i in range(n):
#     print(abc)
#     if h[i] == 0:
#         print('if')
#         cnt = i
#         while abc[cnt] != 0:
#             cnt += 1

#             if cnt >= n:
#                 cnt = 0
            

#         abc[cnt] = i+1
#         # abc[n-i-1] = i+1
#     else:
#         if abc[h[i]] != 0:
#             print('else-if')
#             cnt = i
#             while abc[cnt] != 0:
#                 print('else-if-while')
#                 cnt += 1
#                 if cnt > n:
#                     cnt = 0
#             abc[cnt] = i+1
#         else:
#             print('else-else')
#             abc[h[i]] = i+1
        

# for a in abc:
#     print(a, end=' ')
