from collections import deque
stack = deque([])
result = deque([])

def push(n): return stack.append(n)

def pop():
    if len(stack) > 0: 
        return result.append(stack.popleft())
    else: return result.append(-1)

def size(): return result.append(len(stack))

def empty():
    if len(stack) > 0: return result.append(0)
    else: return result.append(1)

def front():
    if len(stack) > 0: return result.append(stack[0])
    else: return result.append(-1)

def back():
    if len(stack) > 0: return result.append(stack[-1])
    else: return result.append(-1)

n = int(input())

for _ in range(n):
    order = list(input().split())
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        pop()
    elif order[0] == 'size':
        size()
    elif order[0] == 'empty':
        empty()
    elif order[0] == 'front':
        front()
    elif order[0] == 'back':
        back()

for _ in range(len(result)):
    print(result.popleft())