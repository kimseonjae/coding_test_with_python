t = int(input())
button = [300, 60, 10]

for b in button:
    if t % 10 == 0:
        cnt = 0
        cnt += t // b
        t %= b
        print(cnt, end=' ')
    else:
        print(-1)
        break