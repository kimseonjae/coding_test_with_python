n = int(input())    # 입력 받은 횟수
result = [] # 결과 출력할 리스트

for _ in range(n):  # 입력 받은 횟수만큼 반복
    t = str(input())    # 괄호들 입력받음
    stack = []  # stack 선언
    cnt = 0 # 스택이 비어있을때의 상황을 위해 확인용
    for i in t: # 입력받은 괄호들 하나씩 접근
        if i == '(':    # '(' 이라면 stack에 넣어줌
            stack.append(i)
        elif i == ')': 
            if len(stack) > 0:  # ')' 이라면 stack이 비어있지 않을때 pop
                stack.pop()
            else:   # 비어있었으면 +1
                cnt += 1
    if len(stack) == 0 and cnt <= 0: # stack의 길이가 0이고 cnt가 0 이하면 
        result.append('YES')    # YES 출력
    else:   # stack의 길이가 0 이어도 cnt가 1이상이면 NO, stack의 길이가 1이상이어도 NO
        result.append('NO')

for i in result:    #결과들 하나씩 출력
    print(i)