n, m = map(int, input().split())
location = list(map(int, input().split()))
heading = location[2]
driection = {0 : [0, -1],
            1 : [1, 0],
            2 : [0, 1],
            3 : [-1, -0]}

field = [0 for i in range(n)]

for i in range(n):
    field[i] = list(map(int, input().split()))

def move_head(n):
    n -= 1
    if n < 0:
        n = 3
    return n

cnt = 1
# head = move_head(heading)
character = [location[0], location[1]]
# print('driection[head] :' ,driection[head])
# print('driection[head][0], driection[head][1] : ', driection[head][0], driection[head][1])
field[character[0]][character[1]] = 1

while True:
    check = 0
    print('cnt : ', cnt)
    print('현재 character : ', character)
    for i in range(4):
        print('for 문 입장')
        head = move_head(i)
        print('head : ', head)
        move = [int(character[0])+int(driection[head][0]), int(character[1])+int(driection[head][1])]
        print('현재 move : ', move)
        # print(field[character[0], character[1]])
        print('field[move[0]][move[1]] : ', field[move[0]][move[1]])
        if field[move[0]][move[1]] == 0:
            print('if')
            cnt += 1
            check += 1
            x, y = move[0], move[1]
            print('x, y : ', x, y)
            field[move[0]][move[1]] = 1
        print(i+1, '번')
    character = [x, y]
    # break
    if check == 0:
        print(cnt)
        break

