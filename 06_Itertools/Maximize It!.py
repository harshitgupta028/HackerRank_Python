from itertools import product
Tc,M=map(int, input().split())
lis=[]
lst=(list(map(int, input().split())) [1:] for _ in range(Tc))
z=map(lambda x: sum(i**2 for i in x)%M, product(*lst))
print(max(z))

===================================================================================================
Alternate
===================================================================================================

from itertools import product
Tc,M=map(int, input().split())
lis=[]
lst=(list(map(int, input().split())) [1:] for _ in range(Tc))
#print(*lst)

z=list(product(*lst))

for i in z:
    s=0
    for j in i:
        s=s+(j**2)
    lis.append(s%M)
print(max(lis))