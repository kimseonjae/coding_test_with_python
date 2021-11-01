pay = int(input())
cnt = 0

while pay > 0:
    if pay >= 500:
        cnt += pay // 500
        pay %= 500

    elif pay >= 100:
        cnt += pay // 100
        pay %= 100
    
    elif pay >= 50:
        cnt += pay // 50
        pay %= 50

    elif pay >= 10:
        cnt += pay // 10
        pay %= 10
    
print(cnt)

####################################
####################################
## 모법 답안
pay = int(input())
cnt = 0
coin_type = [500, 100, 50, 10]

for coin in coin_type:
    cnt += pay // coin
    pay %= coin

print(cnt)