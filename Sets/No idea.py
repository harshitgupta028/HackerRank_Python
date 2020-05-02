
l,f=input().split()

P=list(map(int, input().split()))

A=set(map(int, input().split()))

B=set(map(int, input().split()))

E=0
D=0

for c in P:
    if c in A:
        E+=1
    if c in B:
        D+=1
        
print(E-D) 
