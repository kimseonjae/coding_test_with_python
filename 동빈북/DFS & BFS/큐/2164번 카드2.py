from collections import deque

n = int(input())   
card_list = deque([])   # deque를 사용하지 않고 하니깐 시간초과가 뜬다.

for i in range(1, n+1):
    card_list.append(i) # N 번까지 카드 번호를 리스트에 담는다.
# print(card_list)
while len(card_list) > 1: # 1장 남을 때까지 카드 버리고 뒤로 보내고 계속 반복
    card_list.popleft() # 가장 먼저 들어온 카드 버리기
    card_list.append(card_list.popleft())  
    # ㄴ 버린 후 가장 위에 있는 카드 맨 뒤로 보내기

print(card_list.pop()) # 한 장 남은 카드 출력