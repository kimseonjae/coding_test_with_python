def dduck_slice(h, start, end, m):
    result = 0
    # if start > end:
    #     return None

    cutting = (start + end) // 2
    for dduck in h:
        if dduck - cutting > 0:
            result += dduck - cutting
    
    if result == m:
        return cutting

    elif result > m:
        return dduck_slice(h, cutting, end, m)

    else:
        return dduck_slice(h, start, cutting, m)
    


n, m = map(int, input().split())
h = list(map(int, input().split()))

print(dduck_slice(h, min(h), max(h), m))