n = int(input())
array = list(map(int, input().split()))

m = int(input())
find_array = list(map(int, input().split()))

for find in find_array:
    if find in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
