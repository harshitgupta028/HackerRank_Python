l1 = int(input())
l2 = set(map(int, input().split()))
l3 = int(input())

for i in range(l3):
        l4,k = list(input().split())
        
        l5 = set(map(int, input().split()))
   
        if l4 == 'intersection_update':
            l2.intersection_update(l5)
        elif l4 == 'update':
            l2.update(l5)
        elif l4 == 'symmetric_difference_update':
            l2.symmetric_difference_update(l5)
        else:
            l2.difference_update(l5)
if len(l2) is 0:
    print("0")
else:    
    print(sum(l2))             

