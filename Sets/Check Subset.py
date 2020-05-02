l1 = int(input())

for i in range(l1):
    l2 = int(input())
    A = set(map(int, input().split()))
    #print(A)
    l4 = int(input())
    B = set(map(int, input().split()))
    if  A.issubset(B):
        print("True")
    else:
        print("False")
