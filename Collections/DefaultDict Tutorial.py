from collections import defaultdict
ls = list()
d = defaultdict(list)
A,*B = input().split()

A = int(A)
B = int(*B)

for i in range(A):
    inp1 = input()
    d[inp1].append(i+1)

for _ in range(B):
    inp2 = input()
    ls.append(inp2)
    
l1 = list(d)
l2 = list(d.items())


for i in ls: 
    if i in d:
        a = str(i)
        b = list(d[a])
        print(*b,sep=' ')
    else:
        print ("-1")
