t = int(input())

for i in range(t):  # 입력받은 횟수 만큼 Case 반복
    n = int(input())    # 품목 개수 입력
    inu = list(map(int, input().split()))   # 할인가, 정상가 리스트 입력
    sale = inu
    print('Case #{}: ' .format(i+1), end='')
    for j in inu:   # 전체 리스트에 접근해 하나씩 비교
        if (j % 3 == 0) and ((j / 3) * 4 in sale): 
            # ㄴ 우연히 4로 나누어 떨어지는 정상가에서 75%가 할인가이니깐 3으로
            # ㄴ 나누어 떨어지고, 할인가를 다시 정상가로 바꾼가격이 있다면 sale 리스트에서 제거
            sale.remove((j / 3) * 4) # 정상가를 한개씩 제거

    for s in range(len(sale)):
        print(sale[s], end=' ') # 남은 할인가 출력
    print()# Case구분을 위한 출바꿈5