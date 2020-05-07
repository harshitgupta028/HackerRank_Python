from collections import deque
d=deque()

inp = int(input())

for i in range(inp):

        perform,*no = input().split()
        #if len(no) != 0:
        if perform == 'append':
            d.append(no)
        elif perform == 'appendleft':
            d.appendleft(no)
        elif perform == 'pop':
            d.pop()
        else:
            d.popleft()
            
for p in d:
    print(*p,end=' ')