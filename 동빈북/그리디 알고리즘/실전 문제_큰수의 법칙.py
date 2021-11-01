n, m, k = map(int, input().split())
number = list(map(int, input().split()))
result = 0

number.sort(reverse=True)
cnt = k

while m > 0:
    m -= 1
    result += number[0]
    cnt -= 1
    
    if cnt == 0:
        m -= 1
        result += number[1]
        cnt = k

print(result)

####################################
####################################
## 동빈북 해설
# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬
first = data[n-1]   # 가장 큰 수
second = data[n-1]  # 두 번째로 큰 수

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기

    if m == 0:  # m이 0이라면 반복문 탈출
        break
    result += second    # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)   # 최종 답안 출력