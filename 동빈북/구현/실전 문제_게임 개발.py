n, m = map(int, input().split())
location = list(map(int, input().split()))
heading = location[2]
driection = {0 : [-1, 0],
            1 : [0, 1],
            2 : [1, 0],
            3 : [0, -1]}

field = [0 for i in range(n)]
cnt = noway = 0
for i in range(n):
    field[i] = list(map(int, input().split()))

start = [location[0], location[1]]
character = start

def turn_left(n):
        if n == 0:
            return 3
        else:
            return n-1

while True:
    go = turn_left(heading)
    character = [x+y for x, y in zip(start, driection[go])]
    for i in range(n):
        for j in range(m):
            if field[i][j] in character == 0:
                cnt += 1
            else:
                character = start
                noway += 1
                if noway == 4:
                    break

print(cnt)
