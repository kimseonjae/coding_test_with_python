n = int(input())
cnt = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = str(h)+str(m)+str(s)
            if '3' in time:
                cnt += 1
print(cnt)

####################################
####################################
## 답안 예시

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)