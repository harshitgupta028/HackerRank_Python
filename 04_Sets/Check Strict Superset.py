l1 = set(map(int, input().split()))
l2 = int(input())

C = 0
D = 0

for line in range(l2):
    
    l3 = set(map(int, input().split()))
    #print(l3)
    if l3.issubset(l1) and sum(l1) > sum(l3):
        D = D + 1
    else:
        C = C+1
        
if D > C:
    print("True")
else:
    print("False")
